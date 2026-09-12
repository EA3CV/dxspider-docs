# `UNSET/BADWORD`

<div class="command-hero" markdown>

**Propagate things like this word again**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/BADWORD [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command description

```text
UNSET/BADWORD <word>..
```

**Propagate things like this word again**

## Details

This is the opposite of set/badword <word>

```text
unset/badword fred
```

will allow text with this word again (if it has been set as a bad word.

## Verify on a running node

```text
HELP UNSET/BADWORD
```

Use the node help to check for local overrides or differences in another installed revision.