# `SET/PASSWORD`

<div class="command-hero" markdown>

**Change your own password interactively, or—at SYSOP privilege—set another user's password.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Identity & Security</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/PASSWORD [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command forms and examples

=== "Available form"

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

=== "Available form"

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

## Related commands

- [`UNSET/PASSWORD`](unset--password.md)
- [`SYSOP`](sysop.md)

## Verify on a running node

```text
HELP SET/PASSWORD
```

Use the node help to check for local overrides or differences in another installed revision.