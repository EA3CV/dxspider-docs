# `UNSET/USSTATE`

<div class="command-hero" markdown>

**Stop US State info on the end of DX announcements**

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
UNSET/USSTATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantusstate()`

### Argument parsing evidence

Source: `cmd/unset/usstate.pl` · SHA-256 `1d23975c932f33c1c9ae25fc66d110bd7c38c02f1505b741c9d89bbea55be8b7`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, $line;
L16: @args = $self->call if (!@args || $self->priv < 9);
L18: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/usstate.pl` · SHA-256 `1d23975c932f33c1c9ae25fc66d110bd7c38c02f1505b741c9d89bbea55be8b7`

```perl
L14: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
L16: @args = $self->call if (!@args || $self->priv < 9);
```

### Output and error evidence

Source: `cmd/unset/usstate.pl` · SHA-256 `1d23975c932f33c1c9ae25fc66d110bd7c38c02f1505b741c9d89bbea55be8b7`

```perl
L14: return (1, $self->msg('db3', 'FCC USDB')) unless $USDB::present;
L24: push @out, $self->msg('usstateu', $call);
L26: push @out, $self->msg('e3', "Unset US State", $call);
L29: return (1, @out);
```

### Message keys returned

`db3`, `e3`, `usstateu`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/USSTATE
```

**Stop US State info on the end of DX announcements**

## Details

If the spotter's or spotted's US State is known it is output on the
end of a DX announcement (there is just enough room).

A spotter's state will appear on the RHS of the time (like
SET/DXGRID) and the spotted's State will appear on the LHS of the
time field. Any information found will override any locator
information from SET/DXGRID.

Some user programs cannot cope with this. You can use this command
to reset (or set) this feature.

Conflicts with: SET/DXCQ, SET/DXITU

Do a STAT/USER to see which flags you have set if you are confused.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/usstate.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/USSTATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.