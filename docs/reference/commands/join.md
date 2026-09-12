# `JOIN`

<div class="command-hero" markdown>

**Join a chat or conference group**

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
JOIN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `user->group()`

### Argument parsing evidence

Source: `cmd/join.pl` · SHA-256 `856e2ecfea068ecc184edb77f8ff0e035b55a32b16e630c21646286aee38a8c1`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach $group (@args) {
```

### Output and error evidence

Source: `cmd/join.pl` · SHA-256 `856e2ecfea068ecc184edb77f8ff0e035b55a32b16e630c21646286aee38a8c1`

```perl
L18: push @out, $self->msg('join', $group);
L24: return (1, @out);
```

### Message keys returned

`join`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
JOIN <group>
```

**Join a chat or conference group**

## Details

JOIN allows you to join a network wide conference group. To join a
group (called FOC in this case) type:-

```text
JOIN FOC
```

See also CHAT, LEAVE, SHOW/CHAT

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/join.pl){ .md-button }

## Verify on a running node

```text
HELP JOIN
```

Compare the installed handler with this page when local overrides or a different revision may be present.