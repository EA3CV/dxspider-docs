# `CLEAR/DUPEFILE`

<div class="command-hero" markdown>

**Clear out the dupefile completely**

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
CLEAR/DUPEFILE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXDupe::finish()`, `DXDupe::init()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/clear/dupefile.pl` · SHA-256 `052c1b30a0babfc82c37499e1402425f875da58dfca0c1cba65348982b99263e`

```perl
L8: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/clear/dupefile.pl` · SHA-256 `052c1b30a0babfc82c37499e1402425f875da58dfca0c1cba65348982b99263e`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L16: return (1, $self->msg('done'));
```

### Output and error evidence

Source: `cmd/clear/dupefile.pl` · SHA-256 `052c1b30a0babfc82c37499e1402425f875da58dfca0c1cba65348982b99263e`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L16: return (1, $self->msg('done'));
```

### Message keys returned

`done`, `e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
CLEAR/DUPEFILE
```

**Clear out the dupefile completely**

## Details

The system maintains a list of duplicate announces and spots (amongst many
other things). Sometimes this file gets corrupted during operation
(although not very often). This command will remove the file and start
again from scratch.

Try this if you get several duplicate DX Spots, one after another.

Please ONLY use this command if you have a problem. And then only once.
If it does not cure your problem, then repeating the command won't help.
Get onto the dxspider-support list and let us try to help.

If you use this command frequently then you will cause other people, as
well as yourself, a lot of problems with duplicates.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/clear/dupefile.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/DUPEFILE
```

Compare the installed handler with this page when local overrides or a different revision may be present.