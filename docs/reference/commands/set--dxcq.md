# `SET/DXCQ`

<div class="command-hero" markdown>

**Show CQ Zones on the end of DX announcements**

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
SET/DXCQ [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantdxcq()`, `user->wantdxitu()`, `user->wantusstate()`

### Argument parsing evidence

Source: `cmd/set/dxcq.pl` · SHA-256 `16fa94f4389f0a9f45149d9a07254b7c099253ef4ea9831647bfc245249410fc`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/dxcq.pl` · SHA-256 `16fa94f4389f0a9f45149d9a07254b7c099253ef4ea9831647bfc245249410fc`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/set/dxcq.pl` · SHA-256 `16fa94f4389f0a9f45149d9a07254b7c099253ef4ea9831647bfc245249410fc`

```perl
L22: push @out, $self->msg('dxituu', $call);
L30: push @out, $self->msg('dxcqs', $call);
L32: push @out, $self->msg('e3', "Set DX CQ", $call);
L35: return (1, @out);
```

### Message keys returned

`dxcqs`, `dxituu`, `e3`, `usstateu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/DXCQ
```

**Show CQ Zones on the end of DX announcements**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/dxcq.pl){ .md-button }

## Verify on a running node

```text
HELP SET/DXCQ
```

Compare the installed handler with this page when local overrides or a different revision may be present.