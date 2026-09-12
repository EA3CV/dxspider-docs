# `CLEAR/RBN`

<div class="command-hero" markdown>

**clear filters commands**

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
CLEAR/RBN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`DXUser::get()`, `Filter::delete()`, `Filter::read_in()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/clear/rbn.pl` · SHA-256 `16485262f963d54f706e756ec5466102ca092f018a06b471147b9efbd7b4113b`

```perl
L8: my ($self, $line) = @_;
L9: my @f = split /\s+/, $line;
L19: $f = uc shift @f;
L23: $call = lc shift @f;
L26: shift @f;
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Validation and access evidence

Source: `cmd/clear/rbn.pl` · SHA-256 `16485262f963d54f706e756ec5466102ca092f018a06b471147b9efbd7b4113b`

```perl
L17: if ($self->priv >= 8) {
L18: if (@f && is_callsign(uc $f[0])) {
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Output and error evidence

Source: `cmd/clear/rbn.pl` · SHA-256 `16485262f963d54f706e756ec5466102ca092f018a06b471147b9efbd7b4113b`

```perl
L36: push @out, $self->msg('filter4', $flag, $sort, $fno, $call);
L37: return (1, @out);
```

### Message keys returned

`filter4`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/clear/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/RBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.