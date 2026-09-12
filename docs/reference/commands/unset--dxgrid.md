# `UNSET/DXGRID`

<div class="command-hero" markdown>

**Stop QRA Grid Squares on the end of DX announcements**

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
UNSET/DXGRID [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantgrid()`

### Argument parsing evidence

Source: `cmd/unset/dxgrid.pl` · SHA-256 `d9a23e8c89b4872442a9d018b9cc5a7116ddda01a0b295f48216c01dbc3e46fc`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L14: @args = $self->call if (!@args || $self->priv < 9);
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/dxgrid.pl` · SHA-256 `d9a23e8c89b4872442a9d018b9cc5a7116ddda01a0b295f48216c01dbc3e46fc`

```perl
L14: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/unset/dxgrid.pl` · SHA-256 `d9a23e8c89b4872442a9d018b9cc5a7116ddda01a0b295f48216c01dbc3e46fc`

```perl
L22: push @out, $self->msg('gridu', $call);
L24: push @out, $self->msg('e3', "Unset Grid", $call);
L27: return (1, @out);
```

### Message keys returned

`e3`, `gridu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/DXGRID
```

**Stop QRA Grid Squares on the end of DX announcements**

## Details

A standard feature which is enabled in version 1.43 and above is
that if the spotter's grid square is known it is output on the end
of a DX announcement (there is just enough room). Some user programs
cannot cope with this. You can use this command to reset (or set)
this feature.

Conflicts with: SET/DXCQ, SET/DXITU

Do a STAT/USER to see which flags you have set if you are confused.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/dxgrid.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/DXGRID
```

Compare the installed handler with this page when local overrides or a different revision may be present.