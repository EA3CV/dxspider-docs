# `WX`

<div class="command-hero" markdown>

**Send a weather message to local users**

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
WX [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Uses or emits DX protocol data.

### Recognized tokens, keys or enumerated values in this handler

`FULL`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`BadWords::check()`, `DXChannel::broadcast_list()`, `DXChannel::broadcast_nodes()`, `DXProt::pc12()`, `DXProt::pc93()`, `badspotter->in()`, `me->normal()`, `self->badcount()`, `self->msg()`, `self->send()`

### Argument parsing evidence

Source: `cmd/wx.pl` · SHA-256 `5a50bc4ec4bf8a3be42c9a6e4ddd3149323b691fcae46e8ce25a44a317e9a4d3`

```perl
L17: my ($self, $line) = @_;
L18: my @f = split /\s+/, $line;
L29: $line =~ s/^$f[0]\s+//; # remove it
L38: $nossid =~ s/-\d+$//;
L40: LogDbg('DXCommand', "bad spotter ($self->{call}) made announcement: $line");
L46: if (@bad = BadWords::check($line)) {
L48: LogDbg('DXCommand', "$self->{call} swore: $line (with words:" . join(',', @bad) . ")");
L53: Log('ann', $to, $from, "[to $from only] $line");
L54: $self->send("WX de $from: $line");
L60: Log('ann', $via ? $via : '*', $from, $line, $ipaddr);
L61: $main::me->normal(DXProt::pc93($to, $from, $via, $line, undef, $ipaddr));
```

### Validation and access evidence

Source: `cmd/wx.pl` · SHA-256 `5a50bc4ec4bf8a3be42c9a6e4ddd3149323b691fcae46e8ce25a44a317e9a4d3`

```perl
L25: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L26: return (1, $self->msg('e28')) unless $self->isregistered;
```

### Output and error evidence

Source: `cmd/wx.pl` · SHA-256 `5a50bc4ec4bf8a3be42c9a6e4ddd3149323b691fcae46e8ce25a44a317e9a4d3`

```perl
L25: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L26: return (1, $self->msg('e28')) unless $self->isregistered;
L54: $self->send("WX de $from: $line");
L55: return (1, ());
L70: return (1, ());
```

### Message keys returned

`e28`, `e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    WX <text>
    ```

    **Send a weather message to local users**


=== "Help variant"

    ```text
    WX FULL <text>
    ```

    **Send a weather message to all cluster users**


=== "Help variant"

    ```text
    WX SYSOP <text>
    ```

    **Send a weather message to other clusters only**

    Weather messages can sometimes be useful if you are experiencing an extreme
    that may indicate enhanced conditions

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/wx.pl){ .md-button }

## Verify on a running node

```text
HELP WX
```

Compare the installed handler with this page when local overrides or a different revision may be present.