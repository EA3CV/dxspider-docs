# `SET/USERVAR`

<div class="command-hero" markdown>

**set any variable in the User file This is a hack - use the UTMOST CAUTION!!!!!!!! set it (dates and silly things like that can come later)**

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
SET/USERVAR [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Observable implementation effects

- Persists a DXUser record with `put()`.

### Important calls

`DXUser::get_current()`, `ref->field_prompt()`, `ref->put()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/uservar.pl` · SHA-256 `3dde2b3964f4c78ea66c9c5f5af56f81da35d1f71adf404cb1c792b73ad5232c`

```perl
L10: my ($self, $line) = @_;
L12: my @args = split /\s+/, $line;
L13: return (1, $self->msg('suser1')) if @args < 3;
```

### Validation and access evidence

Source: `cmd/set/uservar.pl` · SHA-256 `3dde2b3964f4c78ea66c9c5f5af56f81da35d1f71adf404cb1c792b73ad5232c`

```perl
L13: return (1, $self->msg('suser1')) if @args < 3;
L21: return (1, $self->msg('suser2', $call)) unless $ref;
L22: return (1, $self->msg('suser4', $field)) unless $ref->field_prompt($field);
L27: if ($self->priv < 9 || $self->remotecmd || $self->inscript) {
```

### Output and error evidence

Source: `cmd/set/uservar.pl` · SHA-256 `3dde2b3964f4c78ea66c9c5f5af56f81da35d1f71adf404cb1c792b73ad5232c`

```perl
L13: return (1, $self->msg('suser1')) if @args < 3;
L21: return (1, $self->msg('suser2', $call)) unless $ref;
L22: return (1, $self->msg('suser4', $field)) unless $ref->field_prompt($field);
L29: push @out, $self->msg('sorry');
L36: push @out, $self->msg('suser3', $field, $oldvalue, $value);
L37: push @out, print_all_fields($self, $ref, "User Information $call");
L39: return (1, @out);
```

### Message keys returned

`sorry`, `suser1`, `suser2`, `suser3`, `suser4`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/uservar.pl){ .md-button }

## Verify on a running node

```text
HELP SET/USERVAR
```

Compare the installed handler with this page when local overrides or a different revision may be present.