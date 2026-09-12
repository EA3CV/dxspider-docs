# `SET/ADDRESS`

<div class="command-hero" markdown>

**Record your postal address**

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
SET/ADDRESS [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `user->addr()`

### Argument parsing evidence

Source: `cmd/set/address.pl` · SHA-256 `7a5e6dd1947f3ab3bf6c7e1fd61e758bcc66bfc0050c7b25cf3b4022cea95559`

```perl
L9: my ($self, $line) = @_;
L15: $line =~ s/[{}]//g; # no braces allowed
L16: $user->addr($line);
L17: push @out, $self->msg('addr', $line);
```

### Output and error evidence

Source: `cmd/set/address.pl` · SHA-256 `7a5e6dd1947f3ab3bf6c7e1fd61e758bcc66bfc0050c7b25cf3b4022cea95559`

```perl
L17: push @out, $self->msg('addr', $line);
L19: return (1, @out);
```

### Message keys returned

`addr`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/ADDRESS <your address>
```

**Record your postal address**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/address.pl){ .md-button }

## Verify on a running node

```text
HELP SET/ADDRESS
```

Compare the installed handler with this page when local overrides or a different revision may be present.