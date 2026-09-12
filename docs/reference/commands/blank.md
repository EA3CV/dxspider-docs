# `BLANK`

<div class="command-hero" markdown>

**Print nn (default 1) blank lines (or strings)**

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
BLANK [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Argument parsing evidence

Source: `cmd/blank.pl` · SHA-256 `89438125769cd3a08b1a048a629aaa302cf4cd28ddf7b04e3b51a597fcf653ee`

```perl
L17: my ($self, $line) = @_;
L20: my @f = split /\s+/, $line;
L22: $data = shift @f;
L26: if (@f && $f[0] =~ /^\d+$/) {
L27: $lines = shift @f;
```

### Validation and access evidence

Source: `cmd/blank.pl` · SHA-256 `89438125769cd3a08b1a048a629aaa302cf4cd28ddf7b04e3b51a597fcf653ee`

```perl
L21: if (@f && $f[0] !~ /^\d+$/) {
L26: if (@f && $f[0] =~ /^\d+$/) {
```

### Output and error evidence

Source: `cmd/blank.pl` · SHA-256 `89438125769cd3a08b1a048a629aaa302cf4cd28ddf7b04e3b51a597fcf653ee`

```perl
L32: push @out, $data for (1..$lines);
L33: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
BLANK [<string>] [<nn>]
```

**Print nn (default 1) blank lines (or strings)**

## Details

In its basic form this command prints one or more blank lines. However if
you pass it a string it will replicate the string for the width of the
screen (default 80) and then print that one or more times, so:

```text
blank 2
```

prints two blank lines

```text
blank -
```

prints a row of - characters once.

```text
blank abc
```

prints 'abcabcabcabcabcabc....'

This is really only of any use in a script file and you can print a maximum
of 9 lines.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/blank.pl){ .md-button }

## Verify on a running node

```text
HELP BLANK
```

Compare the installed handler with this page when local overrides or a different revision may be present.