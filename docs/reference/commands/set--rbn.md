# `SET/RBN`

<div class="command-hero" markdown>

**Mark this call as an RBN node**

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
SET/RBN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXChannel::get()`, `DXUser->new()`, `DXUser::get()`, `self->msg()`, `user->homenode()`, `user->lockout()`, `user->priv()`, `user->put()`, `user->sort()`

### Argument parsing evidence

Source: `cmd/set/rbn.pl` · SHA-256 `8fea1fce059a944a357d43a9071eaf31d37116b4f1b8ece6d1bb80862113d399`

```perl
L10: my ($self, $line) = @_;
L11: my @args = split /\s+/, $line;
L19: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/rbn.pl` · SHA-256 `8fea1fce059a944a357d43a9071eaf31d37116b4f1b8ece6d1bb80862113d399`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 5;
L40: $user->priv(0) unless $user->priv;
```

### Output and error evidence

Source: `cmd/set/rbn.pl` · SHA-256 `8fea1fce059a944a357d43a9071eaf31d37116b4f1b8ece6d1bb80862113d399`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 5;
L22: push @out, $self->msg('e11', $call);
L26: push @out, $self->msg('e11', $call);
L31: push @out, $self->msg('nodee1', $call);
L42: push @out, $self->msg($create ? 'nodenc' : 'noden', $call);
L44: push @out, $self->msg('e3', "Set RBN", $call);
L48: return (1, @out);
```

### Message keys returned

`e11`, `e3`, `e5`, `nodee1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/RBN <call> ...
```

**Mark this call as an RBN node**

## Details

This will mark this callsign as a Reverse Beacon
Network client. It's not a node in the normal sense of that word
in DXSpider. But it will generate spots from the RBN/Skimmers and
will act like a specialised node just for RBN spots.

You will need to use this command to create your skimmer node
connections. Normally one per RBN port (7000, 7001) but, in principle
you could connect to any skimmer that uses the same spot format.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP SET/RBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.