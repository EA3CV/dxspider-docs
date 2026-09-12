# `INIT`

<div class="command-hero" markdown>

**Re-initialise a link to an AK1A compatible node**

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
INIT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXChannel::get()`, `DXProt::pc18()`, `Route::Node::get()`, `dxchan->route_pc21()`, `dxchan->send()`, `dxchan->state()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/init.pl` · SHA-256 `c506a237f93580f09d247349cd966d5184d3b322a23d364dc5f22bcfe3dbe531`

```perl
L8: my ($self, $line) = @_;
L9: my @calls = split /\s+/, $line;
```

### Validation and access evidence

Source: `cmd/init.pl` · SHA-256 `c506a237f93580f09d247349cd966d5184d3b322a23d364dc5f22bcfe3dbe531`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
```

### Output and error evidence

Source: `cmd/init.pl` · SHA-256 `c506a237f93580f09d247349cd966d5184d3b322a23d364dc5f22bcfe3dbe531`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L25: $dxchan->send(DXProt::pc18());
L27: push @out, $self->msg('init1', $call);
L30: push @out, $self->msg('e10', $call);
L34: return (1, @out);
```

### Message keys returned

`e10`, `e5`, `init1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
INIT <node>
```

**Re-initialise a link to an AK1A compatible node**

## Details

This command attempts to re-initialise a link to a (usually) AK1A node
that has got confused, usually by a protocol loop of some kind. It may
work - but you usually will be better off simply disconnecting it (or
better, if it is a real AK1A node, doing an RCMD <node> DISC/F <your
node>).

Best of luck - you will need it.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/init.pl){ .md-button }

## Verify on a running node

```text
HELP INIT
```

Compare the installed handler with this page when local overrides or a different revision may be present.