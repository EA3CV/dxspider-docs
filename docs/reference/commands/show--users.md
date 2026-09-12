# `SHOW/USERS`

<div class="command-hero" markdown>

**show the users on this cluster from the routing tables**

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
SHOW/USERS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`, `Route::User::get()`, `Route::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/users.pl` · SHA-256 `76359544277a655a454f60253cb840577307eb943838f873e47a5ba9f4c4fd46`

```perl
L9: my ($self, $line) = @_;
L10: my @list = map { uc } split /\s+/, $line; # list of callsigns of nodes
L13: if (@list) {
L14: foreach my $call (sort @list) {
```

### Output and error evidence

Source: `cmd/show/users.pl` · SHA-256 `76359544277a655a454f60253cb840577307eb943838f873e47a5ba9f4c4fd46`

```perl
L24: push @out, "$call $route $name $qth $qra",
L26: push @out, $self->msg('usernf', $call);
L31: push @out, join(' ', $self->msg('userconn'), $main::mycall);
L37: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L50: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L53: return (1, @out);
```

### Message keys returned

`userconn`, `usernf`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/users.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/USERS
```

Compare the installed handler with this page when local overrides or a different revision may be present.