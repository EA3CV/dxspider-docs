"""Conservative, source-first command facts for DXSpider documentation.

The extractor intentionally reports only facts visible in a command handler.
It never turns a filename or stale help header into asserted behaviour.
"""
from pathlib import Path
import hashlib
import re


def _clean(line):
    return re.sub(r"\s+", " ", line).strip()


def _matching_lines(lines, pattern, limit=40):
    rx = re.compile(pattern)
    result = []
    for number, line in enumerate(lines, 1):
        if not line.lstrip().startswith("#") and rx.search(line):
            result.append((number, _clean(line)))
            if len(result) >= limit:
                break
    return result


def _evidence_block(items):
    return "\n".join(f"L{number}: {line}" for number, line in items)


def inspect_command(path):
    path = Path(path)
    source = path.read_text(errors="replace")
    lines = source.splitlines()

    argument_lines = _matching_lines(
        lines,
        r"\$line\b|\bshift\b|\bsplit\b|=~\s*[ms]?[/|{]|\@args\b|\@list\b",
    )
    validation_lines = _matching_lines(
        lines,
        r"\b(?:unless|if)\b.*(?:is_callsign|validcall|is_qra|looks_like_number|=~|!~|defined|priv|remotecmd|inscript)|\breturn\b.*->msg\(",
    )
    output_lines = _matching_lines(
        lines,
        r"\breturn\s*\(|push\s+\@out|->msg\(|->send\(",
    )

    thresholds = sorted({int(x) for x in re.findall(r"\$self->priv\s*<\s*(\d+)", source)})
    named_fields=[]
    for match in re.finditer(r"my\s*\(([^)]+)\)\s*=\s*split[^;]+\$line", source):
        named_fields.extend(re.findall(r"\$([A-Za-z_][A-Za-z0-9_]*)", match.group(1)))
    named_fields=list(dict.fromkeys(named_fields))
    recognized=[]
    recognized += re.findall(r"(?:lc\s+)?\$[A-Za-z_]\w*\s+eq\s+['\"]([^'\"]+)", source)
    recognized += re.findall(r"\$args\{([A-Za-z_][A-Za-z0-9_]*)\}", source)
    for group in re.findall(r"qw(?:\(|\{|\|)(.*?)(?:\)|\}|\|)", source, re.S):
        recognized += re.findall(r"[A-Za-z_][A-Za-z0-9_/-]*", group)
    recognized=sorted(set(recognized), key=str.lower)
    restrictions = []
    if thresholds:
        restrictions.append("The handler contains a direct privilege guard.")
    if "remotecmd" in source:
        restrictions.append("The handler restricts remote-command execution.")
    if "inscript" in source:
        restrictions.append("The handler restricts execution from scripts.")
    if "consort ne 'local'" in source or 'consort ne "local"' in source:
        restrictions.append("The handler requires a local connection context.")

    if not re.search(r"\$line\b", source):
        input_model = "No command arguments are consumed by this handler."
        usage = path.stem.upper()
    elif re.search(r"->(?:cmd|parse|run_cmd|command)\([^\n]*\$line", source):
        input_model = "The complete argument line is delegated to another parser. Follow the cited call for the final grammar."
        usage = f"{path.stem.upper()} <arguments accepted by delegated parser>"
    elif re.search(r"split\s*/\\s[+*]/", source):
        input_model = "The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality."
        usage = f"{path.stem.upper()} [token ...]"
    elif re.search(r"map\s*\{\s*split|split\s*/[^/]*(?:,|=)[^/]*/", source):
        input_model = "The handler parses a structured list (for example comma-separated or key/value input). See parser evidence."
        usage = f"{path.stem.upper()} <structured arguments>"
    elif re.search(r"->\w+\(\s*\$line\s*\)", source):
        input_model = "The complete argument line is used as one value without prior tokenization in this handler."
        usage = f"{path.stem.upper()} [text]"
    else:
        input_model = "The handler uses a custom parser or treats the argument line as free text. See parser evidence."
        usage = f"{path.stem.upper()} [arguments; see parser evidence]"

    effects = []
    for pattern, label in [
        (r"->put\s*\(", "Persists a DXUser record with `put()`."),
        (r"->del\s*\(", "Deletes a DXUser record."),
        (r"Filter::|filterdef|->write\s*\(", "Reads or modifies filter state/files."),
        (r"DXSql|\$main::dbh", "Uses the SQL subsystem."),
        (r"->disconnect\s*\(", "Can disconnect a live session."),
        (r"route_pc|\bpc\d+\b", "Uses or emits DX protocol data."),
        (r"\bunlink\s*\(", "Can remove a file."),
        (r"\bopen\s*\(", "Performs file I/O."),
        (r"DXCluster|DXClusterSnapshot", "Uses cluster synchronization/state code."),
        (r"Spot::|spot_search", "Reads or changes spot data."),
        (r"DXMsg|Msg::", "Uses the internal message subsystem."),
        (r"DXCron", "Uses scheduled-command state."),
    ]:
        if re.search(pattern, source, re.I):
            effects.append(label)

    comments = []
    for line in lines[:45]:
        match = re.match(r"\s*#\s*(.+?)\s*$", line)
        if match and not re.match(r"copyright|^[#=\-]+$|!/", match.group(1), re.I):
            text = _clean(match.group(1))
            if text and text not in comments:
                comments.append(text)

    calls = sorted(set(re.findall(
        r"\b([A-Z][A-Za-z0-9_:]+(?:::[A-Za-z0-9_]+)|[A-Za-z_][A-Za-z0-9_]*->(?:[A-Za-z_][A-Za-z0-9_]*))\s*\(",
        source,
    )))
    message_keys = sorted(set(re.findall(r"->msg\(\s*['\"]([^'\"]+)", source)))

    return {
        "source": source,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "line_count": len(lines),
        "summary": " ".join(comments[:3]),
        "usage": usage,
        "input_model": input_model,
        "direct_privilege_guard": bool(thresholds),
        "restrictions": restrictions,
        "effects": effects,
        "calls": calls,
        "message_keys": message_keys,
        "named_fields": named_fields,
        "recognized_tokens": recognized,
        "argument_evidence": _evidence_block(argument_lines),
        "validation_evidence": _evidence_block(validation_lines),
        "output_evidence": _evidence_block(output_lines),
    }
