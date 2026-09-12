# `SHOW/CONNECT`

<div class="command-hero" markdown>

**Show all the active connections**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/CONNECT
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/connect.pl` · SHA-256 `bbeb6e676c7993600a2c36f17871ad4dfd479525f4abeea194e75d82efa0dd64`

```perl
L9: my $self = shift;
L21: if ($c =~ /^Server\s+(\S+)/) {
```

### Validation and access evidence

Source: `cmd/show/connect.pl` · SHA-256 `bbeb6e676c7993600a2c36f17871ad4dfd479525f4abeea194e75d82efa0dd64`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 1;
L21: if ($c =~ /^Server\s+(\S+)/) {
```

### Output and error evidence

Source: `cmd/show/connect.pl` · SHA-256 `bbeb6e676c7993600a2c36f17871ad4dfd479525f4abeea194e75d82efa0dd64`

```perl
L10: return (1, $self->msg('e5')) if $self->priv < 1;
L14: push @out, "Cnum Call Address/Port State Type Dir. Module";
L33: push @out, sprintf(" %3d %-9s %-27.27s %3s %7s %8s %-8s",
L40: push @out, "$count Connections ($Msg::noconns Allocated)";
L41: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/CONNECT
```

**Show all the active connections**

## Details

This command shows information on all the active connections known to
the node. This command gives slightly more information than WHO.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/connect.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CONNECT
```

Compare the installed handler with this page when local overrides or a different revision may be present.