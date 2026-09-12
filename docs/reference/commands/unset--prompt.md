# `UNSET/PROMPT`

<div class="command-hero" markdown>

**Set your prompt back to default**

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
UNSET/PROMPT [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->put()`

### Argument parsing evidence

Source: `cmd/unset/prompt.pl` · SHA-256 `aba3b2ad3c7e4bb7a36619bcf0cdc23d5b070950e3973015b5291b443de029a3`

```perl
L9: my ($self, $line) = @_;
L18: return (1, $self->msg('pru', $line));
```

### Validation and access evidence

Source: `cmd/unset/prompt.pl` · SHA-256 `aba3b2ad3c7e4bb7a36619bcf0cdc23d5b070950e3973015b5291b443de029a3`

```perl
L18: return (1, $self->msg('pru', $line));
L20: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/unset/prompt.pl` · SHA-256 `aba3b2ad3c7e4bb7a36619bcf0cdc23d5b070950e3973015b5291b443de029a3`

```perl
L18: return (1, $self->msg('pru', $line));
L20: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`namee2`, `pru`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/PROMPT
```

**Set your prompt back to default**

## Details

This command will set your user prompt to the string that you
say. The point of this command to enable a user to interface to programs
that are looking for a specific prompt (or else you just want a different
prompt).

```text
SET/PROMPT clx >
```

There are some substitutions that can be added to the prompt:

```text
%C - callsign [which will have ( and ) around it if not here]
%D - date
%T - time
%M - cluster 'mycall'
```

The standard prompt is defined as:

```text
SET/PROMPT %C de %M %D %T dxspider >
```

UNSET/PROMPT will undo the SET/PROMPT command and set your prompt back to
normal.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/prompt.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PROMPT
```

Compare the installed handler with this page when local overrides or a different revision may be present.