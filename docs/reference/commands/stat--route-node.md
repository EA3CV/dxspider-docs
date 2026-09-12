# `STAT/ROUTE_NODE`

<div class="command-hero" markdown>

**Show the data in a Route::Node object**

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
STAT/ROUTE_NODE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Route::Node::get()`, `Route::Node::get_all()`

### Argument parsing evidence

Source: `cmd/stat/route_node.pl` · SHA-256 `ac60b82a96676e073ee16ee1d2b5b5122eeaf271d57f2880171beeb1cb06c84a`

```perl
L9: my ($self, $line) = @_;
L11: my @list = split /\s+/, $line; # generate a list of callsigns
L12: @list = ($self->call) unless @list; # my channel if no callsigns
L13: if ($self->priv > 5 && @list && uc $list[0] eq 'ALL') {
L15: @list = sort map {$_->call} Route::Node::get_all();
L16: my $count = @list;
L19: while (@list > $n) {
L20: push @out, join(' ', map {sprintf "%9s",$_ } splice(@list, 0, $n));
L22: push @out, join(' ', map {sprintf "%9s",$_ } @list) if @list;
L28: foreach $call (@list) {
L36: push @out, "" if @list > 1;
```

### Validation and access evidence

Source: `cmd/stat/route_node.pl` · SHA-256 `ac60b82a96676e073ee16ee1d2b5b5122eeaf271d57f2880171beeb1cb06c84a`

```perl
L13: if ($self->priv > 5 && @list && uc $list[0] eq 'ALL') {
```

### Output and error evidence

Source: `cmd/stat/route_node.pl` · SHA-256 `ac60b82a96676e073ee16ee1d2b5b5122eeaf271d57f2880171beeb1cb06c84a`

```perl
L14: push @out, "Node Callsigns in Routing Table";
L20: push @out, join(' ', map {sprintf "%9s",$_ } splice(@list, 0, $n));
L22: push @out, join(' ', map {sprintf "%9s",$_ } @list) if @list;
L23: push @out, "$count Nodes";
L24: return (1, @out);
L34: push @out, "Route::Node: $call not found";
L36: push @out, "" if @list > 1;
L39: return (1, @out);
```

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    STAT/ROUTE_NODE <callsign>
    ```

    **Show the data in a Route::Node object**


=== "Help variant"

    ```text
    STAT/ROUTE_NODE all
    ```

    **Show list of all Route::Node objects**


## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/route_node.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/ROUTE_NODE
```

Compare the installed handler with this page when local overrides or a different revision may be present.