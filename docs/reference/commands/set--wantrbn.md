# `SET/WANTRBN`

<div class="command-hero" markdown>

**Choose which curated RBN/Skimmer categories are delivered to the user.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>RBN</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
SET/WANTRBN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantbeacon()`, `user->wantcw()`, `user->wantft()`, `user->wantpsk()`, `user->wantrbn()`, `user->wantrtty()`

### Argument parsing evidence

Source: `cmd/set/wantrbn.pl` · SHA-256 `efb212d7fee5efbbb8c682f01c7703667eb53fe197b59edb42a1c9180c215548`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L17: dbg('set/skimmer @args = "' . join(', ', @args) . '"') if isdbg('set/skim');
L19: while (@args) {
L20: my $a = shift @args;
L31: my ($want) = $a =~ /^(FT|BCN|BEA|DXF|CW|PSK|MSK|FSK|RTT|NO)/;
```

### Validation and access evidence

Source: `cmd/set/wantrbn.pl` · SHA-256 `efb212d7fee5efbbb8c682f01c7703667eb53fe197b59edb42a1c9180c215548`

```perl
L22: if ($a !~ /^(?:FT|BCN|BEA|DXF|CW|PSK|MSK|FSK|RTT|NO)/ && is_callsign($a)) {
L23: return (1, $self->msg('e5')) if $a ne $self->call && $self->priv < 9;
L32: return (1, $self->msg('e39', $a)) unless $want;
```

### Output and error evidence

Source: `cmd/set/wantrbn.pl` · SHA-256 `efb212d7fee5efbbb8c682f01c7703667eb53fe197b59edb42a1c9180c215548`

```perl
L23: return (1, $self->msg('e5')) if $a ne $self->call && $self->priv < 9;
L32: return (1, $self->msg('e39', $a)) unless $want;
L111: push @out, $self->msg('skims', $call, $s);
L114: push @out, $self->msg('e3', "Set Skimmer", $call);
L117: return (1, @out);
```

### Message keys returned

`e3`, `e39`, `e5`, `skims`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SET/WANTRBN
    ```

    **[category ..]^Allow (some) RBN/Skimmer spots**


=== "Help variant"

    ```text
    SET/WANTRBN
    ```

    **<call> [category ..]^Allow (some) RBN/Skimmer spots**


## Practical examples

### Enable the default RBN selection

```text
SET/WANTRBN
```

### CW only

```text
SET/WANTRBN CW
```

### Digital categories

```text
SET/WANTRBN PSK RTTY FT
```

### Disable RBN delivery

```text
UNSET/WANTRBN
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/wantrbn.pl){ .md-button }

## Related commands

- [`UNSET/WANTRBN`](unset--wantrbn.md)
- [`ACCEPT/RBN`](accept--rbn.md)
- [`REJECT/RBN`](reject--rbn.md)
- [`CLEAR/RBN`](clear--rbn.md)

## Verify on a running node

```text
HELP SET/WANTRBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.