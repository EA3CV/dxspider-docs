# `SHOW/REGISTERED`

<div class="command-hero" markdown>

**Show the registered users**

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
SHOW/REGISTERED [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `DXUser::using_database()`, `dbh->prepare()`, `dbm->seq()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/registered.pl` · SHA-256 `b995ae10367d90f52b79ad9d2e29744d1203193d3c891d82a610a5050b2124fa`

```perl
L16: my ($self, $line) = @_;
L21: if ($line) {
L22: $line =~ s/[^\w\-\/]+//g;
L23: $line = uc"\Q$line";
L27: @out = generate($self, $line);
L29: @out = $self->spawn_cmd("show/registered $line", sub { return (generate($self, $line)); });
L37: my $self = shift;
L38: my $line = shift;
L45: $call{$_} = 1 for split /\s+/, $line;
L59: if ($d =~ m{registered}) {
L65: if ($data =~ m{registered}) {
```

### Validation and access evidence

Source: `cmd/show/registered.pl` · SHA-256 `b995ae10367d90f52b79ad9d2e29744d1203193d3c891d82a610a5050b2124fa`

```perl
L17: return (1, $self->msg('e5')) unless $self->priv >= 9;
L59: if ($d =~ m{registered}) {
L65: if ($data =~ m{registered}) {
L76: if ($u && defined (my $r = $u->registered)) {
```

### Output and error evidence

Source: `cmd/show/registered.pl` · SHA-256 `b995ae10367d90f52b79ad9d2e29744d1203193d3c891d82a610a5050b2124fa`

```perl
L17: return (1, $self->msg('e5')) unless $self->priv >= 9;
L29: @out = $self->spawn_cmd("show/registered $line", sub { return (generate($self, $line)); });
L32: return (1, @out);
L83: push @out, "Registration is " . ($main::reqreg ? "Required" : "NOT Required");
L86: push @out, sprintf "%-14s %-14s %-14s %-14s %-14s", @l;
L93: push @out, sprintf "%-14s %-14s %-14s %-14s %-14s", @l;
L96: push @out, $self->msg('rec', $count);
```

### Message keys returned

`e5`, `rec`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/REGISTERED [<prefix>]
```

**Show the registered users**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/registered.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/REGISTERED
```

Compare the installed handler with this page when local overrides or a different revision may be present.