# `UNSET/BELIEVE`

<div class="command-hero" markdown>

**Add a believable node - used to filter nodes as being believable**

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
UNSET/BELIEVE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->unset_believe()`

### Argument parsing evidence

Source: `cmd/unset/believe.pl` · SHA-256 `6cd92082639586bb25cdce4c08336a5bcf3e608d7b72aa7f40186e1a7789505d`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L12: my $node = shift @args;
L21: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/believe.pl` · SHA-256 `6cd92082639586bb25cdce4c08336a5bcf3e608d7b72aa7f40186e1a7789505d`

```perl
L16: return (1, $self->msg('e5')) if $self->priv < 6;
L17: return (1, $self->msg('e22', $node)) unless is_callsign($node);
L19: return (1, $self->msg('e13', $node)) unless $user->is_node;
L22: return (1, $self->msg('e22', $node)) unless is_callsign($call);
```

### Output and error evidence

Source: `cmd/unset/believe.pl` · SHA-256 `6cd92082639586bb25cdce4c08336a5bcf3e608d7b72aa7f40186e1a7789505d`

```perl
L16: return (1, $self->msg('e5')) if $self->priv < 6;
L17: return (1, $self->msg('e22', $node)) unless is_callsign($node);
L19: return (1, $self->msg('e13', $node)) unless $user->is_node;
L22: return (1, $self->msg('e22', $node)) unless is_callsign($call);
L30: push @out, $self->msg('believeu', $call, $node);
L34: return (1, @out);
```

### Message keys returned

`believeu`, `e13`, `e22`, `e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/believe.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BELIEVE
```

Compare the installed handler with this page when local overrides or a different revision may be present.