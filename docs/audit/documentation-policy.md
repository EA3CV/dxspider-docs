# Documentation policy

## Public identity

> **DXSpider 1.57 — applicable to Mojo build 686 and later**

Development-branch naming is not part of the public documentation.

## Source priority

1. Current implementation.
2. Current command-help metadata, when consistent with implementation.
3. Current wiki documentation.
4. Administration Manual v1.51.
5. Historical material, explicitly marked as historical.

## Audience separation

- Normal-user command forms belong in **User**.
- Privileged forms belong in **SYSOP / Administration**.
- If one command name has both forms, each form is documented in its own audience section.

## No inferred semantics

Command names are not sufficient evidence for behaviour. Targeting, persistence, side effects and privilege are verified before publication.
