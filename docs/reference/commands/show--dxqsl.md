# `SHOW/DXQSL`

<div class="command-hero" markdown>

**Show any QSL info gathered from spots**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/dxqsl.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DXQSL
```

The built-in help is useful when checking the exact command set installed on a particular node.