# `SET/PASSWORD`

<div class="command-hero" markdown>

**Change your own password interactively, or—at SYSOP privilege—set another user's password.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Identity & Security</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SET/PASSWORD [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `ref->passwd()`, `ref->put()`, `self->msg()`, `self->state()`

### Argument parsing evidence

Source: `cmd/set/password.pl` · SHA-256 `2af109b7dfdce518652d3ed6f07adeeeefb6e5baea4abd56b1f18b72061936ce`

```perl
L10: my ($self, $line) = @_;
L11: my @args = split /\s+/, $line, 2;
L12: my $call = shift @args;
L28: return (1, $self->msg('e29')) unless @args;
```

### Validation and access evidence

Source: `cmd/set/password.pl` · SHA-256 `2af109b7dfdce518652d3ed6f07adeeeefb6e5baea4abd56b1f18b72061936ce`

```perl
L17: if ($self->remotecmd || $self->inscript) {
L20: return (1, $self->msg('e5'));
L24: if ($self->priv < 9) {
L26: return (1, $self->msg('e5'));
L28: return (1, $self->msg('e29')) unless @args;
```

### Output and error evidence

Source: `cmd/set/password.pl` · SHA-256 `2af109b7dfdce518652d3ed6f07adeeeefb6e5baea4abd56b1f18b72061936ce`

```perl
L20: return (1, $self->msg('e5'));
L26: return (1, $self->msg('e5'));
L28: return (1, $self->msg('e29')) unless @args;
L32: push @out, $self->msg("password", $call);
L35: push @out, $self->msg('e3', 'User record for', $call);
L41: push @out, $self->msg('pw0');
L44: push @out, $self->msg('e5');
L48: return (1, @out);
```

### Message keys returned

`e29`, `e3`, `e5`, `password`, `pw0`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SET/PASSWORD <callsign> <string>
    ```

    **Set a users password**

    The password for a user can only be set by a full sysop. The string
    can contain any characters.

    The way this field is used depends on context. If it is being used in
    the SYSOP command context then you are offered 5 random numbers and you
    have to supply the corresponding letters. This is now mainly for ax25
    connections.

    If it is being used on incoming telnet connections then, if a password
    is set or the:

    ```text
    set/var $main::passwdreq = 1
    ```

    command is executed in the startup script, then a password prompt is
    given after the normal 'login: ' prompt.

=== "Help variant"

    ```text
    SET/PASSWORD
    ```

    **Set your own password**

    This command only works for a 'telnet' user (currently). It will
    only work if you have a password already set. This initial password
    can only be set by the sysop.

    When you execute this command it will ask you for your old password,
    then ask you to type in your new password twice (to make sure you
    get it right). You may or may not see the data echoed on the screen
    as you type, depending on the type of telnet client you have.

## Practical examples

### User form

```text
SET/PASSWORD
```

### SYSOP form

```text
SET/PASSWORD G1ABC new-password
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/password.pl){ .md-button }

## Related commands

- [`UNSET/PASSWORD`](unset--password.md)
- [`SYSOP`](sysop.md)

## Verify on a running node

```text
HELP SET/PASSWORD
```

Compare the installed handler with this page when local overrides or a different revision may be present.