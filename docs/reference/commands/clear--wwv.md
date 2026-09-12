# `CLEAR/WWV`

<div class="command-hero" markdown>

**Clear a WWV filter line**

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
CLEAR/WWV [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`DXUser::get()`, `Filter::delete()`, `Filter::read_in()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/clear/wwv.pl` · SHA-256 `04dc7faba5e3060284d018653fb05a76132b9b49223b730944ef593339167dca`

```perl
L8: my ($self, $line) = @_;
L9: my @f = split /\s+/, $line;
L19: $f = uc shift @f;
L23: $call = lc shift @f;
L26: shift @f;
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Validation and access evidence

Source: `cmd/clear/wwv.pl` · SHA-256 `04dc7faba5e3060284d018653fb05a76132b9b49223b730944ef593339167dca`

```perl
L17: if ($self->priv >= 8) {
L18: if (@f && is_callsign(uc $f[0])) {
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Output and error evidence

Source: `cmd/clear/wwv.pl` · SHA-256 `04dc7faba5e3060284d018653fb05a76132b9b49223b730944ef593339167dca`

```perl
L36: push @out, $self->msg('filter4', $flag, $sort, $fno, $call);
L37: return (1, @out);
```

### Message keys returned

`filter4`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    CLEAR/WWV [1|all]
    ```

    **Clear a WWV filter line**

    This command allows you to clear (remove) a line in a WWV filter or to
    remove the whole filter.

    see CLEAR/SPOTS for a more detailed explanation.

=== "Help variant"

    ```text
    CLEAR/WWV <callsign> [input] [0-9|all]
    ```

    **Clear a WWV filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/clear/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP CLEAR/WWV
```

Compare the installed handler with this page when local overrides or a different revision may be present.