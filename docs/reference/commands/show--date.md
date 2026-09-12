# `SHOW/DATE`

<div class="command-hero" markdown>

**Show the local time**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/DATE [token ...]
```

## Command description

```text
SHOW/DATE [<prefix>|<callsign>]
```

**Show the local time**

## Details

This is very nearly the same as SHOW/TIME, the only difference the format
of the date string if no arguments are given.

If no prefixes or callsigns are given then this command returns the local
time and UTC as the computer has it right now. If you give some prefixes
then it will show UTC and UTC + the local offset (not including DST) at
the prefixes or callsigns that you specify.

## Verify on a running node

```text
HELP SHOW/DATE
```

Use the node help to check for local overrides or differences in another installed revision.