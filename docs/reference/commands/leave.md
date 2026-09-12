# `LEAVE`

<div class="command-hero" markdown>

**Leave a chat or conference group**

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
LEAVE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `user->group()`

### Argument parsing evidence

Source: `cmd/leave.pl` · SHA-256 `acf4bb3dd5e3f66a279d2656fbd6583126a28692256af98f4c0174a39f0c8c6b`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach $group (@args) {
```

### Output and error evidence

Source: `cmd/leave.pl` · SHA-256 `acf4bb3dd5e3f66a279d2656fbd6583126a28692256af98f4c0174a39f0c8c6b`

```perl
L18: push @out, $self->msg('leave', $group);
L24: return (1, @out);
```

### Message keys returned

`leave`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LEAVE <group>
```

**Leave a chat or conference group**

## Details

LEAVE allows you to leave a network wide conference group. To leave a
group (called FOC in this case) type:-

```text
LEAVE FOC
```

See also CHAT, JOIN, SHOW/CHAT

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/leave.pl){ .md-button }

## Verify on a running node

```text
HELP LEAVE
```

Compare the installed handler with this page when local overrides or a different revision may be present.