# `SHOW/FILTER`

<div class="command-hero" markdown>

**Show the contents of all the filters you have set**

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
SHOW/FILTER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Recognized tokens, keys or enumerated values in this handler

`ann`, `rbn`, `route`, `spots`, `wcy`, `wwv`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`Filter::read_in()`, `ref->print()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/filter.pl` · SHA-256 `aecb7f9380bea8c261afa041c798e8ef75ba9901fb0953c4d90f4d65a5c912bf`

```perl
L8: my ($self, $line) = @_;
L9: my @f = split /\s+/, $line;
L16: $call = uc shift @f;
L19: $call = shift @f;
```

### Validation and access evidence

Source: `cmd/show/filter.pl` · SHA-256 `aecb7f9380bea8c261afa041c798e8ef75ba9901fb0953c4d90f4d65a5c912bf`

```perl
L14: if (is_callsign(uc $f[0])) {
L15: return (1, $self->msg('e5')) unless $self->priv >= 1;
L18: return (1, $self->msg('e5')) unless $self->priv >= 1;
```

### Output and error evidence

Source: `cmd/show/filter.pl` · SHA-256 `aecb7f9380bea8c261afa041c798e8ef75ba9901fb0953c4d90f4d65a5c912bf`

```perl
L15: return (1, $self->msg('e5')) unless $self->priv >= 1;
L18: return (1, $self->msg('e5')) unless $self->priv >= 1;
L33: push @out, $ref->print($call, $sort, "input") if $ref;
L35: push @out, $ref->print($call, $sort, "") if $ref;
L37: push @out, $self->msg('filter3', $call) unless @out;
L38: return (1, @out);
```

### Message keys returned

`e5`, `filter3`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/FILTER
```

**Show the contents of all the filters you have set**

## Details

Show the contents of all the filters that are set. This command displays
all the filters set - for all the various categories.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/filter.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/FILTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.