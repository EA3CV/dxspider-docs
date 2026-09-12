# `DISCONNECT`

<div class="command-hero" markdown>

**Disconnect user(s) or node(s)**

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
DISCONNECT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses cluster synchronization/state code.

### Important calls

`DXChannel::get()`, `DXChannel::get_all_node_calls()`, `DXChannel::get_all_user_calls()`, `DXCluster->get_exact()`, `Msg->conns()`, `dxchan->send_now()`, `dxchan->send_pc39()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/disconnect.pl` · SHA-256 `a924fe570cb871a2fe9d1754e28c9934c685f2aa826b5c25dc62b1bc86485d28`

```perl
L4: my ($self, $line) = @_;
L5: my @calls = split /\s+/, $line;
L13: if ($calls[0] =~ /^user/i ) {
L15: } elsif ($calls[0] =~ /^node/i) {
```

### Validation and access evidence

Source: `cmd/disconnect.pl` · SHA-256 `a924fe570cb871a2fe9d1754e28c9934c685f2aa826b5c25dc62b1bc86485d28`

```perl
L9: if ($self->priv < 5) {
L10: return (1, $self->msg('e5'));
L13: if ($calls[0] =~ /^user/i ) {
L28: return (1, $self->msg('e5')) if $self->priv < 8;
```

### Output and error evidence

Source: `cmd/disconnect.pl` · SHA-256 `a924fe570cb871a2fe9d1754e28c9934c685f2aa826b5c25dc62b1bc86485d28`

```perl
L10: return (1, $self->msg('e5'));
L28: return (1, $self->msg('e5')) if $self->priv < 8;
L29: $dxchan->send_now('D', $self->msg('disc1', $self->call));
L32: push @out, $self->msg('disc2', $call);
L35: push @out, $self->msg('disc3', $call);
L43: push @out, $self->msg('e10', $call);
L47: return (1, @out);
```

### Message keys returned

`disc1`, `disc2`, `disc3`, `disc4`, `e10`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DISCONNECT <call> [<call> ...]
```

**Disconnect user(s) or node(s)**

## Details

Disconnect any <call> connected locally.

In addition you can disconnect all users (except yourself) with

```text
DISC users
```

or all nodes with:

```text
DISC nodes
```

or everything (except yourself) with

```text
DISC all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/disconnect.pl){ .md-button }

## Verify on a running node

```text
HELP DISCONNECT
```

Compare the installed handler with this page when local overrides or a different revision may be present.