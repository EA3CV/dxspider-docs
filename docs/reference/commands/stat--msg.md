# `STAT/MSG`

<div class="command-hero" markdown>

**Show the status of the message system**

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
STAT/MSG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::get()`, `DXMsg::get_all_busy()`, `DXMsg::get_all_fwq()`, `DXMsg::get_busy()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/stat/msg.pl` · SHA-256 `e2a1c55d9898ab0c8c3fef0569142bb86ca2e03a2a6bea0ef0aff66278276919`

```perl
L7: my ($self, $line) = @_;
L8: my @list = split /\s+/, $line; # generate a list of msg nos
L13: if (@list == 0) {
L38: foreach my $msgno (@list) {
L45: push @out, "" if @list > 1;
```

### Validation and access evidence

Source: `cmd/stat/msg.pl` · SHA-256 `e2a1c55d9898ab0c8c3fef0569142bb86ca2e03a2a6bea0ef0aff66278276919`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 1;
```

### Output and error evidence

Source: `cmd/stat/msg.pl` · SHA-256 `e2a1c55d9898ab0c8c3fef0569142bb86ca2e03a2a6bea0ef0aff66278276919`

```perl
L11: return (1, $self->msg('e5')) if $self->priv < 1;
L15: push @out, "Work Queue Keys";
L16: push @out, map { " $_" } sort (DXMsg::get_all_fwq());
L17: push @out, "Busy Queue Data";
L32: push @out, " $key/$tonode: $from -> $to msg: $msgno stream: $stream Count: $count Lines: $lines$lastt$waitt"
L34: push @out, " dangling ref for $key";
L43: push @out, $self->msg('m4', $msgno);
L45: push @out, "" if @list > 1;
L49: return (1, @out);
```

### Message keys returned

`e5`, `m4`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    STAT/MSG
    ```

    **Show the status of the message system**


=== "Help variant"

    ```text
    STAT/MSG <msgno>
    ```

    **Show the status of a message**

    This command shows the internal status of a message and includes information
    such as to whom it has been forwarded, its size, origin etc etc.

    If no message number is given then the status of the message system is
    displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/msg.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/MSG
```

Compare the installed handler with this page when local overrides or a different revision may be present.