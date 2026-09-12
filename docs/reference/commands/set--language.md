# `SET/LANGUAGE`

<div class="command-hero" markdown>

**Set the language you want to use**

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
SET/LANGUAGE [text]
```

The complete argument line is used as one value without prior tokenization in this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Recognized tokens, keys or enumerated values in this handler

`cz`, `de`, `en`, `es`, `fr`, `it`, `nl`, `pt`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXUser::get_current()`, `self->lang()`, `self->msg()`, `user->lang()`, `user->put()`

### Argument parsing evidence

Source: `cmd/set/language.pl` · SHA-256 `1c7eb9308820fcb8375fe3d7281d5f178c32d17e99cca8f4922bfcc74f408f49`

```perl
L9: my ($self, $line) = @_;
L17: $line =~ s/^\s+//;
L18: $line =~ s/\s+$//;
L20: return (1, $self->msg('lange1', join(',', @lang))) if !$line;
L21: $line = lc $line;
L22: return (1, $self->msg('lange1', join(',', @lang))) unless grep $_ eq $line, @lang;
L27: $user->lang($line);
L29: $self->lang($line);
L30: return (1, $self->msg('lang', $line));
```

### Validation and access evidence

Source: `cmd/set/language.pl` · SHA-256 `1c7eb9308820fcb8375fe3d7281d5f178c32d17e99cca8f4922bfcc74f408f49`

```perl
L20: return (1, $self->msg('lange1', join(',', @lang))) if !$line;
L22: return (1, $self->msg('lange1', join(',', @lang))) unless grep $_ eq $line, @lang;
L30: return (1, $self->msg('lang', $line));
L32: return (1, $self->msg('lange2', $call));
```

### Output and error evidence

Source: `cmd/set/language.pl` · SHA-256 `1c7eb9308820fcb8375fe3d7281d5f178c32d17e99cca8f4922bfcc74f408f49`

```perl
L20: return (1, $self->msg('lange1', join(',', @lang))) if !$line;
L22: return (1, $self->msg('lange1', join(',', @lang))) unless grep $_ eq $line, @lang;
L30: return (1, $self->msg('lang', $line));
L32: return (1, $self->msg('lange2', $call));
```

### Message keys returned

`lang`, `lange1`, `lange2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/LANGUAGE <lang>
```

**Set the language you want to use**

## Details

You can select the language that you want the cluster to use. Currently
the languages available are en (English), de (German), es (Spanish),
Czech (cz), French (fr), Portuguese (pt), Italian (it) and nl (Dutch).

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/language.pl){ .md-button }

## Verify on a running node

```text
HELP SET/LANGUAGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.