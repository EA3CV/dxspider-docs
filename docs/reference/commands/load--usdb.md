# `LOAD/USDB`

<div class="command-hero" markdown>

**reload the usdb file Be warned, if this is the full database the size of your image will increase by at least 20Mb and all activity will stop for several**

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
LOAD/USDB [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`USDB::init()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/usdb.pl` · SHA-256 `2e89eb26cc05f3f06b9066343d646eba3ee7c8475bb302ab09cd160f7ec766b0`

```perl
L15: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/load/usdb.pl` · SHA-256 `2e89eb26cc05f3f06b9066343d646eba3ee7c8475bb302ab09cd160f7ec766b0`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/usdb.pl` · SHA-256 `2e89eb26cc05f3f06b9066343d646eba3ee7c8475bb302ab09cd160f7ec766b0`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9;
L18: return (1, USDB::init());
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/usdb.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/USDB
```

Compare the installed handler with this page when local overrides or a different revision may be present.