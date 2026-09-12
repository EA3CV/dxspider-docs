# `AGWRESTART`

<div class="command-hero" markdown>

**restart an agw connection**

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
AGWRESTART
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/agwrestart.pl` · SHA-256 `2283756a14da8b93f69afa3178b33f4740340e564142bfc622f9c72448ef6ca3`

```perl
L6: my $self = shift;
```

### Validation and access evidence

Source: `cmd/agwrestart.pl` · SHA-256 `2283756a14da8b93f69afa3178b33f4740340e564142bfc622f9c72448ef6ca3`

```perl
L7: return (1, $self->msg('e5')) if $self->priv < 5;
L9: return (1, $self->msg('done'));
```

### Output and error evidence

Source: `cmd/agwrestart.pl` · SHA-256 `2283756a14da8b93f69afa3178b33f4740340e564142bfc622f9c72448ef6ca3`

```perl
L7: return (1, $self->msg('e5')) if $self->priv < 5;
L9: return (1, $self->msg('done'));
```

### Message keys returned

`done`, `e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/agwrestart.pl){ .md-button }

## Verify on a running node

```text
HELP AGWRESTART
```

Compare the installed handler with this page when local overrides or a different revision may be present.