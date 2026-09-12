# `REGISTER/SHOW`

<div class="command-hero" markdown>

**register/show.pl - Show DXSpider registration requests/history SYSOP only. Usage:**

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
REGISTER/SHOW [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`DXReg::get_history()`, `DXReg::get_request()`, `DXReg::list_pending()`, `DXReg::ready()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/register/show.pl` · SHA-256 `e6b6bddd5edc90f245dbe981984dcf377f7279784ebde5ed29b1c362ab56db28`

```perl
L12: my ($self, $line) = @_;
L27: $line //= '';
L28: $line =~ s/^\s+//;
L29: $line =~ s/\s+$//;
L31: if (!length $line) {
L50: if ($line =~ /^\d+$/) {
L51: my $r = DXReg::get_request($line);
L53: return (1, ' ', "Registration request #$line not found", ' ')
L64: my $call = uc $line;
```

### Validation and access evidence

Source: `cmd/register/show.pl` · SHA-256 `e6b6bddd5edc90f245dbe981984dcf377f7279784ebde5ed29b1c362ab56db28`

```perl
L15: return (1, $self->msg('e5'))
L16: if $self->priv < 9;
L22: if ($self->remotecmd || $self->inscript) {
L24: return (1, $self->msg('e5'));
L50: if ($line =~ /^\d+$/) {
L126: if defined $r->{email} && length $r->{email};
L128: if defined $r->{language} && length $r->{language};
L148: if (defined $r->{note} && length $r->{note}) {
```

### Output and error evidence

Source: `cmd/register/show.pl` · SHA-256 `e6b6bddd5edc90f245dbe981984dcf377f7279784ebde5ed29b1c362ab56db28`

```perl
L15: return (1, $self->msg('e5'))
L19: return (1, ' ', 'Registration subsystem is not enabled', ' ');
L24: return (1, $self->msg('e5'));
L36: return (1, ' ', 'No pending registration requests', ' ')
L39: push @out, ' ';
L40: push @out, 'Pending registration requests:';
L43: push @out, summary_line($r);
L46: push @out, ' ';
L47: return (1, @out);
L53: return (1, ' ', "Registration request #$line not found", ' ')
L56: push @out, ' ';
L57: push @out, 'Registration history for ' . $r->{call} . ':';
L58: push @out, format_request($r);
L59: push @out, ' ';
L61: return (1, @out);
L67: return (1, ' ', "No registration history for $call", ' ')
L74: push @out, ' ';
L75: push @out, "Registration history for $call:";
L78: push @out, format_request($history[$i]);
L79: push @out, ' ' if $i < $#history;
L82: push @out, ' ';
L83: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/register/show.pl){ .md-button }

## Verify on a running node

```text
HELP REGISTER/SHOW
```

Compare the installed handler with this page when local overrides or a different revision may be present.