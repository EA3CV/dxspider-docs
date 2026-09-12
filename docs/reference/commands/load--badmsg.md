# `LOAD/BADMSG`

<div class="command-hero" markdown>

**Reload the bad msg table**

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
LOAD/BADMSG
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::load_badmsg()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/badmsg.pl` · SHA-256 `93a45e2cf24cd6c969fb19779f417718f288e6c8215b92bc119344771b7d8782`

```perl
L2: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/badmsg.pl` · SHA-256 `93a45e2cf24cd6c969fb19779f417718f288e6c8215b92bc119344771b7d8782`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/badmsg.pl` · SHA-256 `93a45e2cf24cd6c969fb19779f417718f288e6c8215b92bc119344771b7d8782`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
L5: push @out, (DXMsg::load_badmsg());
L6: @out = ($self->msg('ok')) unless @out;
L7: return (1, @out);
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/BADMSG
```

**Reload the bad msg table**

## Details

Reload the /spider/msg/badmsg.pl file if you have changed it manually whilst
the cluster is running. This table contains a number of perl regular
expressions which are searched for in the fields targetted of each message.
If any of them match then that message is immediately deleted on receipt.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/badmsg.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BADMSG
```

Compare the installed handler with this page when local overrides or a different revision may be present.