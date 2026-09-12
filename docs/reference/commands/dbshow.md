# `DBSHOW`

<div class="command-hero" markdown>

**Display an entry, if it exists, in a database**

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
DBSHOW [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXChannel::get()`, `DXDb::getdesc()`, `DXDb::newstream()`, `DXProt::pc44()`, `DXProt::route()`, `Route::Node::get()`, `db->getkey()`, `db->print()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/dbshow.pl` · SHA-256 `f95df470b5d4751b15c696e82c4b5f769d31cf331aaeb79c30efbff14e138a5d`

```perl
L7: my ($self, $line) = @_;
L8: my @f = split /\s+/, $line;
L11: my $name = shift @f if @f;
L51: push @out, split /\n/, $value;
```

### Validation and access evidence

Source: `cmd/dbshow.pl` · SHA-256 `f95df470b5d4751b15c696e82c4b5f769d31cf331aaeb79c30efbff14e138a5d`

```perl
L13: return (1, $self->msg('db3', $name)) unless $db;
L22: return (1, $self->msg('db3', $n)) unless $db;
L44: push @out, $pre if defined $pre;
```

### Output and error evidence

Source: `cmd/dbshow.pl` · SHA-256 `f95df470b5d4751b15c696e82c4b5f769d31cf331aaeb79c30efbff14e138a5d`

```perl
L13: return (1, $self->msg('db3', $name)) unless $db;
L22: return (1, $self->msg('db3', $n)) unless $db;
L28: push @out, $self->msg('db4', uc $name, $db->remote);
L32: push @out, $self->msg('db11', $db->remote);
L44: push @out, $pre if defined $pre;
L47: push @out, $db->name . " $_";
L51: push @out, split /\n/, $value;
L54: push @out, $self->msg('db2', uc $_, uc $db->{name});
L59: push @out, $post if $post;
L65: return (1, @out);
```

### Message keys returned

`db11`, `db2`, `db3`, `db4`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DBSHOW <dbname> <key>
```

**Display an entry, if it exists, in a database**

## Details

This is the generic user interface to the database to the database system.
It is expected that the sysop will add an entry to the local Aliases file
so that users can use the more familiar AK1A style of enquiry such as:

```text
SH/BUCK G1TLH
```

but if he hasn't and the database really does exist (use DBAVAIL or
SHOW/COMMAND to find out) you can do the same thing with:

```text
DBSHOW buck G1TLH
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbshow.pl){ .md-button }

## Verify on a running node

```text
HELP DBSHOW
```

Compare the installed handler with this page when local overrides or a different revision may be present.