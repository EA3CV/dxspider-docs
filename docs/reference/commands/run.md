# `RUN`

<div class="command-hero" markdown>

**the run command run a script from the scripts directory**

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
RUN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`script->run()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/run.pl` · SHA-256 `4285c207933eb1af30c9e8b06ddf13460876a2d585526bd33c9b0db700ab4cbf`

```perl
L11: my ($self, $line) = @_;
L12: my @f = split /\s+/, $line;
L16: my $f = shift @f;
L22: $f =~ s|[^-\w/\\]||g;
```

### Validation and access evidence

Source: `cmd/run.pl` · SHA-256 `4285c207933eb1af30c9e8b06ddf13460876a2d585526bd33c9b0db700ab4cbf`

```perl
L18: if (is_callsign(uc $f) && $self->priv < 8 && uc $f ne $self->call) {
```

### Output and error evidence

Source: `cmd/run.pl` · SHA-256 `4285c207933eb1af30c9e8b06ddf13460876a2d585526bd33c9b0db700ab4cbf`

```perl
L19: push @out, $self->msg('e5');
L25: push @out, $self->msg('e3', 'script', $f);
L31: return (1, @out);
```

### Message keys returned

`e3`, `e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/run.pl){ .md-button }

## Verify on a running node

```text
HELP RUN
```

Compare the installed handler with this page when local overrides or a different revision may be present.