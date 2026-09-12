# `SPOOF`

<div class="command-hero" markdown>

**Do a command as though you are another user**

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
SPOOF [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Named fields consumed by the parser

`call`, `newline`

### Important calls

`DXChannel::get()`, `DXUser->new()`, `DXUser::get_current()`, `self->call()`, `self->lang()`, `self->msg()`, `self->run_cmd()`, `self->user()`

### Argument parsing evidence

Source: `cmd/spoof.pl` · SHA-256 `4871dadde893f701023a9c33f0b974fdce7bd9f1f86ec5760bfcd1aaa8669e29`

```perl
L9: my ($self, $line) = @_;
L15: my ($call, $newline) = split /\s+/, $line, 2;
L39: Log('cmd', "$self->{call}|$addr|spoof|$line");
```

### Validation and access evidence

Source: `cmd/spoof.pl` · SHA-256 `4871dadde893f701023a9c33f0b974fdce7bd9f1f86ec5760bfcd1aaa8669e29`

```perl
L16: return (1, $self->msg('nodee1', $call)) if DXChannel::get($call);
L18: if ($self->remotecmd || $self->inscript) {
L20: return (1, $self->msg('e5'));
L22: if ($self->priv < 9) {
L24: return (1, $self->msg('e5'));
```

### Output and error evidence

Source: `cmd/spoof.pl` · SHA-256 `4871dadde893f701023a9c33f0b974fdce7bd9f1f86ec5760bfcd1aaa8669e29`

```perl
L16: return (1, $self->msg('nodee1', $call)) if DXChannel::get($call);
L20: return (1, $self->msg('e5'));
L24: return (1, $self->msg('e5'));
L32: push @out, $self->msg('spf1', $call);
L41: push @out, map {"spoof $call: $_"} @in;
L46: return (1, @out);
```

### Message keys returned

`e5`, `nodee1`, `spf1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SPOOF <call> <command>
```

**Do a command as though you are another user**

## Details

This command is provided so that sysops can set a user's parameters without
me having to write a special 'sysop' version for every user command. It
allows you to pretend that you are doing the command as the user you specify.

eg:-

```text
 SPOOF G1TLH set/name Dirk
 SPOOF G1TLH set/qra JO02LQ
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/spoof.pl){ .md-button }

## Verify on a running node

```text
HELP SPOOF
```

Compare the installed handler with this page when local overrides or a different revision may be present.