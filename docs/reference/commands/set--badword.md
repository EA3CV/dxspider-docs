# `SET/BADWORD`

<div class="command-hero" markdown>

**Stop things like this word being propagated**

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
SET/BADWORD [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`BadWords::add_regex()`, `BadWords::check()`, `BadWords::generate_regex()`, `BadWords::put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/badword.pl` · SHA-256 `03351e91a8adf8fa89fdec4c32ce4c6e5fe207c657015d3030469b56e4a13942`

```perl
L8: my ($self, $line) = @_;
L12: my @words = split /\s+/, uc $line;
```

### Validation and access evidence

Source: `cmd/set/badword.pl` · SHA-256 `03351e91a8adf8fa89fdec4c32ce4c6e5fe207c657015d3030469b56e4a13942`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
```

### Output and error evidence

Source: `cmd/set/badword.pl` · SHA-256 `03351e91a8adf8fa89fdec4c32ce4c6e5fe207c657015d3030469b56e4a13942`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L19: push @out, "BadWord $w already matched by '$in[0]', ignored";
L22: push @out, "BadWord $w added as '$in[0]'";
L30: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/BADWORD <word>..
```

**Stop things like this word being propagated**

## Details

Setting a word as a 'badword' will prevent things like spots,
announces or talks with this word in the the text part from going any
further. They will not be displayed and they will not be sent onto
other nodes.

This has changed its meaning from the master release. All words entered
are reduced to the minimum regex that will match words starting like
this one:

```text
set/badword annihilate
```

will stop anything that starts with these words in the text
like this:

```text
annihilate annihilated
```

but it will also stop things like this:

```text
anihilate annni11ihhh ii lllattt eee
```

A few common 'leet' substitutions are automatically matched:

```text
b0ll0cks bo0lll0ccckks fr1iigging
```

and so on

It will not stop some things like:

```text
The base word FRIG will stop 'friiigging' but not 'friiig ging'
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/badword.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BADWORD
```

Compare the installed handler with this page when local overrides or a different revision may be present.