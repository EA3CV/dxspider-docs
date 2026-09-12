# `SHOW/RBN`

<div class="command-hero" markdown>

**Show which connected users want RBN spots**

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
SHOW/RBN [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXChannel::get_all_users()`, `dbm->seq()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/rbn.pl` · SHA-256 `31550695559d9bbcb1f1c2b105200a84429b7b9ea7785212ef96b95f10cb01ee`

```perl
L12: my ($self, $line) = @_;
L15: my @call = map {uc $_} split /\s+/, $line;
L23: shift @call;
L27: if ($data =~ /"sort":"[UW]"/ && $data =~ /"wantrbn":1/) {
```

### Validation and access evidence

Source: `cmd/show/rbn.pl` · SHA-256 `31550695559d9bbcb1f1c2b105200a84429b7b9ea7785212ef96b95f10cb01ee`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 1;
L26: if (is_callsign($key)) {
L27: if ($data =~ /"sort":"[UW]"/ && $data =~ /"wantrbn":1/) {
L51: return (1, @out, $self->msg('rec', $count));
```

### Output and error evidence

Source: `cmd/show/rbn.pl` · SHA-256 `31550695559d9bbcb1f1c2b105200a84429b7b9ea7785212ef96b95f10cb01ee`

```perl
L13: return (1, $self->msg('e5')) unless $self->priv >= 1;
L34: push @out, join(' ', $self->msg('rbnusers'), $main::mycall);
L40: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L47: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L51: return (1, @out, $self->msg('rec', $count));
```

### Message keys returned

`e5`, `rbnusers`, `rec`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/RBN [<callsign> ...]
    ```

    **Show which connected users want RBN spots**


=== "Help variant"

    ```text
    SHOW/RBN ALL
    ```

    **Show ALL users that want RBN spots**

    Show a list of the users that want RBN spots of any the callsigns
    specified on the command line. If no callsigns are specified then a
    sorted list of all connected users wanting RBN spots will be displayed

    SHOW/RBN ALL

    will go through the user file and display ALL users that want RBN spots.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/rbn.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/RBN
```

Compare the installed handler with this page when local overrides or a different revision may be present.