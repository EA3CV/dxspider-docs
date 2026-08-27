# `UNSET/REGISTER`

<div class="command-hero" markdown>

**Mark a user as not registered**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/register.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/REGISTER
```

The built-in help is useful when checking the exact command set installed on a particular node.