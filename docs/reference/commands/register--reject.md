# `REGISTER/REJECT`

<div class="command-hero" markdown>

**register/reject.pl - Reject a DXSpider registration request SYSOP only. Usage:**

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
REGISTER/REJECT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Named fields consumed by the parser

`target`, `note`

### Important calls

`DXReg::ready()`, `DXReg::reject_request()`, `DXReg::resolve_pending_request()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/register/reject.pl` · SHA-256 `70516d432b977316bb14929f2cc0b03cb2bb87a04c8c9a814a53c9d8deda8206`

```perl
L10: my ($self, $line) = @_;
L24: $line //= '';
L25: $line =~ s/^\s+//;
L26: $line =~ s/\s+$//;
L28: my ($target, $note) = split /\s+/, $line, 2;
```

### Validation and access evidence

Source: `cmd/register/reject.pl` · SHA-256 `70516d432b977316bb14929f2cc0b03cb2bb87a04c8c9a814a53c9d8deda8206`

```perl
L12: return (1, $self->msg('e5'))
L13: if $self->priv < 9;
L19: if ($self->remotecmd || $self->inscript) {
L21: return (1, $self->msg('e5'));
L35: ) unless defined $target && length $target;
L87: if defined $r->{note} && length $r->{note};
```

### Output and error evidence

Source: `cmd/register/reject.pl` · SHA-256 `70516d432b977316bb14929f2cc0b03cb2bb87a04c8c9a814a53c9d8deda8206`

```perl
L12: return (1, $self->msg('e5'))
L16: return (1, ' ', 'Registration subsystem is not enabled', ' ');
L21: return (1, $self->msg('e5'));
L30: return (
L40: return (1, ' ', $request_or_error, ' ')
L63: return (1, ' ', $result, ' ');
L80: push @out, ' ';
L81: push @out, 'Registration rejected:';
L82: push @out, sprintf('%16s %s', 'Request:', '#' . $r->{id} . ' - ' . $r->{call});
L83: push @out, sprintf('%16s %s', 'Status:', 'REJECTED');
L84: push @out, sprintf('%16s %s', 'Processed by:', $r->{processed_by});
L86: push @out, sprintf('%16s %s', 'Note:', $r->{note})
L89: push @out, ' ';
L91: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/register/reject.pl){ .md-button }

## Verify on a running node

```text
HELP REGISTER/REJECT
```

Compare the installed handler with this page when local overrides or a different revision may be present.