# `STAT/USER`

<div class="command-hero" markdown>

**Show the full status of a user**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
STAT/USER [token ...]
```

## Command description

```text
STAT/USER [<callsign>]
```

**Show the full status of a user**

## Details

Shows the full contents of a user record including all the secret flags
and stuff.

Only the fields that are defined (in perl term) will be displayed.

## Verify on a running node

```text
HELP STAT/USER
```

Use the node help to check for local overrides or differences in another installed revision.