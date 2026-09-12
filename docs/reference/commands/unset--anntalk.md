# `UNSET/ANNTALK`

<div class="command-hero" markdown>

**Stop talk like announce messages on your terminal**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/ANNTALK [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Verify on a running node

```text
HELP UNSET/ANNTALK
```

Use the node help to check for local overrides or differences in another installed revision.