# `LOAD/BADWORDS`

<div class="command-hero" markdown>

**Reload the bad words table**

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
LOAD/BADWORDS
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`BadWords::load()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/badwords.pl` · SHA-256 `eae80456a0cada084821e19a9a0487613787abea2e4c6d8f323c243901944b5f`

```perl
L2: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/badwords.pl` · SHA-256 `eae80456a0cada084821e19a9a0487613787abea2e4c6d8f323c243901944b5f`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/badwords.pl` · SHA-256 `eae80456a0cada084821e19a9a0487613787abea2e4c6d8f323c243901944b5f`

```perl
L4: return (1, $self->msg('e5')) if $self->priv < 9;
L5: push @out, (BadWords::load());
L6: @out = ($self->msg('ok')) unless @out;
L7: return (1, @out);
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/BADWORDS
```

**Reload the bad words table**

## Details

Reload the /spider/data/badwords file if you have changed it manually whilst
the cluster is running. This file contains a list of words which, if found
on certain text portions of PC protocol, will cause those protocol frames
to be rejected. It will all put out a message if any of these words are
used on the announce, dx and talk commands. The words can be one or
more on a line, lines starting with '#' are ignored.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/badwords.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BADWORDS
```

Compare the installed handler with this page when local overrides or a different revision may be present.