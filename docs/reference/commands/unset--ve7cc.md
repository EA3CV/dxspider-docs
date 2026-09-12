# `UNSET/VE7CC`

<div class="command-hero" markdown>

**set the ve7cc output flag**

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
UNSET/VE7CC [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->isa()`, `self->msg()`, `self->ve7cc()`

### Argument parsing evidence

Source: `cmd/unset/ve7cc.pl` · SHA-256 `93a605f8d671c9269c6f902c7ab2c6a3b8f720a1f4c1bbf9bb01d02a72562426`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/unset/ve7cc.pl` · SHA-256 `93a605f8d671c9269c6f902c7ab2c6a3b8f720a1f4c1bbf9bb01d02a72562426`

```perl
L14: return (0, $self->msg('e5')) unless $self->isa('DXCommandmode');
```

### Output and error evidence

Source: `cmd/unset/ve7cc.pl` · SHA-256 `93a605f8d671c9269c6f902c7ab2c6a3b8f720a1f4c1bbf9bb01d02a72562426`

```perl
L14: return (0, $self->msg('e5')) unless $self->isa('DXCommandmode');
L16: push @out, $self->msg('ok');
L17: return (1, @out);
```

### Message keys returned

`e5`, `ok`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/ve7cc.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/VE7CC
```

Compare the installed handler with this page when local overrides or a different revision may be present.