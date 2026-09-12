# `SET/SEEMEE`

<div class="command-hero" markdown>

**set the RBN seeme flag**

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
SET/SEEMEE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`RBN::add_seeme()`, `self->isa()`, `self->msg()`, `self->rbnseeme()`, `user->rbnseeme()`

### Argument parsing evidence

Source: `cmd/set/seemee.pl` · SHA-256 `22f3bad6e9e9e6b5238d50609715e9f2c517420f0c1d84e490aab31a18f90788`

```perl
L9: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/set/seemee.pl` · SHA-256 `22f3bad6e9e9e6b5238d50609715e9f2c517420f0c1d84e490aab31a18f90788`

```perl
L12: return (0, $self->msg('e5')) unless $self->isa('DXCommandmode');
```

### Output and error evidence

Source: `cmd/set/seemee.pl` · SHA-256 `22f3bad6e9e9e6b5238d50609715e9f2c517420f0c1d84e490aab31a18f90788`

```perl
L12: return (0, $self->msg('e5')) unless $self->isa('DXCommandmode');
L19: push @out, $self->msg('ok');
L20: return (1, @out);
```

### Message keys returned

`e5`, `ok`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/seemee.pl){ .md-button }

## Verify on a running node

```text
HELP SET/SEEMEE
```

Compare the installed handler with this page when local overrides or a different revision may be present.