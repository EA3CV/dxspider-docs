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
                 "Available in the current DXSpider version; practical description pending.")
        category=note.get("category","Command reference")

        page=[
            f"# `{cmd}`","",
            '<div class="command-hero" markdown>',"",
            f"**{summary}**","",
            '<div class="command-meta" markdown>',
            f'<div><span class="meta-label">Guide</span><br><span class="badge badge-{aud.lower()}">{("Administration" if aud=="SYSOP" else "User / general")}</span></div>',
            f'<div><span class="meta-label">Category</span><br>{category}</div>',
            '<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>',
            '</div>',"",'</div>',"",
        ]

        if facts:
            page += ["## Usage","", "```text", f"{cmd} {facts['usage'].split(' ',1)[1] if ' ' in facts['usage'] else ''}".rstrip(), "```",""]
            if facts["restrictions"]:
                friendly=[]
                if facts["direct_privilege_guard"]:
                    friendly.append("This command is restricted to an appropriately privileged operator.")
                if any("remote-command" in x for x in facts["restrictions"]):
                    friendly.append("It cannot be run through remote-command execution.")
                if any("scripts" in x for x in facts["restrictions"]):
                    friendly.append("It cannot be run from a command script.")
                if any("local connection" in x for x in facts["restrictions"]):
                    friendly.append("It must be run from a local connection.")
                if friendly:
                    page += ["### Who can use it",""] + [f"- {x}" for x in friendly] + [""]
            if facts["named_fields"]:
                page += ["### Arguments","",
                         ", ".join(f"`{x}`" for x in facts["named_fields"]),""]
            if facts["recognized_tokens"]:
                page += ["### Available options and values","",
                         ", ".join(f"`{x}`" for x in facts["recognized_tokens"]),"",
                         "The valid combinations are described in the command forms and examples below.",""]
        else:
            page += ['!!! danger "Not available in this version"',
                     "    This help entry does not correspond to an available command in the checked DXSpider version.",""]

        if len(variants)>1:
            page += ["## Command forms and examples","",]
            for v in variants:
                page += [
                    f'=== "Available form"',"",
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
            page += ["## Command description","",
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
            page += ['!!! info "Documentation status"',
                     "    This command is part of the current DXSpider command set, but a fuller practical description and additional tested examples are still needed.",""]

        rel=note.get("related",[])
        if rel:
            related = related_links(rel, set(code))
            if related:
                page += [related,""]

        page += [
            "## Verify on a running node","", "```text",f"HELP {cmd}","```","",
            "Use the node help to check for local overrides or differences in another installed revision."
        ]

        (outdir/f"{slug(cmd)}.md").write_text("\n".join(page), encoding='utf-8')
        public.append((cmd,aud,privs,summary))

    # Full index
    idx=["# Command Reference","",
         "Search or browse the current command set. Each page is checked against the current DXSpider implementation and presented as a practical guide.","",
         "Use the site search (`/`) for instant lookup by command name, option or help text.",
         "</div>","",
         "| Command | Guide | What it does |",
         "|---|---|---|"]
    for cmd,aud,privs,summary in public:
        guide = "Administration" if aud=="SYSOP" else "User / general"
        idx.append(f"| [`{cmd}`]({slug(cmd)}.md) | {guide} | {summary} |")
    (outdir/'index.md').write_text("\n".join(idx),encoding='utf-8')

    # User and SYSOP indexes
    for target, allowed, title in [
        (docs/'user/commands/index.md', {'USER'}, 'User and general commands'),
        (docs/'sysop/commands/index.md', {'SYSOP'}, 'Administration commands')
    ]:
        data=[x for x in public if x[1] in allowed]
        md=[f"# {title}","",
            "This list is generated from the current DXSpider command set and organized by intended audience.","",
            "| Command | Guide | Purpose |","|---|---|---|"]
        for cmd,aud,privs,summary in data:
            guide = "Administration" if aud=="SYSOP" else "User / general"
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
