# `RINIT`

<div class="command-hero" markdown>

**reverse init a cluster connection**

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
RINIT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXChannel::get()`, `DXProt::pc20()`, `Route::Node::get()`, `dxchan->send()`, `dxchan->state()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/rinit.pl` · SHA-256 `70d15dc113ea4bc32d737c4ba50e03ef4153935fbf3ddb8f9783278c8e14723a`

```perl
L8: my ($self, $line) = @_;
L9: my @calls = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/rinit.pl` · SHA-256 `70d15dc113ea4bc32d737c4ba50e03ef4153935fbf3ddb8f9783278c8e14723a`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
```

### Output and error evidence

Source: `cmd/rinit.pl` · SHA-256 `70d15dc113ea4bc32d737c4ba50e03ef4153935fbf3ddb8f9783278c8e14723a`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L24: $dxchan->send(DXProt::pc20());
L25: push @out, $self->msg('init1', $call);
L28: push @out, $self->msg('e10', $call);
L32: return (1, @out);
```

### Message keys returned

`e10`, `e5`, `init1`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/rinit.pl){ .md-button }

## Verify on a running node

```text
HELP RINIT
```

Compare the installed handler with this page when local overrides or a different revision may be present.