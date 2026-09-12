# `SHOW/425`

<div class="command-hero" markdown>

**Query the 425 Database server for a callsign from an idea by Leo,IZ5FSA and 425DxNews Group**

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
SHOW/425 [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.

### Important calls

`AsyncMsg->get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/425.pl` · SHA-256 `bdf52cdfeb5abf8b6b42643b9fc39338c1f987617663da4202bae71d7c5011ee`

```perl
L11: my ($self, $line) = @_;
L12: my @list = map {uc} split /\s+/, $line; # generate a list of callsigns
L18: return (1, "SHOW/425 <callsign>\nSHOW/425 CAL\nSHOW/425 BULL <bulletin number>\n e.g. SH/425 IQ5BL, SH/425 CAL, SH/425 BUL 779\n") unless @list;
L23: dbg('sh/425: args=' . join('|', @list)) if isdbg('425');
```

### Validation and access evidence

Source: `cmd/show/425.pl` · SHA-256 `bdf52cdfeb5abf8b6b42643b9fc39338c1f987617663da4202bae71d7c5011ee`

```perl
L17: return (1, $self->msg('e24')) unless $Internet::allow;
```

### Output and error evidence

Source: `cmd/show/425.pl` · SHA-256 `bdf52cdfeb5abf8b6b42643b9fc39338c1f987617663da4202bae71d7c5011ee`

```perl
L17: return (1, $self->msg('e24')) unless $Internet::allow;
L18: return (1, "SHOW/425 <callsign>\nSHOW/425 CAL\nSHOW/425 BULL <bulletin number>\n e.g. SH/425 IQ5BL, SH/425 CAL, SH/425 BUL 779\n") unless @list;
L40: push @out, $self->msg('m21', "show/425");
L42: push @out, $self->msg('e18', 'Open(ARI.org)');
L45: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `m21`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/425.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/425
```

Compare the installed handler with this page when local overrides or a different revision may be present.