# `SHOW/BUDDY`

<div class="command-hero" markdown>

**Show your list of buddies**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/BUDDY
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Output and error evidence

Source: `cmd/show/buddy.pl` · SHA-256 `49d8ae895e448294dbb96814dfdfb9ebf0e282384dac15eee2e9157d367c202f`

```perl
L16: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L22: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L23: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/BUDDY
```

**Show your list of buddies**

## Details

See SET/BUDDY for more information about buddies.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/buddy.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BUDDY
```

Compare the installed handler with this page when local overrides or a different revision may be present.