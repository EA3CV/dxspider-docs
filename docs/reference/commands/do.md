# `DO`

<div class="command-hero" markdown>

**do anything Rape me!**

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
DO [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/do.pl` · SHA-256 `f8620ee13c33389d8d7a69f79b9bbb1721955863917e812ad67947a21d1ea12a`

```perl
L11: my ($self, $line) = @_;
L13: Log('DXCommand', $self->call . " do $line" );
L14: eval "$line";
L15: return (1, $@ ? $@ : "Ok, done $line" );
```

### Validation and access evidence

Source: `cmd/do.pl` · SHA-256 `f8620ee13c33389d8d7a69f79b9bbb1721955863917e812ad67947a21d1ea12a`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
```

### Output and error evidence

Source: `cmd/do.pl` · SHA-256 `f8620ee13c33389d8d7a69f79b9bbb1721955863917e812ad67947a21d1ea12a`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd || $self->inscript;
L15: return (1, $@ ? $@ : "Ok, done $line" );
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/do.pl){ .md-button }

## Verify on a running node

```text
HELP DO
```

Compare the installed handler with this page when local overrides or a different revision may be present.