# `SHOW/VAR`

<div class="command-hero" markdown>

**show any variable Rape me! print "\$f = $f\n";**

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
SHOW/VAR [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/show/var.pl` · SHA-256 `520874879b738528e24c00d4554ba763b38e56cf1a2b1a5cba3e4fce3527e216`

```perl
L11: my ($self, $line) = @_;
L13: return (1, $self->msg('e9')) unless $line;
L14: my @f = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/show/var.pl` · SHA-256 `520874879b738528e24c00d4554ba763b38e56cf1a2b1a5cba3e4fce3527e216`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
L13: return (1, $self->msg('e9')) unless $line;
```

### Output and error evidence

Source: `cmd/show/var.pl` · SHA-256 `520874879b738528e24c00d4554ba763b38e56cf1a2b1a5cba3e4fce3527e216`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
L13: return (1, $self->msg('e9')) unless $line;
L23: push @out, "$f = ". dd(\@in);
L26: push @out, $@ ? $@ : $self->msg('e3', 'show/var', $f);
L31: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `e9`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/var.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/VAR
```

Compare the installed handler with this page when local overrides or a different revision may be present.