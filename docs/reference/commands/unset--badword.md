# `UNSET/BADWORD`

<div class="command-hero" markdown>

**Propagate things like this word again**

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
UNSET/BADWORD [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`BadWords::check()`, `BadWords::del_regex()`, `BadWords::generate_regex()`, `BadWords::put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/badword.pl` · SHA-256 `facb4751744fdfcb61668a60c645d19a3324f93d96c7d1feca37f7126f60530f`

```perl
L8: my ($self, $line) = @_;
L13: my @words = split /\s+/, uc $line;
```

### Validation and access evidence

Source: `cmd/unset/badword.pl` · SHA-256 `facb4751744fdfcb61668a60c645d19a3324f93d96c7d1feca37f7126f60530f`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
```

### Output and error evidence

Source: `cmd/unset/badword.pl` · SHA-256 `facb4751744fdfcb61668a60c645d19a3324f93d96c7d1feca37f7126f60530f`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L20: push @out, "BadWord $w not defined, ignored";
L23: push @out, "BadWord $w removed";
L31: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BADWORD <word>..
```

**Propagate things like this word again**

## Details

This is the opposite of set/badword <word>

```text
unset/badword fred
```

will allow text with this word again (if it has been set as a bad word.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/badword.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BADWORD
```

Compare the installed handler with this page when local overrides or a different revision may be present.