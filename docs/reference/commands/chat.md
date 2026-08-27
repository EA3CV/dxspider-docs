# `CHAT`

<div class="command-hero" markdown>

**Chat or Conference to a group**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
CHAT <group> <text>
```

**Chat or Conference to a group**

## Details

It is now possible to JOIN a group and have network wide conferencing to that
group. DXSpider does not (and probably will not) implement the AK1A
conference mode as this seems very limiting, is hardly used and doesn't seem
to work too well anyway.

This system uses the existing ANN system and is compatible with both other
DXSpider nodes and AK1A clusters (they use ANN/<group>).

You can be a member of as many "groups" as you want. To join a group type:-

```text
JOIN FOC    (where FOC is the group name)
```

To leave a group type:-

```text
LEAVE FOC
```

You can see which groups you are in by typing:-

```text
STAT/USER
```

and you can see whether your mate is in the group, if he connects to the
same node as you, by typing:-

```text
STAT/USER g1tlh
```

To send a message to a group type:-

```text
CHAT FOC hello everyone
```

or

```text
CH #9000 hello I am back
```

See also JOIN, LEAVE, SHOW/CHAT

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/chat.pl){ .md-button }

## Verify on a running node

```text
HELP CHAT
```

The built-in help is useful when checking the exact command set installed on a particular node.