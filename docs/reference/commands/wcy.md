# `WCY`

<div class="command-hero" markdown>

**WCY command This can only be used if the appropriate flag is enabled. I would STRONGLY recommend that, unless your callsign is DK8LV, you**

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
WCY <structured arguments>
```

The handler parses a structured list (for example comma-separated or key/value input). See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Recognized tokens, keys or enumerated values in this handler

`a`, `act`, `au`, `aurora`, `eru`, `expk`, `gmf`, `k`, `mag`, `maj`, `min`, `nil`, `no`, `pro`, `qui`, `r`, `sa`, `sev`, `sf`, `strong`, `war`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXProt::send_wcy_spot()`, `WCY::dup()`, `WCY::update()`, `self->msg()`, `self->wcy()`

### Argument parsing evidence

Source: `cmd/wcy.pl` · SHA-256 `dbbc03ab2ceca84d208f98fc2ca6b1d1e9fe6001fcefa734d7079fce13b976b8`

```perl
L27: my ($self, $line) = @_;
L29: $call =~ s/-\d+$//;
L38: $line = unpad($line);
L39: my %args = map {split /\s*=\s*/} split /\s*,\s*/, lc $line;
```

### Validation and access evidence

Source: `cmd/wcy.pl` · SHA-256 `dbbc03ab2ceca84d208f98fc2ca6b1d1e9fe6001fcefa734d7079fce13b976b8`

```perl
L30: return (1, $self->msg('e5')) unless grep $call eq $_, @WCY::allowed;
L42: push @out, $self->msg('wcy1', 'k') unless defined $args{k} && $args{k} >= 0 && $args{k} <= 9;
L43: push @out, $self->msg('wcy1', 'espk') unless defined $args{expk} && $args{expk} >= 0 && $args{expk} <= 9;
L44: push @out, $self->msg('wcy1', 'a') unless defined $args{a} && $args{a} >= 0 && $args{a} <= 400;
L45: push @out, $self->msg('wcy1', 'r') unless defined $args{r} && $args{r} >= 0 && $args{r} <= 500;
L46: push @out, $self->msg('wcy1', 'sf') unless defined $args{sf} && $args{sf} >= 65 && $args{sf} <= 300;
L47: push @out, $self->msg('wcy1', 'sa') unless defined $args{sa} && grep $args{sa} eq $_, qw(qui eru act maj pro war nil);
L48: push @out, $self->msg('wcy1', 'gmf') unless defined $args{gmf} && grep $args{gmf} eq $_, qw(qui act min maj sev mag war nil);
L49: push @out, $self->msg('wcy1', 'au') unless defined $args{au} && grep $args{au} eq $_, qw(no aurora strong);
```

### Output and error evidence

Source: `cmd/wcy.pl` · SHA-256 `dbbc03ab2ceca84d208f98fc2ca6b1d1e9fe6001fcefa734d7079fce13b976b8`

```perl
L30: return (1, $self->msg('e5')) unless grep $call eq $_, @WCY::allowed;
L42: push @out, $self->msg('wcy1', 'k') unless defined $args{k} && $args{k} >= 0 && $args{k} <= 9;
L43: push @out, $self->msg('wcy1', 'espk') unless defined $args{expk} && $args{expk} >= 0 && $args{expk} <= 9;
L44: push @out, $self->msg('wcy1', 'a') unless defined $args{a} && $args{a} >= 0 && $args{a} <= 400;
L45: push @out, $self->msg('wcy1', 'r') unless defined $args{r} && $args{r} >= 0 && $args{r} <= 500;
L46: push @out, $self->msg('wcy1', 'sf') unless defined $args{sf} && $args{sf} >= 65 && $args{sf} <= 300;
L47: push @out, $self->msg('wcy1', 'sa') unless defined $args{sa} && grep $args{sa} eq $_, qw(qui eru act maj pro war nil);
L48: push @out, $self->msg('wcy1', 'gmf') unless defined $args{gmf} && grep $args{gmf} eq $_, qw(qui act min maj sev mag war nil);
L49: push @out, $self->msg('wcy1', 'au') unless defined $args{au} && grep $args{au} eq $_, qw(no aurora strong);
L51: push @out, $self->msg('wcy2') if WCY::dup($d);
L54: return (1, @out) if @out;
L68: return (1, @out);
```

### Message keys returned

`e5`, `wcy1`, `wcy2`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/wcy.pl){ .md-button }

## Verify on a running node

```text
HELP WCY
```

Compare the installed handler with this page when local overrides or a different revision may be present.