# `SHOW/STATION`

<div class="command-hero" markdown>

**Show list of users in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SHOW/STATION [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXBearing::bdist()`, `DXBearing::lltoqra()`, `DXBearing::lltos()`, `DXBearing::qratoll()`, `DXUser::get_all_calls()`, `DXUser::get_current()`, `DXUtil::cldatetime()`, `Route::get()`, `cref->isa()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/station.pl` · SHA-256 `3f3d7c08c40ad35df53fd7ad642b2058185e341eb61135a41d811ac19ad19a9e`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, uc $line;
```

### Output and error evidence

Source: `cmd/show/station.pl` · SHA-256 `3f3d7c08c40ad35df53fd7ad642b2058185e341eb61135a41d811ac19ad19a9e`

```perl
L76: push @out, sprintf("%-13s: %s (%s %s)", $self->msg('user'), $call, $self->msg('at'), $seek);
L78: push @out, sprintf("%-13s: %s", $self->msg('user'), $call);
L80: push @out, sprintf("%-13s: %s", $self->msg('name1'), $name) if $name;
L81: push @out, sprintf("%-13s: %s", $self->msg('lastconn'), $last) if $last;
L82: push @out, sprintf("%-13s: %s", 'QTH', $qth) if $qth;
L83: push @out, sprintf("%-13s: %s", $self->msg('location'), "$latlong ($qra)") if $latlong || $qra ;
L84: push @out, sprintf("%-13s: %.0f Deg. %.0f Mi. %.0f Km.", $self->msg('heading'), $bearing, $miles, $dx) if $latlong;
L85: push @out, sprintf("%-13s: %s", $self->msg('homenode2'), $homenode) if $homenode;
L87: push @out, $self->msg('usernf', $call);
L92: return (1, @out);
```

### Message keys returned

`at`, `e6`, `heading`, `homenode2`, `lastconn`, `location`, `name1`, `user`, `usernf`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/STATION ALL [<regex>]
    ```

    **Show list of users in the system**


=== "Help variant"

    ```text
    SHOW/STATION [<callsign> ..]
    ```

    **Show information about a callsign**

    Show the information known about a callsign and whether (and where)
    that callsign is connected to the cluster.

    ```text
    SH/ST G1TLH
    ```

    If no callsign is given then show the information for yourself.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/station.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/STATION
```

Compare the installed handler with this page when local overrides or a different revision may be present.