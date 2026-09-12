# `SHOW/DUP_EPH`

<div class="command-hero" markdown>

**show a list of all the outstanding announce dups for debugging really**

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
SHOW/DUP_EPH [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXProt::eph_list()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/dup_eph.pl` · SHA-256 `5af4bff40b2580ff202ea59c0263f85c441897f520c6eca0a93003f00f0d7c70`

```perl
L9: my $self = shift;
L10: my $line = shift;
L12: my $regex = $line;
```

### Validation and access evidence

Source: `cmd/show/dup_eph.pl` · SHA-256 `5af4bff40b2580ff202ea59c0263f85c441897f520c6eca0a93003f00f0d7c70`

```perl
L11: return (1, $self->msg('e5')) unless $self->priv >= 9;
```

### Output and error evidence

Source: `cmd/show/dup_eph.pl` · SHA-256 `5af4bff40b2580ff202ea59c0263f85c441897f520c6eca0a93003f00f0d7c70`

```perl
L11: return (1, $self->msg('e5')) unless $self->priv >= 9;
L20: push @out, ztime($list{$_}) . ": $_";
L22: return (1, sort @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/dup_eph.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DUP_EPH
```

Compare the installed handler with this page when local overrides or a different revision may be present.