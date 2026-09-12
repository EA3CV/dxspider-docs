# `REGISTER/REQUEST`

<div class="command-hero" markdown>

**register/request.pl - Create a DXSpider registration request Normal user: register/request <email> <EN|ES> [ssid-list]**

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
REGISTER/REQUEST [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`DXReg::create_request()`, `DXReg::ready()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/register/request.pl` · SHA-256 `3506bbf66368f641a678117c415253749415dfca48286f9530393417af2b903b`

```perl
L17: my ($self, $line) = @_;
L29: my @args = grep { length $_ } split /\s+/, ($line // '');
L35: unless @args >= 3;
L37: ($call, $email, $language, $ssid_spec) = @args;
L42: unless @args >= 2;
L44: ($email, $language, $ssid_spec) = @args;
L108: for my $part (split /,/, $spec) {
L109: if ($part =~ /^(\d+)-(\d+)$/) {
L116: } elsif ($part =~ /^\d+$/) {
```

### Validation and access evidence

Source: `cmd/register/request.pl` · SHA-256 `3506bbf66368f641a678117c415253749415dfca48286f9530393417af2b903b`

```perl
L24: if ($self->remotecmd || $self->inscript) {
L26: return (1, $self->msg('e5'));
L33: if ($self->priv >= 9) {
L104: return (1, []) unless defined $spec && length $spec;
L109: if ($part =~ /^(\d+)-(\d+)$/) {
```

### Output and error evidence

Source: `cmd/register/request.pl` · SHA-256 `3506bbf66368f641a678117c415253749415dfca48286f9530393417af2b903b`

```perl
L21: return (1, 'Registration subsystem is not enabled');
L26: return (1, $self->msg('e5'));
L34: return (1, 'Usage: register/request <call> <email> <EN|ES> [ssid-list]')
L41: return (1, 'Usage: register/request <email> <EN|ES> [ssid-list]')
L51: return (1, $ssids_or_error) unless $ssid_ok;
L73: return (1, $result);
L92: push @out, sprintf('Registration request #%d - %s', $r->{id}, $r->{call});
L93: push @out, "Email: $r->{email}";
L94: push @out, "Language: $r->{language}";
L95: push @out, "SSIDs: $ssid_text";
L96: push @out, 'Status: PENDING';
L98: return (1, @out);
L104: return (1, []) unless defined $spec && length $spec;
L112: return (0, "Invalid SSID range '$part'")
L119: return (0, "Invalid SSID specification '$part'");
L123: return (1, \@result);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/register/request.pl){ .md-button }

## Verify on a running node

```text
HELP REGISTER/REQUEST
```

Compare the installed handler with this page when local overrides or a different revision may be present.