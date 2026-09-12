# `SET/USER`

<div class="command-hero" markdown>

**Make the callsign a normal user**

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
SET/USER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `self->msg()`, `user->priv()`, `user->put()`, `user->sort()`

### Argument parsing evidence

Source: `cmd/set/user.pl` · SHA-256 `4354e401d6a08ed64347ed2c0eb74f097b0f564548c29ef9f41f204002161646`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/user.pl` · SHA-256 `4354e401d6a08ed64347ed2c0eb74f097b0f564548c29ef9f41f204002161646`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L31: return (1, $self->msg('usernf', $call)) if !$user;
```

### Output and error evidence

Source: `cmd/set/user.pl` · SHA-256 `4354e401d6a08ed64347ed2c0eb74f097b0f564548c29ef9f41f204002161646`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 5;
L23: push @out, $self->msg('e11', $call);
L28: push @out, $self->msg('nodee1', $call);
L31: return (1, $self->msg('usernf', $call)) if !$user;
L35: push @out, $self->msg('nodeu', $call);
L38: return (1, @out);
```

### Message keys returned

`e11`, `e5`, `nodee1`, `nodeu`, `usernf`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/USER <call> [<call>..]
```

**Make the callsign a normal user**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/user.pl){ .md-button }

## Verify on a running node

```text
HELP SET/USER
```

Compare the installed handler with this page when local overrides or a different revision may be present.