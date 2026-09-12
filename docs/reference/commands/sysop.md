# `SYSOP`

<div class="command-hero" markdown>

**Regain your privileges if you login remotely**

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
SYSOP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `self->passwd()`, `self->state()`

### Argument parsing evidence

Source: `cmd/sysop.pl` · SHA-256 `0ef08ef22d92eaf14fa816509a7994a736886631204ed60b832d77838a58133d`

```perl
L8: my ($self, $line) = @_;
L15: my @list;
L18: push @list, int rand($lth);
L21: $self->passwd(\@list);
L23: push @out, join(' ', @list);
```

### Output and error evidence

Source: `cmd/sysop.pl` · SHA-256 `0ef08ef22d92eaf14fa816509a7994a736886631204ed60b832d77838a58133d`

```perl
L23: push @out, join(' ', @list);
L24: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SYSOP
```

**Regain your privileges if you login remotely**

## Details

The system automatically reduces your privilege level to that of a
normal user if you login in remotely. This command allows you to
regain your normal privilege level. It uses the normal system: five
numbers are returned that are indexes into the character array that is
your assigned password (see SET/PASSWORD). The indexes start from
zero.

You are expected to return a string which contains the characters
required in the correct order. You may intersperse those characters
with others to obscure your reply for any watchers. For example (and
these values are for explanation :-):

```text
password = 012345678901234567890123456789
> sysop
22 10 15 17 3
```
you type:-
 aa2bbbb0ccc5ddd7xxx3n
 or 2 0 5 7 3
 or 20573

They will all match. If there is no password you will still be offered
numbers but nothing will happen when you input a string. Any match is
case sensitive.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/sysop.pl){ .md-button }

## Verify on a running node

```text
HELP SYSOP
```

Compare the installed handler with this page when local overrides or a different revision may be present.