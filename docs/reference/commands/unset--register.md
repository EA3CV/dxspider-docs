# `UNSET/REGISTER`

<div class="command-hero" markdown>

**Mark a user as not registered**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
UNSET/REGISTER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get_current()`, `dxchan->registered()`, `ref->put()`, `ref->registered()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/register.pl` · SHA-256 `aa1f4ebb3cfce4f588420118ebebe0bd3244eb76225aab8bbfc1ee13c87739cf`

```perl
L8: my ($self, $line) = @_;
L9: my @args = split /\s+/, $line;
L17: Log('DXCommand', $self->call . " attempted to unregister @args");
L22: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/register.pl` · SHA-256 `aa1f4ebb3cfce4f588420118ebebe0bd3244eb76225aab8bbfc1ee13c87739cf`

```perl
L16: if ($self->priv < 9) {
L18: return (1, $self->msg('e5'));
L24: unless ($self->remotecmd || $self->inscript) {
```

### Output and error evidence

Source: `cmd/unset/register.pl` · SHA-256 `aa1f4ebb3cfce4f588420118ebebe0bd3244eb76225aab8bbfc1ee13c87739cf`

```perl
L18: return (1, $self->msg('e5'));
L30: push @out, $self->msg("regun", $call);
L33: push @out, $self->msg('e3', 'unset/register', $call);
L37: push @out, $self->msg('sorry');
L40: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `reginac`, `regun`, `sorry`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/register.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/REGISTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.