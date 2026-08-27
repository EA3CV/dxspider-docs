#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, html, os, subprocess
from collections import defaultdict

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

def related_links(names):
    if not names: return ""
    rows=["## Related commands",""]
    for c in names:
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

    all_commands=sorted(set(grouped)|set(code))
    public=[]
    missing_help=[]

    for cmd in all_commands:
        variants=grouped.get(cmd,[])
        if not variants:
            missing_help.append(cmd)
            continue

        aud=audience(variants)
        privs=sorted(set(v["privilege"] for v in variants))
        note=notes.get(cmd,{})
        summary=note.get("summary") or variants[0]["description"]
        category=note.get("category","Command reference")
        source_rel=code.get(cmd)
        source_link=""
        if source_rel and source_revision:
            rel=Path(source_rel).relative_to(src).as_posix()
            source_link=f"https://github.com/EA3CV/dxspider/blob/{source_revision}/{rel}"

        page=[
            f"# `{cmd}`","",
            '<div class="command-hero" markdown>',"",
            f"**{summary}**","",
            '<div class="command-meta" markdown>',
            f'<div><span class="meta-label">Audience</span><br><span class="badge badge-{aud.lower()}">{aud}</span></div>',
            f'<div><span class="meta-label">Privilege</span><br>`{" / ".join(map(str,privs))}`</div>',
            f'<div><span class="meta-label">Category</span><br>{category}</div>',
            '<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>',
            '</div>',"",'</div>',"",
        ]

        if len(variants)>1:
            page += ["## Syntax and variants",""]
            for v in variants:
                page += [
                    f'=== "Privilege {v["privilege"]}"',"",
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
        else:
            v=variants[0]
            page += ["## Syntax","", "```text",v["syntax"],"```","",
                     f"**{v['description']}**",""]
            body=body_markdown(v["body"])
            if body:
                page += ["## Details","",body,""]

        examples=note.get("examples",[])
        if examples:
            page += ["## Practical examples",""]
            for title, ex in examples:
                page += [f"### {title}","", "```text",ex,"```",""]

        if aud=="DUAL":
            page += [
                '!!! info "User and SYSOP forms"',
                "    This command has both a normal-user form and one or more privileged forms. "
                "The privilege tabs above are part of the command semantics; they are not merely aliases.",""
            ]

        if source_link:
            page += [
                "## Implementation","",
                f"[View the current command source on GitHub]({source_link}){{ .md-button }}",""
            ]

        rel=note.get("related",[])
        if rel:
            page += [related_links(rel),""]

        page += [
            "## Verify on a running node","",
            "```text",f"HELP {cmd}","```","",
            "The built-in help is useful when checking the exact command set installed on a particular node."
        ]

        (outdir/f"{slug(cmd)}.md").write_text("\n".join(page), encoding='utf-8')
        public.append((cmd,aud,privs,summary))

    # Full index
    idx=["# Command Reference","",
         "Search or browse the current command set. Every page below is generated from the current "
         "`Commands_en.hlp`; where a command also has source code, the page links directly to it.","",
         '<div class="command-filter" markdown>',
         "Use the site search (`/`) for instant lookup by command name, option or help text.",
         "</div>","",
         "| Command | Audience | Privilege | What it does |",
         "|---|---|---:|---|"]
    for cmd,aud,privs,summary in public:
        idx.append(f"| [`{cmd}`]({slug(cmd)}.md) | {aud} | {' / '.join(map(str,privs))} | {summary} |")
    (outdir/'index.md').write_text("\n".join(idx),encoding='utf-8')

    # User and SYSOP indexes
    for target, allowed, title in [
        (docs/'user/commands/index.md', {'USER','DUAL'}, 'User command reference'),
        (docs/'sysop/commands/index.md', {'SYSOP','DUAL'}, 'SYSOP command reference')
    ]:
        data=[x for x in public if x[1] in allowed]
        md=[f"# {title}","",
            "This list is generated from the current DXSpider help metadata. "
            "Commands marked **DUAL** contain both user and privileged variants.","",
            "| Command | Audience | Privilege | Purpose |","|---|---|---:|---|"]
        for cmd,aud,privs,summary in data:
            md.append(f"| [`{cmd}`](../../reference/commands/{slug(cmd)}.md) | {aud} | {' / '.join(map(str,privs))} | {summary} |")
        target.write_text("\n".join(md),encoding='utf-8')

    audit=docs/'audit/generated-reference.md'
    audit.parent.mkdir(parents=True,exist_ok=True)
    audit.write_text(
        "# Generated reference audit\n\n"
        f"- Help entries parsed: **{len(entries)}**\n"
        f"- Unique commands documented from help: **{len(public)}**\n"
        f"- `.pl` command files without a matching help header: **{len(missing_help)}**\n\n"
        "## Code-present commands without help\n\n" +
        ("\n".join(f"- `{x}`" for x in missing_help) if missing_help else "_None._")
    )

    print(f"Generated {len(public)} command pages from {helpfile}")
    print(f"Code commands without help: {len(missing_help)}")

if __name__ == '__main__':
    main()
