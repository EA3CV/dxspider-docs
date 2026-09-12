# `SET/PINGINTERVAL`

<div class="command-hero" markdown>

**Set ping time to neighbouring nodes**

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
SET/PINGINTERVAL [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `dxchan->pingint()`, `self->msg()`, `user->pingint()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/pinginterval.pl` · SHA-256 `84c352ae37cb0ae866779d805ee739f448a3c3f7ea74e9cc6b5e7bdbb762e5ad`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: my $val = shift @args if @args;
L19: return (1, $self->msg('e12')) unless @args;
L21: if ($val =~ /^(\d+)[sS]$/) {
L23: } elsif ($val =~ /^(\d+)[mM]$/) {
L25: } elsif ($val =~ /^(\d+)[hH]$/) {
L27: } elsif ($val =~ /^\d+$/) {
L33: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/pinginterval.pl` · SHA-256 `84c352ae37cb0ae866779d805ee739f448a3c3f7ea74e9cc6b5e7bdbb762e5ad`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 8;
L18: return (1, $self->msg('e14')) unless defined $val;
L19: return (1, $self->msg('e12')) unless @args;
L21: if ($val =~ /^(\d+)[sS]$/) {
L30: return (1, $self->msg('e14'));
```

### Output and error evidence

Source: `cmd/set/pinginterval.pl` · SHA-256 `84c352ae37cb0ae866779d805ee739f448a3c3f7ea74e9cc6b5e7bdbb762e5ad`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 8;
L18: return (1, $self->msg('e14')) unless defined $val;
L19: return (1, $self->msg('e12')) unless @args;
L30: return (1, $self->msg('e14'));
L40: push @out, $self->msg('e13', $call);
L49: push @out, $self->msg('pingint', $call, $val);
L51: push @out, $self->msg('e3', "Set/Pinginterval", $call);
L54: return (1, @out);
```

### Message keys returned

`e12`, `e13`, `e14`, `e3`, `e5`, `pingint`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/PINGINTERVAL <time> <nodecall>
```

**Set ping time to neighbouring nodes**

## Details

As from release 1.35 all neighbouring nodes are pinged at regular intervals
in order to determine the rolling quality of the link and, in future, to
affect routing decisions. The default interval is 300 secs or 5 minutes.

You can use this command to set a different interval. Please don't.

But if you do the value you enter is treated as minutes up 30 and seconds
for numbers greater than that.

This is used also to help determine when a link is down at the far end
(as certain cluster software doesn't always notice), see SET/OBSCOUNT
for more information.

If you must change it (and it may be useful for internet connected nodes
on dynamic IP addresses that go away after a set time of usage) the time
can be specified as:-

```text
5      which if less than 30 is converted to minutes otherwise is
       taken as the no of seconds between pings.
120s   120 seconds
5m     5 minutes
1h     1 hour
```

Please be aware that this causes traffic to occur on the link, setting
this value too low may annoy your neighbours beyond the point of
endurance!

You can switch this off by setting it to 0.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/pinginterval.pl){ .md-button }

## Verify on a running node

```text
HELP SET/PINGINTERVAL
```

Compare the installed handler with this page when local overrides or a different revision may be present.