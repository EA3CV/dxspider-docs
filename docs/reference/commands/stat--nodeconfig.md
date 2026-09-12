# `STAT/NODECONFIG`

<div class="command-hero" markdown>

**show who all the nodes are connected to**

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
STAT/NODECONFIG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Route::Node::get()`

### Argument parsing evidence

Source: `cmd/stat/nodeconfig.pl` · SHA-256 `10e6e8bde2b7259fca77c5a2a0deb7b13867ad3e38e0d301e3756099edcc6b7a`

```perl
L9: my ($self, $line) = @_;
L10: my @list = map { uc } split /\s+/, $line; # list of callsigns of nodes
L16: next if @list && !grep $ncall =~ m|$_|, @list;
```

### Validation and access evidence

Source: `cmd/stat/nodeconfig.pl` · SHA-256 `10e6e8bde2b7259fca77c5a2a0deb7b13867ad3e38e0d301e3756099edcc6b7a`

```perl
L16: next if @list && !grep $ncall =~ m|$_|, @list;
```

### Output and error evidence

Source: `cmd/stat/nodeconfig.pl` · SHA-256 `10e6e8bde2b7259fca77c5a2a0deb7b13867ad3e38e0d301e3756099edcc6b7a`

```perl
L19: push @out, "$call->$l";
L22: return (1, @out);
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/nodeconfig.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/NODECONFIG
```

Compare the installed handler with this page when local overrides or a different revision may be present.