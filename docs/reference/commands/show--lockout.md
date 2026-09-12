# `SHOW/LOCKOUT`

<div class="command-hero" markdown>

**Show the list of locked out or excluded callsigns**

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
SHOW/LOCKOUT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`ALL`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXUser::get_current()`, `DXUser::using_database()`, `dbh->prepare()`, `dbm->seq()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/lockout.pl` · SHA-256 `af00705a54e0082bae9a5e9dd86d053ad6221744c58d6918b2b94aee44e16caf`

```perl
L13: my ($self, $line) = @_;
L15: return (1, $self->msg('lockoutuse')) unless $line;
L17: return (1, generate($self, $line));
L19: return (1, $self->spawn_cmd("show/lockout$line", sub { return (generate($self, $line)); }));
L25: my $self = shift;
L26: my $line = shift;
L34: push @val, split /\s+/, uc $line;
L36: shift @val;
L43: if ($d =~ m{"lockout":(\d)}) {
L52: if ($data =~ m{"lockout":(\d)}) {
L62: $mcall =~ s/-0$//;
L69: unless ($call =~ /-\d{1,2}$/ ) {
```

### Validation and access evidence

Source: `cmd/show/lockout.pl` · SHA-256 `af00705a54e0082bae9a5e9dd86d053ad6221744c58d6918b2b94aee44e16caf`

```perl
L14: return (1, $self->msg('e5')) unless $self->priv >= 9;
L15: return (1, $self->msg('lockoutuse')) unless $line;
L43: if ($d =~ m{"lockout":(\d)}) {
L52: if ($data =~ m{"lockout":(\d)}) {
L69: unless ($call =~ /-\d{1,2}$/ ) {
```

### Output and error evidence

Source: `cmd/show/lockout.pl` · SHA-256 `af00705a54e0082bae9a5e9dd86d053ad6221744c58d6918b2b94aee44e16caf`

```perl
L14: return (1, $self->msg('e5')) unless $self->priv >= 9;
L15: return (1, $self->msg('lockoutuse')) unless $line;
L17: return (1, generate($self, $line));
L19: return (1, $self->spawn_cmd("show/lockout$line", sub { return (generate($self, $line)); }));
L85: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L92: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L95: push @out, $@ if $@;
L96: push @out, $self->msg('rec', $count);
```

### Message keys returned

`e5`, `lockoutuse`, `rec`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/LOCKOUT <prefix>|ALL
```

**Show the list of locked out or excluded callsigns**

## Details

This command works in the same general way as SET/LOCKOUT, in that using a bare
callsign without ssid will show all the callsign + ssid users as well as the bare callsign. In
order to just see the base callsign's lock status, use the ssid '-0'. E.g. G1TLH-0.

The ALL keyword will search through the user database for callsigns that are locked.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/lockout.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/LOCKOUT
```

Compare the installed handler with this page when local overrides or a different revision may be present.