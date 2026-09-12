# `BYE`

<div class="command-hero" markdown>

**Exit from the cluster**

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
BYE
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`self->msg()`, `self->send_file()`

### Argument parsing evidence

Source: `cmd/bye.pl` · SHA-256 `a828dc8fe9f59548d58a5baf33245ec3eed07b88351712d0d99fe67fd30d8cb8`

```perl
L8: my $self = shift;
```

### Validation and access evidence

Source: `cmd/bye.pl` · SHA-256 `a828dc8fe9f59548d58a5baf33245ec3eed07b88351712d0d99fe67fd30d8cb8`

```perl
L9: return (1, $self->msg('e5')) if $self->inscript || $self->remotecmd;
```

### Output and error evidence

Source: `cmd/bye.pl` · SHA-256 `a828dc8fe9f59548d58a5baf33245ec3eed07b88351712d0d99fe67fd30d8cb8`

```perl
L9: return (1, $self->msg('e5')) if $self->inscript || $self->remotecmd;
L20: return (1);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
BYE
```

**Exit from the cluster**

## Details

This will disconnect you from the cluster

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/bye.pl){ .md-button }

## Verify on a running node

```text
HELP BYE
```

Compare the installed handler with this page when local overrides or a different revision may be present.