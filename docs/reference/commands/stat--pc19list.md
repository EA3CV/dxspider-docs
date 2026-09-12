# `STAT/PC19LIST`

<div class="command-hero" markdown>

**list out the PC19s that are outstanding (for which PC16s have not been seen)**

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
STAT/PC19LIST
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/stat/pc19list.pl` · SHA-256 `82a90b062e02ea2e95f6c8d29fcad0dee943918e28643135a002676748c5f111`

```perl
L9: my $self = shift;
L12: my @patt = map {"^\Q$_"} split /\s+/, uc shift;
L16: if (!@patt || grep $k =~ /$_/, @patt) {
```

### Validation and access evidence

Source: `cmd/stat/pc19list.pl` · SHA-256 `82a90b062e02ea2e95f6c8d29fcad0dee943918e28643135a002676748c5f111`

```perl
L10: return (1, $self->msg('e5')) unless $self->priv >= 9;
L16: if (!@patt || grep $k =~ /$_/, @patt) {
```

### Output and error evidence

Source: `cmd/stat/pc19list.pl` · SHA-256 `82a90b062e02ea2e95f6c8d29fcad0dee943918e28643135a002676748c5f111`

```perl
L10: return (1, $self->msg('e5')) unless $self->priv >= 9;
L18: push @out, "$k: " . join (', ', map {"via $_->[0]($_->[1] $_->[2])"} @$nl);
L22: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/pc19list.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/PC19LIST
```

Compare the installed handler with this page when local overrides or a different revision may be present.