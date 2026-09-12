# `SET/EMAIL`

<div class="command-hero" markdown>

**Set email address(es) and forward your personals**

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
SET/EMAIL [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->email()`, `user->put()`, `user->wantemail()`

### Argument parsing evidence

Source: `cmd/set/email.pl` · SHA-256 `5ce24f121438c8fd04189da2da237c4602394ba6297a0109ed29101713345685`

```perl
L9: my ($self, $line) = @_;
L13: $line =~ s/[<>()\[\]{}]//g; # remove any braces
L14: my @f = split /\s+/, $line;
L16: return (1, $self->msg('emaile1')) if !$line;
L23: return (1, $self->msg('emaila', $line));
```

### Validation and access evidence

Source: `cmd/set/email.pl` · SHA-256 `5ce24f121438c8fd04189da2da237c4602394ba6297a0109ed29101713345685`

```perl
L16: return (1, $self->msg('emaile1')) if !$line;
L23: return (1, $self->msg('emaila', $line));
L25: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/email.pl` · SHA-256 `5ce24f121438c8fd04189da2da237c4602394ba6297a0109ed29101713345685`

```perl
L16: return (1, $self->msg('emaile1')) if !$line;
L23: return (1, $self->msg('emaila', $line));
L25: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`emaila`, `emaile1`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/EMAIL <email> ...
```

**Set email address(es) and forward your personals**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/email.pl){ .md-button }

## Verify on a running node

```text
HELP SET/EMAIL
```

Compare the installed handler with this page when local overrides or a different revision may be present.