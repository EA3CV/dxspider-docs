# `REGISTER/REMOVE`

<div class="command-hero" markdown>

**register/remove.pl - Remove DXSpider registration for a callsign family SYSOP only. Usage:**

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
REGISTER/REMOVE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Named fields consumed by the parser

`call`, `note`

### Important calls

`DXReg::ready()`, `DXReg::remove_registration()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/register/remove.pl` · SHA-256 `45a36366f6e637916c1065f1dd50e23db124102d20d1dd24314830a8d235dd91`

```perl
L14: my ($self, $line) = @_;
L28: $line //= '';
L29: $line =~ s/^\s+//;
L30: $line =~ s/\s+$//;
L32: my ($call, $note) = split /\s+/, $line, 2;
```

### Validation and access evidence

Source: `cmd/register/remove.pl` · SHA-256 `45a36366f6e637916c1065f1dd50e23db124102d20d1dd24314830a8d235dd91`

```perl
L16: return (1, $self->msg('e5'))
L17: if $self->priv < 9;
L23: if ($self->remotecmd || $self->inscript) {
L25: return (1, $self->msg('e5'));
L39: ) unless defined $call && length $call;
L101: if defined $r->{note} && length $r->{note};
```

### Output and error evidence

Source: `cmd/register/remove.pl` · SHA-256 `45a36366f6e637916c1065f1dd50e23db124102d20d1dd24314830a8d235dd91`

```perl
L16: return (1, $self->msg('e5'))
L20: return (1, ' ', 'Registration subsystem is not enabled', ' ');
L25: return (1, $self->msg('e5'));
L34: return (
L66: return (1, ' ', $result, ' ');
L91: push @out, ' ';
L92: push @out, 'Registration removed:';
L93: push @out, sprintf('%16s %s', 'Record:', '#' . $r->{id} . ' - ' . $r->{call});
L94: push @out, sprintf('%16s %s', 'Status:', 'REMOVED');
L95: push @out, sprintf('%16s %s', 'Affected SSIDs:', $ssids);
L96: push @out, sprintf('%16s %d', 'DXUser records:', scalar @{ $result->{affected_calls} });
L97: push @out, sprintf('%16s %s', 'Disconnected:', $disconnected);
L98: push @out, sprintf('%16s %s', 'Processed by:', $r->{processed_by});
L100: push @out, sprintf('%16s %s', 'Note:', $r->{note})
L104: push @out, sprintf(
L111: push @out, ' ';
L113: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/register/remove.pl){ .md-button }

## Verify on a running node

```text
HELP REGISTER/REMOVE
```

Compare the installed handler with this page when local overrides or a different revision may be present.