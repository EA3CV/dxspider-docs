# `UNSET/WANTPC16`

<div class="command-hero" markdown>

**unset the want PC16 flag**

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
UNSET/WANTPC16 [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`DXUser::get_current()`, `self->msg()`, `user->wantpc16()`

### Argument parsing evidence

Source: `cmd/unset/wantpc16.pl` · SHA-256 `c632cce13ff5b8ceef4e36da134c0679ee7b7b9bab4be2d2557f37cafacdb43a`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/wantpc16.pl` · SHA-256 `c632cce13ff5b8ceef4e36da134c0679ee7b7b9bab4be2d2557f37cafacdb43a`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L17: return (1, $self->msg('e12')) unless is_callsign($call);
```

### Output and error evidence

Source: `cmd/unset/wantpc16.pl` · SHA-256 `c632cce13ff5b8ceef4e36da134c0679ee7b7b9bab4be2d2557f37cafacdb43a`

```perl
L14: return (1, $self->msg('e5')) if $self->priv < 9;
L17: return (1, $self->msg('e12')) unless is_callsign($call);
L23: push @out, $self->msg('wpc16u', $call);
L25: push @out, $self->msg('e3', "unset/wantpc16", $call);
L28: return (1, @out);
```

### Message keys returned

`e12`, `e3`, `e5`, `wpc16u`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/wantpc16.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/WANTPC16
```

Compare the installed handler with this page when local overrides or a different revision may be present.