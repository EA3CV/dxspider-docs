# `SHOW/DATE`

<div class="command-hero" markdown>

**Show the local time**

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
SHOW/DATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Prefix::extract()`, `a->name()`, `a->utcoff()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/date.pl` · SHA-256 `956c2a0fa3d7a604a0826b2b70b6db3cfa8f15f10e4784e91830bb1765cc48a6`

```perl
L13: my ($self, $line) = @_;
L14: my @list = split /\s+/, $line;
L22: if (@list) {
L23: foreach $l (@list) {
L27: my $pre = shift @ans;
```

### Output and error evidence

Source: `cmd/show/date.pl` · SHA-256 `956c2a0fa3d7a604a0826b2b70b6db3cfa8f15f10e4784e91830bb1765cc48a6`

```perl
L20: push @out, $self->msg("time3", cldate($t, 1), ztime($t));
L39: push @out, $self->msg("time2", $s, $buf, sprintf("%+.1f", -$off));
L44: return (1, @out);
```

### Message keys returned

`time2`, `time3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/DATE [<prefix>|<callsign>]
```

**Show the local time**

## Details

This is very nearly the same as SHOW/TIME, the only difference the format
of the date string if no arguments are given.

If no prefixes or callsigns are given then this command returns the local
time and UTC as the computer has it right now. If you give some prefixes
then it will show UTC and UTC + the local offset (not including DST) at
the prefixes or callsigns that you specify.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/date.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.