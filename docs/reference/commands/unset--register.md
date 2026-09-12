# `UNSET/REGISTER`

<div class="command-hero" markdown>

**Mark a user as not registered**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/REGISTER [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.

## Command description

```text
UNSET/REGISTER <call> ...
```

**Mark a user as not registered**

## Details

Registration is a concept that you can switch on by executing the

```text
set/var $main::reqreg = 1
```

command (usually in your startup file)

If a user is NOT registered then, firstly, instead of the normal
motd file (/spider/data/motd) being sent to the user at startup, the
user is sent the motd_nor file instead. Secondly, the non registered
user only has READ-ONLY access to the node. The non-registered user
cannot use DX, ANN etc.

The only exception to this is that a non-registered user can TALK or
SEND messages to the sysop.

## Verify on a running node

```text
HELP UNSET/REGISTER
```

Use the node help to check for local overrides or differences in another installed revision.