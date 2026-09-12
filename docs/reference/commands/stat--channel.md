# `STAT/CHANNEL`

<div class="command-hero" markdown>

**Show the status of a channel on the cluster**

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
STAT/CHANNEL [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`

### Argument parsing evidence

Source: `cmd/stat/channel.pl` · SHA-256 `6318dcaef33992ebced5085a3d7c8b1bd5e75fab18f957ea41ab017f43c18beb`

```perl
L8: my ($self, $line) = @_;
L9: my @list = split /\s+/, $line; # generate a list of callsigns
L10: @list = ($self->call) if !@list || $self->priv < 1; # my channel if no callsigns
L14: foreach $call (@list) {
L22: push @out, "" if @list > 1;
```

### Validation and access evidence

Source: `cmd/stat/channel.pl` · SHA-256 `6318dcaef33992ebced5085a3d7c8b1bd5e75fab18f957ea41ab017f43c18beb`

```perl
L10: @list = ($self->call) if !@list || $self->priv < 1; # my channel if no callsigns
```

### Output and error evidence

Source: `cmd/stat/channel.pl` · SHA-256 `6318dcaef33992ebced5085a3d7c8b1bd5e75fab18f957ea41ab017f43c18beb`

```perl
L20: return (0, "Channel: $call not found") if !$ref;
L22: push @out, "" if @list > 1;
L25: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
STAT/CHANNEL [<callsign>]
```

**Show the status of a channel on the cluster**

## Details

Show the internal status of the channel object either for the channel that
you are on or else for the callsign that you asked for.

Only the fields that are defined (in perl term) will be displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/channel.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/CHANNEL
```

Compare the installed handler with this page when local overrides or a different revision may be present.