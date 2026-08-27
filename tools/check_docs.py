#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path('docs')
broken=[]
pat=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for p in root.rglob('*.md'):
    for t in pat.findall(p.read_text(errors='replace')):
        t=t.split()[0].strip('<>').split('#')[0]
        if not t or t.startswith(('http://','https://','mailto:')):
            continue
        if not (p.parent/t).resolve().exists():
            broken.append((p,t))
if broken:
    for p,t in broken[:50]:
        print("BROKEN",p,t)
    raise SystemExit(1)
print(f"OK: {len(list(root.rglob('*.md')))} Markdown files; no broken relative links.")
