# `STAT/ROUTE`

<div class="command-hero" markdown>

**show a Route thingy A general purpose Route get thingy, use stat/route_user or _node if you want a list of all that particular type of thingy otherwise this**

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
STAT/ROUTE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Route::get()`

### Argument parsing evidence

Source: `cmd/stat/route.pl` · SHA-256 `e39417f16b8b4509a90be31a13afc93caebc6425122d853bd71096682d3dde98`

```perl
L11: my ($self, $line) = @_;
L13: my @list = split /\s+/, $line; # generate a list of callsigns
L15: push @list, $self->call unless @list;
L17: foreach my $call (@list) {
L25: push @out, "" if @list > 1;
```

### Output and error evidence

Source: `cmd/stat/route.pl` · SHA-256 `e39417f16b8b4509a90be31a13afc93caebc6425122d853bd71096682d3dde98`

```perl
L21: push @out, print_all_fields($self, $ref, "Route::User Information $call");
L23: push @out, "Route: $call not found";
L25: push @out, "" if @list > 1;
L28: return (1, @out);
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/route.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/ROUTE
```

Compare the installed handler with this page when local overrides or a different revision may be present.