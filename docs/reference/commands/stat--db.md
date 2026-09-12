# `STAT/DB`

<div class="command-hero" markdown>

**Show the status of a database**

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
STAT/DB [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXDb::getdesc()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/stat/db.pl` · SHA-256 `d5d003ecb630cba22ffe6c1c3f38956986d9cbe658d41d1801fd685772e5a0ba`

```perl
L7: my ($self, $line) = @_;
L8: my @list = split /\s+/, $line; # generate a list of msg nos
L12: return (1, $self->msg('m16')) if @list == 0;
L14: foreach my $name (@list) {
L21: push @out, "" if @list > 1;
```

### Validation and access evidence

Source: `cmd/stat/db.pl` · SHA-256 `d5d003ecb630cba22ffe6c1c3f38956986d9cbe658d41d1801fd685772e5a0ba`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 5;
L12: return (1, $self->msg('m16')) if @list == 0;
```

### Output and error evidence

Source: `cmd/stat/db.pl` · SHA-256 `d5d003ecb630cba22ffe6c1c3f38956986d9cbe658d41d1801fd685772e5a0ba`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 5;
L12: return (1, $self->msg('m16')) if @list == 0;
L19: push @out, $self->msg('db3', $name);
L21: push @out, "" if @list > 1;
L24: return (1, @out);
```

### Message keys returned

`db3`, `e5`, `m16`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
STAT/DB <dbname>
```

**Show the status of a database**

## Details

Show the internal status of a database descriptor.

Depending on your privilege level you will see more or less information.
This command is unlikely to be of much use to anyone other than a sysop.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/db.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/DB
```

Compare the installed handler with this page when local overrides or a different revision may be present.