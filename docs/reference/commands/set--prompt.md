# `SET/PROMPT`

<div class="command-hero" markdown>

**Set your prompt to <string>**

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
SET/PROMPT [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->prompt()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/prompt.pl` · SHA-256 `7a48d117a0ce682319af1ef3d9e3b8275dd2cee0da2e3bfe4e5a6c293cbe1c2f`

```perl
L9: my ($self, $line) = @_;
L14: $line =~ s/^\s+//;
L15: $line =~ s/\s+$//;
L17: return (1, $self->msg('e9')) if !$line;
L21: $user->prompt($line);
L22: $self->{prompt} = $line; # this is like this because $self->prompt is a function that does something else
L24: return (1, $self->msg('prs', $line));
```

### Validation and access evidence

Source: `cmd/set/prompt.pl` · SHA-256 `7a48d117a0ce682319af1ef3d9e3b8275dd2cee0da2e3bfe4e5a6c293cbe1c2f`

```perl
L17: return (1, $self->msg('e9')) if !$line;
L24: return (1, $self->msg('prs', $line));
L26: return (1, $self->msg('namee2', $call));
```

### Output and error evidence

Source: `cmd/set/prompt.pl` · SHA-256 `7a48d117a0ce682319af1ef3d9e3b8275dd2cee0da2e3bfe4e5a6c293cbe1c2f`

```perl
L17: return (1, $self->msg('e9')) if !$line;
L24: return (1, $self->msg('prs', $line));
L26: return (1, $self->msg('namee2', $call));
```

### Message keys returned

`e9`, `namee2`, `prs`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/PROMPT <string>
```

**Set your prompt to <string>**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/prompt.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PROMPT
```

Compare the installed handler with this page when local overrides or a different revision may be present.