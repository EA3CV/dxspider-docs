# `SET/BUDDY`

<div class="command-hero" markdown>

**Add this call to my buddy list**

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
SET/BUDDY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/set/buddy.pl` · SHA-256 `1e8f6c40b66d736601a1f6937db9f725a89ee3768087ada8209532162de530c6`

```perl
L9: my ($self, $line) = @_;
L10: my @args = split /\s+/, uc $line;
L16: foreach my $call (@args) {
```

### Validation and access evidence

Source: `cmd/set/buddy.pl` · SHA-256 `1e8f6c40b66d736601a1f6937db9f725a89ee3768087ada8209532162de530c6`

```perl
L17: push(@out, $self->msg('e22', $call)), next unless is_callsign($call);
```

### Output and error evidence

Source: `cmd/set/buddy.pl` · SHA-256 `1e8f6c40b66d736601a1f6937db9f725a89ee3768087ada8209532162de530c6`

```perl
L17: push(@out, $self->msg('e22', $call)), next unless is_callsign($call);
L20: push @out, $self->msg('buddya', $call);
L25: return (1, @out);
```

### Message keys returned

`buddya`, `e22`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/BUDDY <call> [<call>..]
```

**Add this call to my buddy list**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/buddy.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BUDDY
```

Compare the installed handler with this page when local overrides or a different revision may be present.