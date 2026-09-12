# `UNSET/EMAIL`

<div class="command-hero" markdown>

**Stop personal msgs being forwarded by email**

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
UNSET/EMAIL [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->put()`, `user->wantemail()`

### Argument parsing evidence

Source: `cmd/unset/email.pl` · SHA-256 `33d4f68ec64a6ca107678edbe449e0527b252705fefb969f9b2b383cfbd38684`

```perl
L9: my ($self, $line) = @_;
L17: return (1, $self->msg('emaila', $line));
```

### Validation and access evidence

Source: `cmd/unset/email.pl` · SHA-256 `33d4f68ec64a6ca107678edbe449e0527b252705fefb969f9b2b383cfbd38684`

```perl
L17: return (1, $self->msg('emaila', $line));
L19: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/unset/email.pl` · SHA-256 `33d4f68ec64a6ca107678edbe449e0527b252705fefb969f9b2b383cfbd38684`

```perl
L17: return (1, $self->msg('emaila', $line));
L19: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`emaila`, `namee2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/EMAIL
```

**Stop personal msgs being forwarded by email**

## Details

If any personal messages come in for your callsign then you can use
these commands to control whether they are forwarded onto your email
address. To enable the forwarding do something like:-

```text
SET/EMAIL mike.tubby@somewhere.com
```

You can have more than one email address (each one separated by a space).
Emails are forwarded to all the email addresses you specify.

You can disable forwarding by:-

```text
UNSET/EMAIL
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/email.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/EMAIL
```

Compare the installed handler with this page when local overrides or a different revision may be present.