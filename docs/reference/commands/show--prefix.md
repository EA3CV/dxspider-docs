# `SHOW/PREFIX`

<div class="command-hero" markdown>

**Interrogate the prefix database**

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
SHOW/PREFIX [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Prefix::extract()`

### Argument parsing evidence

Source: `cmd/show/prefix.pl` · SHA-256 `767a7498f542b558eed44daaddefeda1e8dd5cf136439bc8a1e7c57e005965d8`

```perl
L7: my ($self, $line) = @_;
L8: my @list = split /\s+/, $line; # generate a list of callsigns
L16: foreach $l (@list) {
L20: my $pre = shift @ans;
L27: push @out, sprintf "%s City: %s State: %s", $l, join (' ', map {ucfirst} split(/\s+/, lc $ans[0]->city)), $ans[0]->state;
```

### Output and error evidence

Source: `cmd/show/prefix.pl` · SHA-256 `767a7498f542b558eed44daaddefeda1e8dd5cf136439bc8a1e7c57e005965d8`

```perl
L23: push @out, substr(sprintf("%s CC: %d IZ: %d CZ: %d LL: %s %s %4.4s (%s, %s", uc $l, $a->dxcc, $a->itu, $a->cq, slat($a->lat), slong($a->long), $a->qra, $pre, $a->name), 0, 78) . ')';
L27: push @out, sprintf "%s City: %s State: %s", $l, join (' ', map {ucfirst} split(/\s+/, lc $ans[0]->city)), $ans[0]->state;
L32: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/PREFIX <callsign>
```

**Interrogate the prefix database**

## Details

This command takes the <callsign> (which can be a full or partial
callsign or a prefix), looks up which internal country number
it is and then displays all the relevant prefixes for that country
together with the internal country no, the CQ and ITU regions.

See also SHOW/DXCC

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/prefix.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/PREFIX
```

Compare the installed handler with this page when local overrides or a different revision may be present.