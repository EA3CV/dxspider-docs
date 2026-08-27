# Final command audit

Public identity: **DXSpider 1.57 — Mojo build 686 and later**

## Inventory

- Family/subcommands from supplied table and current source additions: **247**
- Root command files added from the current command tree: **62**
- Total audited command entries: **309**
- Publicly documented entries: **305**
- Internal/unsupported entries intentionally excluded: **4**

## Internal/unsupported entries

- `set/uservar` — Not published as a supported operational command pending code-control-flow review.
- `dbdelkey` — Current file is a no-op placeholder; not exposed as supported documentation.
- `dbupdate` — Current file is a no-op placeholder; not exposed as supported documentation.
- `do` — Local authorization d Perl-eval command; intentionally excluded from normal operational docs.

## Documentation rule

No source-tree command is promoted to normal user documentation merely because its code has no explicit authorization check. Operational/internal commands can be classified as SYSOP by purpose, and unusual raw-internal commands are excluded from public navigation.
