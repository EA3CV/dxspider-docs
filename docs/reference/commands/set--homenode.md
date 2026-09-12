# `SET/HOMENODE`

<div class="command-hero" markdown>

**Set your normal cluster callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/HOMENODE [text]
```

## Command description

```text
SET/HOMENODE <node>
```

**Set your normal cluster callsign**

## Details

Tell the cluster system where you normally connect to. Any Messages sent
to you will normally find their way there should you not be connected.
eg:-
```text
SET/HOMENODE gb7djk
```

## Verify on a running node

```text
HELP SET/HOMENODE
```

Use the node help to check for local overrides or differences in another installed revision.