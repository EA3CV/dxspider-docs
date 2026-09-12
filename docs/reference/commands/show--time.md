# `SHOW/TIME`

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
SHOW/TIME [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Prefix::extract()`, `a->name()`, `a->utcoff()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/time.pl` · SHA-256 `a1358de589d9111f3498193ef1ec6fc86b8a89ea44e998ce4a6fdbb5f46779d6`

```perl
L10: my ($self, $line) = @_;
L11: my @list = split /\s+/, $line;
L13: push @list, $self->call unless @list;
L18: if ($list[0] =~ /^\d+$/) {
L19: $t = shift @list;
L24: if (@list) {
L25: foreach $l (@list) {
L29: my $pre = shift @ans;
```

### Validation and access evidence

Source: `cmd/show/time.pl` · SHA-256 `a1358de589d9111f3498193ef1ec6fc86b8a89ea44e998ce4a6fdbb5f46779d6`

```perl
L18: if ($list[0] =~ /^\d+$/) {
```

### Output and error evidence

Source: `cmd/show/time.pl` · SHA-256 `a1358de589d9111f3498193ef1ec6fc86b8a89ea44e998ce4a6fdbb5f46779d6`

```perl
L22: push @out, $self->msg("time1", cldate($t, 1), ztime($t, 1), ztime($t));
L41: push @out, $self->msg("time2", $s, $buf, sprintf("%+.1f", -$off));
L46: return (1, @out);
```

### Message keys returned

`time1`, `time2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/TIME [<prefix>|<callsign>]
```

**Show the local time**

## Details

If no prefixes or callsigns are given then this command returns the local
time and UTC as the computer has it right now. If you give some prefixes
then it will show UTC and UTC + the local offset (not including DST) at
the prefixes or callsigns that you specify.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/time.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/TIME
```

Compare the installed handler with this page when local overrides or a different revision may be present.