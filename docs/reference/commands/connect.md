# `CONNECT`

<div class="command-hero" markdown>

**Start a connection to another DX Cluster**

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
CONNECT
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `ExtMsg::start_connect()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/connect.pl` · SHA-256 `2b38e6067c8ae57846bb307a7101aed95a05b06e507bb560e87fe3c968587573`

```perl
L4: my $self = shift;
L5: my $call = uc shift;
```

### Validation and access evidence

Source: `cmd/connect.pl` · SHA-256 `2b38e6067c8ae57846bb307a7101aed95a05b06e507bb560e87fe3c968587573`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 5;
L9: return (1, $self->msg('e6')) unless $call gt ' ';
L10: return (1, $self->msg('already', $call)) if DXChannel::get($call);
L11: return (1, $self->msg('outconn', $call)) if grep {$_->{call} eq $call} @main::outstanding_connects;
L12: return (1, $self->msg('conscript', $lccall)) unless -e "$main::root/connect/$lccall";
L15: return (1, $self->msg('lockout', $call)) if $user && $user->lockout;
```

### Output and error evidence

Source: `cmd/connect.pl` · SHA-256 `2b38e6067c8ae57846bb307a7101aed95a05b06e507bb560e87fe3c968587573`

```perl
L8: return (1, $self->msg('e5')) if $self->priv < 5;
L9: return (1, $self->msg('e6')) unless $call gt ' ';
L10: return (1, $self->msg('already', $call)) if DXChannel::get($call);
L11: return (1, $self->msg('outconn', $call)) if grep {$_->{call} eq $call} @main::outstanding_connects;
L12: return (1, $self->msg('conscript', $lccall)) unless -e "$main::root/connect/$lccall";
L15: return (1, $self->msg('lockout', $call)) if $user && $user->lockout;
L18: push @out, $self->msg('constart', $call);
L20: return (1, @out);
```

### Message keys returned

`already`, `conscript`, `constart`, `e5`, `e6`, `lockout`, `outconn`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
CONNECT <callsign>
```

**Start a connection to another DX Cluster**

## Details

Start a connection process that will culminate in a new connection to the
DX cluster <callsign>. This process creates a new 'client' process which will
use the script in /spider/connect/<callsign> to effect the 'chat' exchange
necessary to traverse the network(s) to logon to the cluster <callsign>.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/connect.pl){ .md-button }

## Verify on a running node

```text
HELP CONNECT
```

Compare the installed handler with this page when local overrides or a different revision may be present.