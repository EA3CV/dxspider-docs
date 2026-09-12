# `UNSET/BUDDY`

<div class="command-hero" markdown>

**Remove this call from my buddy list**

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
UNSET/BUDDY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`, `user->buddies()`

### Argument parsing evidence

Source: `cmd/unset/buddy.pl` · SHA-256 `cac952fed0de1fd01f2d567d50c39afd1648e1fb11dda6ce31269251dd5a795f`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach my $call (@args) {
```

### Validation and access evidence

Source: `cmd/unset/buddy.pl` · SHA-256 `cac952fed0de1fd01f2d567d50c39afd1648e1fb11dda6ce31269251dd5a795f`

```perl
L17: push(@out, $self->msg('e22', $call)), next unless is_callsign($call);
```

### Output and error evidence

Source: `cmd/unset/buddy.pl` · SHA-256 `cac952fed0de1fd01f2d567d50c39afd1648e1fb11dda6ce31269251dd5a795f`

```perl
L17: push(@out, $self->msg('e22', $call)), next unless is_callsign($call);
L20: push @out, $self->msg('buddyu', $call);
L26: return (1, @out);
```

### Message keys returned

`buddyu`, `e22`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/BUDDY <call> [<call>..]
```

**Remove this call from my buddy list**

## Details

A notification message
is sent to you automatically if anybody on your buddy list logs in or
out of any node in this cluster.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/buddy.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/BUDDY
```

Compare the installed handler with this page when local overrides or a different revision may be present.