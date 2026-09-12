# `LINKS`

<div class="command-hero" markdown>

**Show which nodes is physically connected**

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
LINKS
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`dxchan->call()`

### Argument parsing evidence

Source: `cmd/links.pl` · SHA-256 `98c8cdb98f475ff02297a778ddd8183bfa6ac3f06c0471108146996e1301df57`

```perl
L13: my $self = shift;
L40: $fin = $dxchan->inroutefilter =~ /node_default/ ? 'D' : 'Y';
L43: $fout = $dxchan->routefilter =~ /node_default/ ? 'D' : 'Y';
L64: $ipaddr = 'local' if $addr =~ /^127\./ || $addr =~ /^::[0-9a-f]+$/;
```

### Validation and access evidence

Source: `cmd/links.pl` · SHA-256 `98c8cdb98f475ff02297a778ddd8183bfa6ac3f06c0471108146996e1301df57`

```perl
L64: $ipaddr = 'local' if $addr =~ /^127\./ || $addr =~ /^::[0-9a-f]+$/;
```

### Output and error evidence

Source: `cmd/links.pl` · SHA-256 `98c8cdb98f475ff02297a778ddd8183bfa6ac3f06c0471108146996e1301df57`

```perl
L18: push @out, " Ave Obs Ping Next Filters";
L19: push @out, " Callsign Type Started Uptime RTT Count Int. Ping Iso? In Out PC92? Address";
L68: push @out, sprintf "%10s $sort $t%13s$ping $obscount %5d %5d $iso $fin $fout $pc92 $ipaddr", $call, $uptime ,$pingint, $lastt;
L71: return (1, @out)
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LINKS
```

**Show which nodes is physically connected**

## Details

This is a quick listing that shows which links are connected and
some information about them. See WHO for a list of all connections.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/links.pl){ .md-button }

## Verify on a running node

```text
HELP LINKS
```

Compare the installed handler with this page when local overrides or a different revision may be present.