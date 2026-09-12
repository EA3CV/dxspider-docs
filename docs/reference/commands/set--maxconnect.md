# `SET/MAXCONNECT`

<div class="command-hero" markdown>

**Set max incoming connections for user/node**

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
SET/MAXCONNECT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->maxconnect()`

### Argument parsing evidence

Source: `cmd/set/maxconnect.pl` · SHA-256 `e3730cef3b6331ebebd7845d11df749c540f2794dce139baf562fa6b0432aa62`

```perl
L8: my ($self, $line) = @_;
L9: my @args = split /\s+/, $line;
L13: my $val = shift @args if @args;
L18: return (1, $self->msg('e12')) unless @args;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/maxconnect.pl` · SHA-256 `e3730cef3b6331ebebd7845d11df749c540f2794dce139baf562fa6b0432aa62`

```perl
L16: return (1, $self->msg('e5')) if $self->priv < 8;
L17: return (1, $self->msg('e14')) unless defined $val;
L18: return (1, $self->msg('e12')) unless @args;
```

### Output and error evidence

Source: `cmd/set/maxconnect.pl` · SHA-256 `e3730cef3b6331ebebd7845d11df749c540f2794dce139baf562fa6b0432aa62`

```perl
L16: return (1, $self->msg('e5')) if $self->priv < 8;
L17: return (1, $self->msg('e14')) unless defined $val;
L18: return (1, $self->msg('e12')) unless @args;
L26: push @out, $self->msg('maxconnect', $call, $val);
L28: push @out, $self->msg('e3', "set/maxconnect", $call);
L31: return (1, @out);
```

### Message keys returned

`e12`, `e14`, `e3`, `e5`, `maxconnect`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/MAXCONNECT <value> [<call> ..]
```

**Set max incoming connections for user/node**

## Details

Set the maximum no of connections (parents) an incoming user or node is
allowed to have. If this incoming connection takes it over the separate
limits for users and nodes (defaults: 3 and 8 respectively), then the
connection is refused (with a polite message).

The idea behind this to limit the number of copies of messages that
are sent to users (and nodes). Nodes really don't need to have more than
5 or 6 partners and users don't need more than two connections into the
cluster cloud.

This check is only for INCOMING connections, no check is performed for
outgoing connections.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/maxconnect.pl){ .md-button }

## Verify on a running node

```text
HELP SET/MAXCONNECT
```

Compare the installed handler with this page when local overrides or a different revision may be present.