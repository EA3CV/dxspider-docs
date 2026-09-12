# `SHOW/ROUTE`

<div class="command-hero" markdown>

**Show the route to the callsign**

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
SHOW/ROUTE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Route::findroutes()`, `Route::get()`, `ref->isa()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/route.pl` · SHA-256 `988ef674ff577c5a3486c9a4b0aaa5ff69073297f34b12e1c338e66b911a04cd`

```perl
L9: my ($self, $line) = @_;
L10: my @list = map { uc } split /\s+/, $line; # list of callsigns of nodes
L13: return (1, $self->msg('e6')) unless @list;
L16: foreach $l (@list) {
```

### Validation and access evidence

Source: `cmd/show/route.pl` · SHA-256 `988ef674ff577c5a3486c9a4b0aaa5ff69073297f34b12e1c338e66b911a04cd`

```perl
L13: return (1, $self->msg('e6')) unless @list;
```

### Output and error evidence

Source: `cmd/show/route.pl` · SHA-256 `988ef674ff577c5a3486c9a4b0aaa5ff69073297f34b12e1c338e66b911a04cd`

```perl
L13: return (1, $self->msg('e6')) unless @list;
L22: push @out, $self->msg('route', $l, $parents, join(',', @n));
L24: push @out, $self->msg('e7', $l);
L28: return (1, @out);
```

### Message keys returned

`e6`, `e7`, `route`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/ROUTE <callsign> ...
```

**Show the route to the callsign**

## Details

This command allows you to see to which node the callsigns specified are
connected. It is a sort of inverse sh/config.

 sh/route n2tly

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/route.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/ROUTE
```

Compare the installed handler with this page when local overrides or a different revision may be present.