# `SET/OBSCOUNT`

<div class="command-hero" markdown>

**Set the 'pump-up' obscelence PING counter**

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
SET/OBSCOUNT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get_current()`, `dxchan->nopings()`, `self->msg()`, `user->nopings()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/obscount.pl` · SHA-256 `d47fd6efd260b36c5bd997052dfbcbfe3386beaa5d9398ddb3441fc55572c1b6`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: my $val = shift @args if @args;
L18: return (1, $self->msg('e25', 1, 9)) unless defined $val && $val =~ /^\d+$/ && $val >= 1 && $val <= 9;
L19: return (1, $self->msg('e12')) unless @args;
L21: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/obscount.pl` · SHA-256 `d47fd6efd260b36c5bd997052dfbcbfe3386beaa5d9398ddb3441fc55572c1b6`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 8;
L18: return (1, $self->msg('e25', 1, 9)) unless defined $val && $val =~ /^\d+$/ && $val >= 1 && $val <= 9;
L19: return (1, $self->msg('e12')) unless @args;
```

### Output and error evidence

Source: `cmd/set/obscount.pl` · SHA-256 `d47fd6efd260b36c5bd997052dfbcbfe3386beaa5d9398ddb3441fc55572c1b6`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 8;
L18: return (1, $self->msg('e25', 1, 9)) unless defined $val && $val =~ /^\d+$/ && $val >= 1 && $val <= 9;
L19: return (1, $self->msg('e12')) unless @args;
L28: push @out, $self->msg('e13', $call);
L37: push @out, $self->msg('obscount', $call, $val);
L39: push @out, $self->msg('e3', "set/obscount", $call);
L42: return (1, @out);
```

### Message keys returned

`e12`, `e13`, `e25`, `e3`, `e5`, `obscount`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/OBSCOUNT <count> <call>
```

**Set the 'pump-up' obscelence PING counter**

## Details

From 1.35 onwards neighbouring nodes are pinged at regular intervals (see
SET/PINGINTERVAL), usually 300 seconds or 5 minutes. There is a 'pump-up'
counter which is decremented on every outgoing ping and then reset to
the 'obscount' value on every incoming ping. The default value of this
parameter is 2.

What this means is that a neighbouring node will be pinged twice at
(default) 300 second intervals and if no reply has been heard just before
what would be the third attempt, that node is disconnected.

If a ping is heard then the obscount is reset to the full value. Using
default values, if a node has not responded to a ping within 15 minutes,
it is disconnected.

You can set this parameter between 1 and 9.

It is STRONGLY recommended that you don't change the default.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/obscount.pl){ .md-button }

## Verify on a running node

```text
HELP SET/OBSCOUNT
```

Compare the installed handler with this page when local overrides or a different revision may be present.