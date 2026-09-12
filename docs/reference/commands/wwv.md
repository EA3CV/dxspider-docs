# `WWV`

<div class="command-hero" markdown>

**WWV command This can only be used if the appropriate flag is enabled. I would STRONGLY recommend that you**

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
WWV <structured arguments>
```

The handler parses a structured list (for example comma-separated or key/value input). See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Recognized tokens, keys or enumerated values in this handler

`a`, `call`, `k`, `sf`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXProt::send_wwv_spot()`, `Geomag::dup()`, `Geomag::update()`, `self->msg()`, `self->wwv()`

### Argument parsing evidence

Source: `cmd/wwv.pl` · SHA-256 `e89f2dca5ac57e47eee10943d616237371e4b6b6e7fd2c77555cc3f679e4c20e`

```perl
L26: my ($self, $line) = @_;
L28: $call =~ s/-\d+$//;
L39: $line = unpad($line);
L41: my @l = split /\s*,\s*/, $line;
L45: my %args = map {split /\s*=\s*/, lc $_} @l;
L67: my ($r) = $forecast =~ /R=(\d+)/;
```

### Validation and access evidence

Source: `cmd/wwv.pl` · SHA-256 `e89f2dca5ac57e47eee10943d616237371e4b6b6e7fd2c77555cc3f679e4c20e`

```perl
L29: return (1, $self->msg('e5')) unless grep $call eq $_, @Geomag::allowed;
L48: push @out, $self->msg('wwv1', 'k') unless defined $args{k} && $args{k} >= 0 && $args{k} <= 9;
L49: push @out, $self->msg('wwv1', 'a') unless defined $args{a} && $args{a} >= 0 && $args{a} <= 400;
L50: push @out, $self->msg('wwv1', 'sf') unless defined $args{sf} && $args{sf} >= 65 && $args{sf} <= 300;
```

### Output and error evidence

Source: `cmd/wwv.pl` · SHA-256 `e89f2dca5ac57e47eee10943d616237371e4b6b6e7fd2c77555cc3f679e4c20e`

```perl
L29: return (1, $self->msg('e5')) unless grep $call eq $_, @Geomag::allowed;
L48: push @out, $self->msg('wwv1', 'k') unless defined $args{k} && $args{k} >= 0 && $args{k} <= 9;
L49: push @out, $self->msg('wwv1', 'a') unless defined $args{a} && $args{a} >= 0 && $args{a} <= 400;
L50: push @out, $self->msg('wwv1', 'sf') unless defined $args{sf} && $args{sf} >= 65 && $args{sf} <= 300;
L51: push @out, $self->msg('wwv1', 'forecast') unless $forecast;
L52: push @out, $self->msg('wwv2') if Geomag::dup($d, $args{sf}, $args{k}, $args{a}, $forecast);
L54: return (1, @out) if @out;
L71: return (1, @out);
```

### Message keys returned

`e5`, `wwv1`, `wwv2`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP WWV
```

Compare the installed handler with this page when local overrides or a different revision may be present.