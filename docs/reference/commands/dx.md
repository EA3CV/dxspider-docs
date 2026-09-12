# `DX`

<div class="command-hero" markdown>

**Send a DX spot into the cluster network.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
DX [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Uses or emits DX protocol data.
- Reads or changes spot data.

### Important calls

`BadWords::check()`, `Bands::get_all()`, `DXProt::pc61()`, `DXProt::send_dx_spot()`, `Spot::add_local()`, `Spot::dup_find()`, `Spot::prepare()`, `baddx->in()`, `badspotter->in()`, `self->badcount()`, `self->dx_spot()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dx.pl` · SHA-256 `65f5999dea40595b0d36789b7c1619bd264b5bd40a58c8ab8340395b3b991d48`

```perl
L11: my ($self, $line) = @_;
L12: my @f = split /\s+/, $line, 3;
L19: my $oline = $line;
L29: Log('cmd', "$self->{call}|$addr|dx|$line");
L32: if (@bad = BadWords::check($line)) {
L34: LogDbg('DXCommand', "$self->{call} swore: $line (with words:" . join(',', @bad) . ")");
L45: if ($f[0] =~ /^by$/i) {
L48: $line =~ s/^\s*$f[0]\s+$f[1]\s+//;
L49: @f = split /\s+/, $line, 3;
L54: @f = split /\s+/, $line, 3;
L62: $line =~ s/^\s*$f[0]\s+$f[1]\s+//;
L63: @f = split /\s+/, $line, 3;
L68: if (is_freq($f[1]) && $f[0] =~ m{^[\w\d]+(?:/[\w\d]+){0,2}$}) {
L71: } elsif (is_freq($f[0]) && $f[1] =~ m{^[\w\d]+(?:/[\w\d]+){0,2}$}) {
L77: $line =~ s/^\s*$f[0]//;
L78: $line =~ s/^\s*$f[1]//;
L79: $line = unpad($line);
L80: $line =~ s/\t+/ /g; # do this here because it needs to be stopped ASAP!
L81: $line ||= ' ';
L106: if (($spotted =~ /$spotternoid/ || $spotted =~ /$callnoid/) && $freq < $Spot::minselfspotqrg) {
L158: my @spot = Spot::prepare($freq, $spotted, $t, $line, $spotter, $main::mycall, $ipaddr);
L162: if ($freq =~ /^69/ || $localonly) {
L165: if ($freq =~ /^69/) {
L175: my $spot = DXProt::pc61($spotter, $freq, $spotted, unpad($line), $ipaddr);
L186: LogDbg("DXCommand", "Spot dupe from $spotter: $line");
```

### Validation and access evidence

Source: `cmd/dx.pl` · SHA-256 `65f5999dea40595b0d36789b7c1619bd264b5bd40a58c8ab8340395b3b991d48`

```perl
L23: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L24: return (1, $self->msg('e28')) unless $self->isregistered;
L39: return (1, $self->msg('dx2')) unless @f >= 2;
L45: if ($f[0] =~ /^by$/i) {
L46: return (1, $self->msg('e5')) unless $main::allowdxby || $self->priv > 1;
L50: return (1, $self->msg('dx2')) unless @f >= 2;
L56: return (1, $self->msg('e5')) unless $spotter && $self->priv > 1;
L60: return (1, $self->msg('dx4', $f[1]));
L68: if (is_freq($f[1]) && $f[0] =~ m{^[\w\d]+(?:/[\w\d]+){0,2}$}) {
L75: return (1, $self->msg('dx3'));
L106: if (($spotted =~ /$spotternoid/ || $spotted =~ /$callnoid/) && $freq < $Spot::minselfspotqrg) {
L162: if ($freq =~ /^69/ || $localonly) {
L165: if ($freq =~ /^69/) {
L185: return (1, $self->msg('dup'));
```

### Output and error evidence

Source: `cmd/dx.pl` · SHA-256 `65f5999dea40595b0d36789b7c1619bd264b5bd40a58c8ab8340395b3b991d48`

```perl
L23: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L24: return (1, $self->msg('e28')) unless $self->isregistered;
L39: return (1, $self->msg('dx2')) unless @f >= 2;
L46: return (1, $self->msg('e5')) unless $main::allowdxby || $self->priv > 1;
L50: return (1, $self->msg('dx2')) unless @f >= 2;
L56: return (1, $self->msg('e5')) unless $spotter && $self->priv > 1;
L60: return (1, $self->msg('dx4', $f[1]));
L75: return (1, $self->msg('dx3'));
L146: push @out, $self->msg('dx1', $freq) unless $valid;
L150: push @out, $self->msg('dx2');
L154: return (1, @out) unless $valid;
L171: return (1);
L185: return (1, $self->msg('dup'));
L193: return (1, @out);
```

### Message keys returned

`dup`, `dx1`, `dx2`, `dx3`, `dx4`, `e28`, `e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    DX <freq> <call> <remarks>
    ```

    **Send a DX spot**


=== "Help variant"

    ```text
    DX [BY <call>] [ip <ipaddress>] <freq> <call> <remarks>
    ```

    **Send a DX spot**

    This is how you send a DX Spot to other users. You can, in fact, now
    enter the <freq> and the <call> either way round.

    ```text
     DX FR0G 144.600
     DX 144.600 FR0G
     DX 144600 FR0G
    ```

    will all give the same result. You can add some remarks to the end
    of the command and they will be added to the spot.

    ```text
     DX FR0G 144600 this is a test
    ```

    You can credit someone else by saying:-

    ```text
     DX by G1TLH FR0G 144.600 he isn't on the cluster
    ```

    The <freq> is compared against the available bands set up in the
    cluster.  See SHOW/BANDS for more information.

## Practical examples

### Normal spot

```text
DX 14025.0 K1ABC CQ
```

### With a short comment

```text
DX 50313.0 EA8XYZ FT8
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dx.pl){ .md-button }

## Related commands

- [`SHOW/DX`](show--dx.md)
- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)

## Verify on a running node

```text
HELP DX
```

Compare the installed handler with this page when local overrides or a different revision may be present.