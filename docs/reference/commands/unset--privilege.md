# `UNSET/PRIVILEGE`

<div class="command-hero" markdown>

**Remove any privilege for this session**

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
UNSET/PRIVILEGE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `self->priv()`

### Argument parsing evidence

Source: `cmd/unset/privilege.pl` · SHA-256 `0de666ca70074912246d7e6a8a9de3369b3e9a46d974dfa14a0bcb7901cd8cff`

```perl
L8: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/unset/privilege.pl` · SHA-256 `0de666ca70074912246d7e6a8a9de3369b3e9a46d974dfa14a0bcb7901cd8cff`

```perl
L10: return (1, $self->msg('done'));
```

### Output and error evidence

Source: `cmd/unset/privilege.pl` · SHA-256 `0de666ca70074912246d7e6a8a9de3369b3e9a46d974dfa14a0bcb7901cd8cff`

```perl
L10: return (1, $self->msg('done'));
```

### Message keys returned

`done`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/PRIVILEGE
```

**Remove any privilege for this session**

## Details

You can use this command to 'protect' this session from unauthorised
use. If you want to get your normal privilege back you will need to
either logout and login again (if you are on a console) or use the
SYSOP command.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/privilege.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PRIVILEGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.