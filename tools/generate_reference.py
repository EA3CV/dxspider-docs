#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, html, os, subprocess
from collections import defaultdict
from code_intel import inspect_command

HEADER = re.compile(r'^===\s+(\d+)\^([^^]+)\^(.*)$')

def canonical_from_syntax(s):
    token = s.strip().split()[0].upper()
    token = token.rstrip('-')
    return token

def parse_help(path):
    entries=[]
    current=None
    for raw in Path(path).read_text(errors='replace').splitlines():
        m=HEADER.match(raw)
        if m:
            if current:
                entries.append(current)
            current={
                "privilege": int(m.group(1)),
                "syntax": m.group(2).strip(),
                "description": m.group(3).strip(),
                "body": []
            }
            continue
        if current is not None:
            current["body"].append(raw.rstrip())
    if current:
        entries.append(current)
    for e in entries:
        e["command"]=canonical_from_syntax(e["syntax"])
    return entries

def scan_code(cmd_root):
    cmds={}
    root=Path(cmd_root)
    if not root.exists():
        return cmds
    for p in root.rglob('*.pl'):
        rel=p.relative_to(root).with_suffix('')
        cmd='/'.join(rel.parts).upper()
        cmds[cmd]=str(p)
    return cmds

def slug(cmd):
    return cmd.lower().replace('/','--').replace('_','-')

def audience(entries):
    privs=sorted(set(e["privilege"] for e in entries))
    if 0 in privs and any(p>0 for p in privs): return "DUAL"
    if privs == [0]: return "USER"
    return "SYSOP"

def body_markdown(lines):
    # Preserve authoritative help faithfully but make it readable.
    # Detect indented/example-like lines as code blocks.
    out=[]
    code=[]
    def flush():
        nonlocal code
        if code:
            out.append("```text")
            out.extend([x[2:] if x.startswith("  ") else x for x in code])
            out.append("```")
            code=[]
    for ln in lines:
        if not ln.strip():
            flush()
            out.append("")
            continue
        if ln.startswith("  ") or ln.startswith("\t"):
            code.append(ln)
        else:
            flush()
            out.append(ln)
    flush()
    # reduce excessive blank lines
    cleaned=[]
    for x in out:
        if x=="" and cleaned and cleaned[-1]=="":
            continue
        cleaned.append(x)
    return "\n".join(cleaned).strip()

