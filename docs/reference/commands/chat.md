# `CHAT`

<div class="command-hero" markdown>

**Chat or Conference to a group**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
CHAT [token ...]
```

### Who can use it

- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command description

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

## Verify on a running node

```text
HELP CHAT
```

Use the node help to check for local overrides or differences in another installed revision.