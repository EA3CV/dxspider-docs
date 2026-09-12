# `SHOW/MSG_STATUS`

<div class="command-hero" markdown>

**show msgs system status**

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
SHOW/MSG_STATUS [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/msg_status.pl` · SHA-256 `5a5009b2ff09eb9e08895116a5199217d1ab0bd3036f0539dc8631223e2a4fd1`

```perl
L8: my ($self, $line) = @_;
L13: if (!$line || $line =~ /^b/i) {
L21: if (!$line || $line =~ /^w/i) {
```

### Validation and access evidence

Source: `cmd/show/msg_status.pl` · SHA-256 `5a5009b2ff09eb9e08895116a5199217d1ab0bd3036f0539dc8631223e2a4fd1`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 5;
L13: if (!$line || $line =~ /^b/i) {
L21: if (!$line || $line =~ /^w/i) {
```

### Output and error evidence

Source: `cmd/show/msg_status.pl` · SHA-256 `5a5009b2ff09eb9e08895116a5199217d1ab0bd3036f0539dc8631223e2a4fd1`

```perl
L9: return (0, $self->msg('e5')) if $self->priv < 5;
L14: push @out, "Busy Queue";
L15: push @out, "----------";
L18: push @out, "$_ : $r->{msgno}, $r->{from} -> $r->{to}, $r->{subject}\n";
L22: push @out, "Work Queue";
L23: push @out, "----------";
L27: push @out, "$_ : msgno $r->{msgno}, total lines $n, count $r->{count}\n";
L28: push @out, "$_ : stream $r->{stream}, tonode $r->{tonode}, fromnode $r->{fromnode}\n";
L32: return (0, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/msg_status.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/MSG_STATUS
```

Compare the installed handler with this page when local overrides or a different revision may be present.