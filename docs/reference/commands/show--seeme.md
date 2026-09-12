# `SHOW/SEEME`

<div class="command-hero" markdown>

**show/registered show all registered users dbg("set/register line: $line");**

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
SHOW/SEEME [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXChannel::get()`, `DXUser::get_current()`, `DXUser::using_database()`, `dbh->prepare()`, `dbm->seq()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/seeme.pl` · SHA-256 `bd73c81fc0b2432f5534844ac17f255f79d86079007ea6a0513364fbc6da8269`

```perl
L13: my ($self, $line) = @_;
L20: if ($line) {
L21: $line =~ s/[^\w\-\/]+//g;
L22: $line = uc "\Q$line";
L26: @out = generate($self, $line);
L28: @out = $self->spawn_cmd("show/seeme $line", sub { return (generate($self, $line)); });
L36: my $self = shift;
L37: my $line = shift;
L44: $call{$_} = 1 for split /\s+/, $line;
L54: if ($d =~ m{"rbnseeme":}) {
L62: if ($data =~ m{rbnseeme}) {
```

### Validation and access evidence

Source: `cmd/show/seeme.pl` · SHA-256 `bd73c81fc0b2432f5534844ac17f255f79d86079007ea6a0513364fbc6da8269`

```perl
L14: return (1, $self->msg('e5')) unless $self->priv >= 9;
L54: if ($d =~ m{"rbnseeme":}) {
L62: if ($data =~ m{rbnseeme}) {
L71: if ($u && defined (my $r = $u->rbnseeme)) {
```

### Output and error evidence

Source: `cmd/show/seeme.pl` · SHA-256 `bd73c81fc0b2432f5534844ac17f255f79d86079007ea6a0513364fbc6da8269`

```perl
L14: return (1, $self->msg('e5')) unless $self->priv >= 9;
L28: @out = $self->spawn_cmd("show/seeme $line", sub { return (generate($self, $line)); });
L31: return (1, @out);
L79: push @out, "RBN See Me Users";
L82: push @out, sprintf "%-14s %-14s %-14s %-14s %-14s", @l;
L89: push @out, sprintf "%-14s %-14s %-14s %-14s %-14s", @l;
L92: push @out, $self->msg('rec', $count);
```

### Message keys returned

`e5`, `rec`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/seeme.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/SEEME
```

Compare the installed handler with this page when local overrides or a different revision may be present.