# `SET/HOMEBBS`

<div class="command-hero" markdown>

**set the home mail bbs of the user remove leading and trailing spaces**

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
SET/HOMEBBS [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->bbs()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/homebbs.pl` · SHA-256 `18db50f895e15195099374fe188915e042d810eb68c4c03e2b33f4a21e435a51`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L17: return (1, $self->msg('bbse1')) if !$line;
L21: $line = uc $line;
L22: $user->bbs($line);
L24: return (1, $self->msg('bbs', $line));
```

### Validation and access evidence

Source: `cmd/set/homebbs.pl` · SHA-256 `18db50f895e15195099374fe188915e042d810eb68c4c03e2b33f4a21e435a51`

```perl
L17: return (1, $self->msg('bbse1')) if !$line;
L24: return (1, $self->msg('bbs', $line));
L26: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/homebbs.pl` · SHA-256 `18db50f895e15195099374fe188915e042d810eb68c4c03e2b33f4a21e435a51`

```perl
L17: return (1, $self->msg('bbse1')) if !$line;
L24: return (1, $self->msg('bbs', $line));
L26: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`bbs`, `bbse1`, `namee2`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/homebbs.pl){ .md-button }

## Verify on a running node

```text
HELP SET/HOMEBBS
```

Compare the installed handler with this page when local overrides or a different revision may be present.