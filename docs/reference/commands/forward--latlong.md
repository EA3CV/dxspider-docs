# `FORWARD/LATLONG`

<div class="command-hero" markdown>

**Send latitude and longitude information to another cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
FORWARD/LATLONG [token ...]
```

## Command description

```text
FORWARD/LATLONG <node_call>
```

**Send latitude and longitude information to another cluster**

## Details

This command sends all the latitude and longitude information that your
cluster is holding against callsigns.  One advantage of recieving this
information is that more locator information is held by you.  This
means that more locators are given on the DX line assuming you have
SET/DXGRID enabled.  This could be a LOT of information though, so
it is not recommended on slow links.

## Verify on a running node

```text
HELP FORWARD/LATLONG
```

Use the node help to check for local overrides or differences in another installed revision.