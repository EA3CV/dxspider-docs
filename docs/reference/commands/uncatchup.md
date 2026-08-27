# `UNCATCHUP`

<div class="command-hero" markdown>

**Unmark a message as sent**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNCATCHUP <node call> All|[msgno> ...]
```

**Unmark a message as sent**

## Details

When you send messages the fact that you have forwarded it to another node
is remembered so that it isn't sent again. When you have a new partner
node and you add their callsign to your /spider/msg/forward.pl file, all
outstanding non-private messages will be forwarded to them. This may well
be ALL the non-private messages. You can prevent this by using these
commmands:-

```text
catchup GB7DJK all
catchup GB7DJK 300 301 302 303 500-510
```

and to undo what you have just done:-

```text
uncatchup GB7DJK all
uncatchup GB7DJK 300 301 302 303 500-510
```

which will arrange for them to be forward candidates again.

Order is not important.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/uncatchup.pl){ .md-button }

## Verify on a running node

```text
HELP UNCATCHUP
```

The built-in help is useful when checking the exact command set installed on a particular node.