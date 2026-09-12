# `ANNOUNCE`

<div class="command-hero" markdown>

**Send local, cluster-wide or SYSOP-only announcements.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Communications</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
ANNOUNCE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Uses or emits DX protocol data.

### Recognized tokens, keys or enumerated values in this handler

`FULL`, `LOCAL`, `SYSOP`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`AnnTalk::dup()`, `BadWords::check()`, `DXChannel::broadcast_list()`, `DXChannel::broadcast_nodes()`, `DXProt::pc12()`, `DXProt::pc93()`, `badspotter->in()`, `me->normal()`, `self->badcount()`, `self->msg()`, `self->send()`

### Argument parsing evidence

Source: `cmd/announce.pl` · SHA-256 `21595c53427125481f9a4453509a048ac78edf66b600619459b848675bff11bc`

```perl
L18: my ($self, $line) = @_;
L21: Log('cmd', "$self->{call}|$addr|announce|$line");
L22: my @f = split /\s+/, $line;
L37: $line =~ s/^$f[0]\s+//; # remove it
L40: $line =~ s/^$f[0]\s+//; # remove it
L44: $line =~ s/^$f[0]\s+//; # remove it
L50: $nossid =~ s/-\d+$//;
L52: LogDbg('DXCommand', "bad spotter ($self->{call}) made announcement: $line");
L58: if (@bad = BadWords::check($line)) {
L60: LogDbg('DXCommand', "$self->{call} swore: $line (with words:" . join(',', @bad) . ")");
L65: Log('ann', $to, $from, "[to $from only] $line");
L66: $self->send("To $to de $from: $line");
L72: Log('ann', $to, $from, $line);
L73: $main::me->normal(DXProt::pc93($to, $from, $via, $line, undef, $ipaddr));
```

### Validation and access evidence

Source: `cmd/announce.pl` · SHA-256 `21595c53427125481f9a4453509a048ac78edf66b600619459b848675bff11bc`

```perl
L23: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L24: return (1, $self->msg('e9')) if !@f;
L25: return (1, $self->msg('e28')) unless $self->isregistered;
```

### Output and error evidence

Source: `cmd/announce.pl` · SHA-256 `21595c53427125481f9a4453509a048ac78edf66b600619459b848675bff11bc`

```perl
L23: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L24: return (1, $self->msg('e9')) if !@f;
L25: return (1, $self->msg('e28')) unless $self->isregistered;
L66: $self->send("To $to de $from: $line");
L67: return (1, ());
L81: return (1, ());
```

### Message keys returned

`dup`, `e28`, `e5`, `e9`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    ANNOUNCE <text>
    ```

    **Send an announcement to LOCAL users only**

    <text> is the text of the announcement you wish to broadcast

=== "Help variant"

    ```text
    ANNOUNCE FULL <text>
    ```

    **Send an announcement cluster wide**

    This will send your announcement cluster wide

=== "Help variant"

    ```text
    ANNOUNCE SYSOP <text>
    ```

    **Send an announcement to Sysops only**


## Practical examples

### Local users only

```text
ANNOUNCE Local net starts at 20:00Z
```

### Cluster-wide

```text
ANNOUNCE FULL Contest starts in 10 minutes
```

### SYSOP audience

```text
ANNOUNCE SYSOP Link maintenance at 22:00Z
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/announce.pl){ .md-button }

## Related commands

- [`SHOW/ANNOUNCE`](show--announce.md)
- [`ACCEPT/ANNOUNCE`](accept--announce.md)
- [`REJECT/ANNOUNCE`](reject--announce.md)

## Verify on a running node

```text
HELP ANNOUNCE
```

Compare the installed handler with this page when local overrides or a different revision may be present.