# `SHOW/ISOLATE`

<div class="command-hero" markdown>

**Show list of ISOLATED nodes**

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
SHOW/ISOLATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `DXUser::using_database()`, `dbh->prepare()`, `dbm->seq()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/isolate.pl` · SHA-256 `72344241b8285551270888a3e256a0bb0eeff6dc63c5c9bf01bab13b36ec4d64`

```perl
L15: my ($self, $line) = @_;
L23: return (1, $self->spawn_cmd("show/isolate $line", sub { return (generate($self)); }));
L30: my $self = shift;
L31: my $line = uc shift;
L37: push @val, split /\s+/, $line;
L40: shift @val;
L48: if ($d =~ m{"isolate":}) {
L56: if ($data =~ m{isolate}) {
```

### Validation and access evidence

Source: `cmd/show/isolate.pl` · SHA-256 `72344241b8285551270888a3e256a0bb0eeff6dc63c5c9bf01bab13b36ec4d64`

```perl
L16: return (1, $self->msg('e5')) unless $self->priv >= 1;
L48: if ($d =~ m{"isolate":}) {
L56: if ($data =~ m{isolate}) {
```

### Output and error evidence

Source: `cmd/show/isolate.pl` · SHA-256 `72344241b8285551270888a3e256a0bb0eeff6dc63c5c9bf01bab13b36ec4d64`

```perl
L16: return (1, $self->msg('e5')) unless $self->priv >= 1;
L21: return (1, generate($self));
L23: return (1, $self->spawn_cmd("show/isolate $line", sub { return (generate($self)); }));
L70: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L77: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L80: push @out, , $self->msg('rec', $count);
```

### Message keys returned

`e5`, `rec`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/ISOLATE
```

**Show list of ISOLATED nodes**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/isolate.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/ISOLATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.