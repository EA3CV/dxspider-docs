# `MERGE`

<div class="command-hero" markdown>

**Ask for the latest spots and WWV**

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
MERGE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`Route::Node::get()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/merge.pl` · SHA-256 `6b34a5bc7b50374206959aa93e3cdd8694e081e174770e59e44cc21ebc760527`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
L28: my ($spots, $wwv) = $f[1] =~ m{(\d+)/(\d+)} if $f[1];
```

### Validation and access evidence

Source: `cmd/merge.pl` · SHA-256 `6b34a5bc7b50374206959aa93e3cdd8694e081e174770e59e44cc21ebc760527`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L14: return (1, $self->msg('e12')) if !$f[0];
L17: return (1, $self->msg('e11', $call)) if $call eq $main::mycall;
L25: return (1, $self->msg('e10', $call)) unless $ref;
L35: return (1, $self->msg('merge1', $call, $spots, $wwv));
```

### Output and error evidence

Source: `cmd/merge.pl` · SHA-256 `6b34a5bc7b50374206959aa93e3cdd8694e081e174770e59e44cc21ebc760527`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L14: return (1, $self->msg('e12')) if !$f[0];
L17: return (1, $self->msg('e11', $call)) if $call eq $main::mycall;
L19: push @out, $self->msg('e11', $call);
L25: return (1, $self->msg('e10', $call)) unless $ref;
L33: $dxchan->send("PC25^$call^$main::mycall^$spots^$wwv^");
L35: return (1, $self->msg('merge1', $call, $spots, $wwv));
```

### Message keys returned

`e10`, `e11`, `e12`, `e5`, `merge1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
MERGE <node> [<no spots>/<no wwv>]
```

**Ask for the latest spots and WWV**

## Details

MERGE allows you to bring your spot and wwv database up to date. By default
it will request the last 10 spots and 5 WWVs from the node you select. The
node must be connected locally.

You can request any number of spots or wwv and although they will be appended
to your databases they will not duplicate any that have recently been added
(the last 2 days for spots and last month for WWV data).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/merge.pl){ .md-button }

## Verify on a running node

```text
HELP MERGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.