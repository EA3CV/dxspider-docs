# `SHOW/DXQSL`

<div class="command-hero" markdown>

**Show any QSL info gathered from spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/DXQSL [token ...]
```

## Command description

```text
SHOW/DXQSL <callsign>
```

**Show any QSL info gathered from spots**

## Details

The node collects information from the comment fields in spots (things
like 'VIA EA7WA' or 'QSL-G1TLH') and stores these in a database.

This command allows you to interrogate that database and if the callsign
is found will display the manager(s) that people have spotted. This
information is NOT reliable, but it is normally reasonably accurate if
it is spotted enough times.

For example:-

```text
sh/dxqsl 4k9w
```

You can check the raw input spots yourself with:-

```text
sh/dx 4k9w qsl
```

This gives you more background information.

## Verify on a running node

```text
HELP SHOW/DXQSL
```

Use the node help to check for local overrides or differences in another installed revision.