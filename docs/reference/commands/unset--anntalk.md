# `UNSET/ANNTALK`

<div class="command-hero" markdown>

**Stop talk like announce messages on your terminal**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/ANNTALK
```

**Stop talk like announce messages on your terminal**

## Details

The announce system on legacy cluster nodes is used as a talk
substitute because the network is so poorly connected. If you:

```text
unset/anntalk
```

you will suppress several of these announces, you may miss the odd
useful one as well, but you would probably miss them anyway in the
welter of useless ones.

```text
set/anntalk
```

allows you to see them again. This is the default.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/anntalk.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/ANNTALK
```

The built-in help is useful when checking the exact command set installed on a particular node.