def related_links(names, available_commands):
    if not names:
        return ""

    valid = [c for c in names if c in available_commands]
    if not valid:
        return ""

    rows = ["## Related commands", ""]
    for c in valid:
        rows.append(f"- [`{c}`]({slug(c)}.md)")
    return "\n".join(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source', required=True, help='Path to DXSpider checkout')
    ap.add_argument('--docs', default='docs')
    ap.add_argument('--notes', default='data/command_notes.json')
    args=ap.parse_args()

    src=Path(args.source)
    docs=Path(args.docs)
    try:
        source_revision = subprocess.check_output(
            ["git", "-C", str(src), "rev-parse", "HEAD"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        source_revision = ""
    helpfile=src/'cmd/Commands_en.hlp'
    if not helpfile.exists():
        raise SystemExit(f"Missing {helpfile}")

    entries=parse_help(helpfile)
    grouped=defaultdict(list)
    for e in entries:
        grouped[e["command"]].append(e)

    code=scan_code(src/'cmd')
    notes=json.loads(Path(args.notes).read_text()) if Path(args.notes).exists() else {}

    outdir=docs/'reference/commands'
    outdir.mkdir(parents=True, exist_ok=True)
    # Keep index, regenerate command pages.
    for p in outdir.glob('*.md'):
        if p.name != 'index.md':
            p.unlink()

    # Executable handlers define the public inventory. Help-only headers are
    # audited separately and never promoted to executable commands.
    all_commands=sorted(code)
    help_without_code=sorted(set(grouped)-set(code))
    public=[]
    missing_help=[]

    for cmd in all_commands:
        variants=grouped.get(cmd,[])
        source_rel=code.get(cmd)
        facts=inspect_command(source_rel) if source_rel else None
        if not variants:
            missing_help.append(cmd)

        # Code is authoritative. Help privilege metadata is never used to claim
        # authorization. A direct source guard is enough to place a command in
        # the administration index; delegated checks remain visibly unresolved.
        aud="SYSOP" if facts and facts["direct_privilege_guard"] else "USER"
        privs=sorted(set(v["privilege"] for v in variants))
        note=notes.get(cmd,{})
        summary=(note.get("summary") or (variants[0]["description"] if variants else "") or
                 (facts and facts["summary"]) or "Source-present command; review implementation evidence.")
        category=note.get("category","Command reference")
        source_link=""
        source_display=""
        if source_rel and source_revision:
            rel=Path(source_rel).relative_to(src).as_posix()
            source_link=f"https://github.com/EA3CV/dxspider/blob/{source_revision}/{rel}"
        if source_rel:
            try:
                source_display=Path(source_rel).relative_to(src).as_posix()
            except ValueError:
                source_display=str(source_rel)

        page=[
            f"# `{cmd}`","",
            '<div class="command-hero" markdown>',"",
            f"**{summary}**","",
            '<div class="command-meta" markdown>',
            f'<div><span class="meta-label">Code classification</span><br><span class="badge badge-{aud.lower()}">{("Direct administration guard" if aud=="SYSOP" else "No direct handler guard")}</span></div>',
            f'<div><span class="meta-label">Category</span><br>{category}</div>',
            '<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>',
            '</div>',"",'</div>',"",
        ]

        page += [
            '!!! warning "Implementation is authoritative"',
            "    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.",""
        ]

        if facts:
            page += ["## Effective interface from code","", "```text", f"{cmd} {facts['usage'].split(' ',1)[1] if ' ' in facts['usage'] else ''}".rstrip(), "```","",
                     facts["input_model"],""]
            if facts["restrictions"]:
                page += ["### Access and execution restrictions",""] + [f"- {x}" for x in facts["restrictions"]] + [""]
            else:
                page += ["### Access and execution restrictions","",
                         "No direct privilege, remote-command, script, or local-context guard was found in this handler. "
                         "This does not rule out checks in delegated functions or the surrounding session path.",""]
            if facts["effects"]:
                page += ["### Observable implementation effects",""] + [f"- {x}" for x in facts["effects"]] + [""]
            if facts["named_fields"]:
                page += ["### Named fields consumed by the parser","",
                         ", ".join(f"`{x}`" for x in facts["named_fields"]),""]
            if facts["recognized_tokens"]:
                page += ["### Recognized tokens, keys or enumerated values in this handler","",
                         ", ".join(f"`{x}`" for x in facts["recognized_tokens"]),"",
                         "These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. "
                         "Their exact role and combinations are established by the parser evidence below.",""]
            if facts["calls"]:
                page += ["### Important calls", "", ", ".join(f"`{x}()`" for x in facts["calls"]), ""]
            for title,key in [
                ("Argument parsing evidence","argument_evidence"),
                ("Validation and access evidence","validation_evidence"),
                ("Output and error evidence","output_evidence"),
            ]:
                if facts[key]:
                    page += [f"### {title}","",f"Source: `{source_display}` · SHA-256 `{facts['sha256']}`","", "```perl", facts[key], "```",""]
            if facts["message_keys"]:
                page += ["### Message keys returned", "", ", ".join(f"`{x}`" for x in facts["message_keys"]), ""]
        else:
            page += ['!!! danger "No command handler found"',
                     "    This help entry has no matching `cmd/*.pl` handler in the checked source tree and is not asserted to be executable.",""]

        if len(variants)>1:
            page += ["## Built-in help (secondary)","",
                     "The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.",""]
            for v in variants:
                page += [
                    f'=== "Help variant"',"",
                    "    ```text",
                    f'    {v["syntax"]}',
                    "    ```","",
                    f'    **{v["description"]}**',""
                ]
                body=body_markdown(v["body"])
                if body:
                    for line in body.splitlines():
                        page.append("    "+line if line else "")
                page.append("")
        elif variants:
            v=variants[0]
            page += ["## Built-in help (secondary)","",
                     "This section comes from `Commands_en.hlp` and may lag the implementation.","",
                     "```text",v["syntax"],"```","",
                     f"**{v['description']}**",""]
            body=body_markdown(v["body"])
            if body:
                page += ["## Details","",body,""]

        why=note.get("why","")
        if why:
            page += ["## When would I use this?","",why,""]

        examples=note.get("examples",[])
        if examples:
            page += ["## Practical examples",""]
            for title, ex in examples:
                page += [f"### {title}","", "```text",ex,"```",""]

        if not variants:
            page += ['!!! info "No built-in help entry"',
                     "    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. "
                     "Its page is therefore derived from implementation evidence only.",""]

        if source_link:
            page += [
                "## Implementation","",
                f"[View the current command source on GitHub]({source_link}){{ .md-button }}",""
            ]

        rel=note.get("related",[])
        if rel:
            related = related_links(rel, set(code))
            if related:
                page += [related,""]

        page += [
            "## Verify on a running node","", "```text",f"HELP {cmd}","```","",
            "Compare the installed handler with this page when local overrides or a different revision may be present."
        ]

        (outdir/f"{slug(cmd)}.md").write_text("\n".join(page), encoding='utf-8')
        public.append((cmd,aud,privs,summary))

    # Full index
    idx=["# Command Reference","",
         "Search or browse the current command set. The inventory is generated from `cmd/*.pl`; "
         "implementation evidence is authoritative and `Commands_en.hlp` is secondary.","",
         '<div class="command-filter" markdown>',
         "Use the site search (`/`) for instant lookup by command name, option or help text.",
         "</div>","",
         "| Command | Guide | What it does |",
         "|---|---|---|"]
    for cmd,aud,privs,summary in public:
        guide = "Direct administration guard" if aud=="SYSOP" else "No direct handler guard"
        idx.append(f"| [`{cmd}`]({slug(cmd)}.md) | {guide} | {summary} |")
    (outdir/'index.md').write_text("\n".join(idx),encoding='utf-8')

    # User and SYSOP indexes
    for target, allowed, title in [
        (docs/'user/commands/index.md', {'USER'}, 'Commands without a direct administration guard'),
        (docs/'sysop/commands/index.md', {'SYSOP'}, 'Commands with a direct administration guard')
    ]:
        data=[x for x in public if x[1] in allowed]
        md=[f"# {title}","",
            "This list is generated from the current command handlers. Classification reflects direct guards "
            "visible in each handler; delegated authorization is called out on the command page.","",
            "| Command | Guide | Purpose |","|---|---|---|"]
        for cmd,aud,privs,summary in data:
            guide = "Direct administration guard" if aud=="SYSOP" else "No direct handler guard"
            md.append(f"| [`{cmd}`](../../reference/commands/{slug(cmd)}.md) | {guide} | {summary} |")
        target.write_text("\n".join(md),encoding='utf-8')

    audit=docs/'audit/generated-reference.md'
    audit.parent.mkdir(parents=True,exist_ok=True)
    audit.write_text(
        "# Generated reference audit\n\n"
        f"- Help entries parsed: **{len(entries)}**\n"
        f"- Unique command pages generated from code + help: **{len(public)}**\n"
        f"- `.pl` command files without a matching help header: **{len(missing_help)}**\n\n"
        "## Code-present commands without help\n\n" +
        ("\n".join(f"- `{x}`" for x in missing_help) if missing_help else "_None._") +
        "\n\n## Help headers without a matching executable handler\n\n" +
        ("\n".join(f"- `{x}`" for x in help_without_code) if help_without_code else "_None._")
    )

    print(f"Generated {len(public)} command pages; cmd/*.pl is authoritative")
    print(f"Code commands without help: {len(missing_help)}")

if __name__ == '__main__':
    main()
