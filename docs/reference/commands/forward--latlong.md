# `FORWARD/LATLONG`

<div class="command-hero" markdown>

**Send latitude and longitude information to another cluster**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
FORWARD/LATLONG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXBearing::lltos()`, `DXChannel::get()`, `DXProt::pc41()`, `DXUser::get_current()`, `dbm->seq()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/forward/latlong.pl` · SHA-256 `2b8640b918ee918fb21de87f826ff0233e16f59569a1b8ec683f729a24ad6a73`

```perl
L11: my ($self, $line) = @_;
L19: for ( map {uc $_ } split /\s+/, $line ) {
L32: if ($data =~ m{(?:lat|long) =>}) {
L42: $s =~ s{H\d+\^~$}{H1^~};
```

### Validation and access evidence

Source: `cmd/forward/latlong.pl` · SHA-256 `2b8640b918ee918fb21de87f826ff0233e16f59569a1b8ec683f729a24ad6a73`

```perl
L12: return (1, $self->msg('e5')) unless $self->priv >= 6;
L32: if ($data =~ m{(?:lat|long) =>}) {
L50: return(1, @out, $self->msg('rec', $count));
```

### Output and error evidence

Source: `cmd/forward/latlong.pl` · SHA-256 `2b8640b918ee918fb21de87f826ff0233e16f59569a1b8ec683f729a24ad6a73`

```perl
L12: return (1, $self->msg('e5')) unless $self->priv >= 6;
L13: return (1, "Obsolete command, do not use");
L23: push @out, $self->msg('e10', $_);
L26: return (1, @out) if @out;
L43: $dxchan->send($s);
L50: return(1, @out, $self->msg('rec', $count));
```

### Message keys returned

`e10`, `e5`, `rec`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
FORWARD/LATLONG <node_call>
```

**Send latitude and longitude information to another cluster**

## Details

This command sends all the latitude and longitude information that your
cluster is holding against callsigns.  One advantage of recieving this
information is that more locator information is held by you.  This
means that more locators are given on the DX line assuming you have
SET/DXGRID enabled.  This could be a LOT of information though, so
it is not recommended on slow links.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/forward/latlong.pl){ .md-button }

## Verify on a running node

```text
HELP FORWARD/LATLONG
```

Compare the installed handler with this page when local overrides or a different revision may be present.