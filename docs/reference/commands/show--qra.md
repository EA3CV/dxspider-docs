# `SHOW/QRA`

<div class="command-hero" markdown>

**Show distance between QRA Grid locators**

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
SHOW/QRA [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXBearing::bdist()`, `DXBearing::lltoqra()`, `DXBearing::lltos()`, `DXBearing::qratoll()`, `DXBearing::stoll()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/qra.pl` · SHA-256 `c2ef27e87e3a79ba9323f31d81dcc71d85c053494fa62da5a4cbb823b546e567`

```perl
L9: my ($self, $line) = @_;
L10: my @list = split /\s+/, $line; # generate a list of callsigns
L11: return (1, $self->msg('qrashe1')) unless @list > 0;
L16: $line = uc $line;
L19: if (is_latlong($line)) {
L20: my ($llat, $llong) = DXBearing::stoll(uc $line);
L21: return (1, "QRA $line = " . DXBearing::lltoqra($llat, $llong));
L33: unshift @list, $self->user->qra if @list == 1 && $self->user->qra;
L34: unshift @list, DXBearing::lltoqra($lat, $long) unless @list > 1;
L38: $f .= 'MM' if $f =~ /^[A-Z][A-Z]\d\d$/;
L44: $l .= 'MM' if $l =~ /^[A-Z][A-Z]\d\d$/;
L50: $fll =~ s/\s+([NSEW])/$1/g;
L52: $tll =~ s/\s+([NSEW])/$1/g;
```

### Validation and access evidence

Source: `cmd/show/qra.pl` · SHA-256 `c2ef27e87e3a79ba9323f31d81dcc71d85c053494fa62da5a4cbb823b546e567`

```perl
L11: return (1, $self->msg('qrashe1')) unless @list > 0;
L38: $f .= 'MM' if $f =~ /^[A-Z][A-Z]\d\d$/;
L39: return (1, $self->msg('qrae2', $f)) unless is_qra($f);
L44: $l .= 'MM' if $l =~ /^[A-Z][A-Z]\d\d$/;
L45: return (1, $self->msg('qrae2', $l)) unless is_qra($l);
```

### Output and error evidence

Source: `cmd/show/qra.pl` · SHA-256 `c2ef27e87e3a79ba9323f31d81dcc71d85c053494fa62da5a4cbb823b546e567`

```perl
L11: return (1, $self->msg('qrashe1')) unless @list > 0;
L21: return (1, "QRA $line = " . DXBearing::lltoqra($llat, $llong));
L28: push @out, $self->msg('heade1');
L39: return (1, $self->msg('qrae2', $f)) unless is_qra($f);
L45: return (1, $self->msg('qrae2', $l)) unless is_qra($l);
L62: push @out, sprintf "$from$to To: %.0f Fr: %.0f Dst: %.0fMi %.0fKm", $b, $r, $dx * 0.62133785, $dx;
L64: return (1, @out);
```

### Message keys returned

`heade1`, `qrae2`, `qrashe1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/QRA <locator> [<locator>]
    ```

    **Show distance between QRA Grid locators**


=== "Help variant"

    ```text
    SHOW/QRA <lat> <long>
    ```

    **Convert lat/long to a QRA Grid locator**

    This is a multipurpose command that allows you either to calculate the
    distance and bearing between two locators or (if only one locator is
    given on the command line) the distance and beraing from your station
    to the locator. For example:-

     SH/QRA IO92QL
     SH/QRA JN06 IN73

    The first example will show the distance and bearing to the locator from
    yourself, the second example will calculate the distance and bearing from
    the first locator to the second. You can use 4 or 6 character locators.

    It is also possible to convert a latitude and longitude to a locator by
    using this command with a latitude and longitude as an argument, for
    example:-

     SH/QRA 52 41 N 0 58 E

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/qra.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/QRA
```

Compare the installed handler with this page when local overrides or a different revision may be present.