# `SET/PRIVILEGE`

<div class="command-hero" markdown>

**Set privilege level on a call**

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
SET/PRIVILEGE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `ref->priv()`, `self->msg()`, `user->priv()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/privilege.pl` · SHA-256 `a09e3758ea78d0872b0728d482f31896d5cb18fd3d3e379bc7015965c7299b4b`

```perl
L10: my ($self, $line) = @_;
L11: my @args = split /\s+/, $line;
L13: my $priv = shift @args;
L19: Log('DXCommand', $self->call . " attempted to set privilege $priv for @args");
L27: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/privilege.pl` · SHA-256 `a09e3758ea78d0872b0728d482f31896d5cb18fd3d3e379bc7015965c7299b4b`

```perl
L18: if ($self->priv < 9 || $self->remotecmd || $self->inscript) {
L20: return (1, $self->msg('e5'));
L23: if ($priv < 0 || $priv > 9) {
L24: return (1, $self->msg('e5'));
L29: unless ($self->remotecmd || $self->inscript) {
```

### Output and error evidence

Source: `cmd/set/privilege.pl` · SHA-256 `a09e3758ea78d0872b0728d482f31896d5cb18fd3d3e379bc7015965c7299b4b`

```perl
L20: return (1, $self->msg('e5'));
L24: return (1, $self->msg('e5'));
L40: push @out, $self->msg('priv', $call);
L43: push @out, $self->msg('e3', "Set Privilege", $call);
L46: push @out, $self->msg('sorry');
L50: return (1, @out);
```

### Message keys returned

`e3`, `e5`, `priv`, `sorry`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/PRIVILEGE <n> <call> [<call..]
```

**Set privilege level on a call**

## Details

Set the privilege level on a callsign. The privilege levels that pertain
to commands are as default:-
```text
0 - normal user
1 - allow remote nodes normal user RCMDs
5 - various privileged commands (including shutdown, but not disc-
    connect), the normal level for another node.
8 - more privileged commands (including disconnect)
9 - local sysop privilege. DO NOT SET ANY REMOTE USER OR NODE TO THIS
    LEVEL.
```
If you are a sysop and you come in as a normal user on a remote connection
your privilege will automatically be set to 0.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/privilege.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PRIVILEGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.