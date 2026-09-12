# `CLEAR/SPOTS`

<div class="command-hero" markdown>

**Remove one line or the complete DX spot filter.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Filtering</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
CLEAR/SPOTS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Reads or modifies filter state/files.

### Important calls

`DXUser::get_current()`, `Filter::delete()`, `Filter::read_in()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/clear/spots.pl` · SHA-256 `82f5e50bf6ef52f30a203c489f630071ce70e1a7fdd169c2856d23646f79e421`

```perl
L8: my ($self, $line) = @_;
L9: my @f = split /\s+/, $line;
L19: $f = uc shift @f;
L23: $call = lc shift @f;
L26: shift @f;
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Validation and access evidence

Source: `cmd/clear/spots.pl` · SHA-256 `82f5e50bf6ef52f30a203c489f630071ce70e1a7fdd169c2856d23646f79e421`

```perl
L17: if ($self->priv >= 8) {
L18: if (@f && is_callsign(uc $f[0])) {
L31: $fno = shift @f if @f && $f[0] =~ /^\d|all$/;
```

### Output and error evidence

Source: `cmd/clear/spots.pl` · SHA-256 `82f5e50bf6ef52f30a203c489f630071ce70e1a7fdd169c2856d23646f79e421`

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
    CLEAR/SPOTS [0-9|all]
    ```

    **Clear a spot filter line**

    This command allows you to clear (remove) a line in a spot filter or to
    remove the whole filter.

    If you have a filter:-

    ```text
    acc/spot 1 on hf/cw
    acc/spot 2 on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
    ```

    and you say:-

    ```text
    clear/spot 1
    ```

    you will be left with:-

    ```text
    acc/spot 2 on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
    ```

    If you do:

    ```text
    clear/spot all
    ```

    the filter will be completely removed.

=== "Help variant"

    ```text
    CLEAR/SPOTS <callsign> [input] [0-9|all]
    ```

    **Clear a spot filter line**

    A sysop can clear an input or normal output filter for a user or the
    node_default or user_default.

## Practical examples

### Remove line 1

```text
CLEAR/SPOTS 1
```

### Remove the complete filter

```text
CLEAR/SPOTS ALL
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/clear/spots.pl){ .md-button }

## Related commands

- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)
- [`SHOW/FILTER`](show--filter.md)

## Verify on a running node

```text
HELP CLEAR/SPOTS
```

Compare the installed handler with this page when local overrides or a different revision may be present.