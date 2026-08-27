# Phase 2 — audience and documentation audit

This is working audit material, not final public documentation.

## Inventory correction

The original quick parser split rows on whitespace and could shift cells when status text had different lengths. The corrected parser uses the fixed start positions of the table headers.

- Commands from supplied table: **241**
- Additional code-present commands already identified: **6**
- Working inventory: **247**

## Audience state

- USER: **83**
- SYSOP: **59**
- DUAL: **17**
- REVIEW: **88**

Uncertain commands stay in **REVIEW** rather than being classified by intuition.

## Confirmed documentation gaps

### `set/width`

Exists in the current implementation and updates both the active session width and the stored user width. It is absent from the command help, Administration Manual v1.51 and User Command Reference wiki checked during this audit.

### `set/homebbs`

Exists in the current implementation, acts on the current user and persists the home mail BBS. It is absent from the legacy documentation sources checked.

### `show/users`

Exists in the current implementation and reads routing/user information, but no current help entry was found. Its audience remains REVIEW until the access path is verified.

## Dual semantics already confirmed

### `set/password`

- `SET/PASSWORD` — normal user changes their own existing password.
- `SET/PASSWORD <callsign> <password>` — SYSOP operation requiring privilege 9.

### Filter families

Several ACCEPT, REJECT and CLEAR commands have a privilege-0 user form and a separate privilege-8 SYSOP form for another callsign or defaults.

## Legacy-content warning

Current route-filter help still describes behaviour using legacy PC protocol records. That text should not be copied mechanically into the new manual.

## Publication gate

A command is published only after its existence, access rules, syntax, target semantics, persistence and important side effects have been verified.
