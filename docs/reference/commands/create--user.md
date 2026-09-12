# `CREATE/USER`

<div class="command-hero" markdown>

**Create this user from the User Database**

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
CREATE/USER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser->new()`, `DXUser::get()`, `self->msg()`, `user->homenode()`, `user->put()`, `user->sort()`

### Argument parsing evidence

Source: `cmd/create/user.pl` · SHA-256 `4931db4d5fdfdc4c8e445a93678e9f3d7484236a983ef3cbfbad3cfac8f01a36`

```perl
L11: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L20: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/create/user.pl` · SHA-256 `4931db4d5fdfdc4c8e445a93678e9f3d7484236a983ef3cbfbad3cfac8f01a36`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
```

### Output and error evidence

Source: `cmd/create/user.pl` · SHA-256 `4931db4d5fdfdc4c8e445a93678e9f3d7484236a983ef3cbfbad3cfac8f01a36`

```perl
L18: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
L28: push @out, $self->msg('creuser', $call);
L30: push @out, $self->msg('hasha', $call, 'Users');
L33: return (1, @out);
```

### Message keys returned

`creuser`, `e5`, `hasha`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
CREATE/USER <callsign> ...
```

**Create this user from the User Database**

## Details

This command will create one or more new users. None of the fields
like name, qth etc will be filled in. It is just a new entry in the user
database to which one can add more stuff like SET/PASSWORD or by SPOOF.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/create/user.pl){ .md-button }

## Verify on a running node

```text
HELP CREATE/USER
```

Compare the installed handler with this page when local overrides or a different revision may be present.