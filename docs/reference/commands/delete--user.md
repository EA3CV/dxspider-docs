# `DELETE/USER`

<div class="command-hero" markdown>

**Delete this user from the User Database**

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
DELETE/USER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXChannel::get()`, `DXUser::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/delete/user.pl` · SHA-256 `404acbdc359e7b662b619bbcf099cdddc63d201e2a7261e2548767045782d962`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L19: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/delete/user.pl` · SHA-256 `404acbdc359e7b662b619bbcf099cdddc63d201e2a7261e2548767045782d962`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/delete/user.pl` · SHA-256 `404acbdc359e7b662b619bbcf099cdddc63d201e2a7261e2548767045782d962`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9;
L23: push @out, $self->msg('nodee1', $call);
L28: push @out, $self->msg('deluser', $call);
L29: Log('DXCommand', $self->msg('deluser', $call));
L31: push @out, $self->msg('e3', "Delete/User", $call);
L35: return (1, @out);
```

### Message keys returned

`deluser`, `e3`, `e5`, `nodee1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DELETE/USER <callsign> ...
```

**Delete this user from the User Database**

## Details

This command will completely remove a one or more users from the database.

There is NO SECOND CHANCE.

It goes without saying that you should use this command CAREFULLY!

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/delete/user.pl){ .md-button }

## Verify on a running node

```text
HELP DELETE/USER
```

Compare the installed handler with this page when local overrides or a different revision may be present.