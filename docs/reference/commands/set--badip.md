# `SET/BADIP`

<div class="command-hero" markdown>

**Stop logins and spots with this IP address**

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
SET/BADIP [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`DXCIDR::add()`, `DXCIDR::append()`, `DXCIDR::clean_prep()`, `DXCIDR::find()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/set/badip.pl` · SHA-256 `ec246ffc05cff066cdeddb5261a89a0e7102b93924b588736e331df481bc5c2e`

```perl
L8: my ($self, $line) = @_;
L16: my @in = split /\s+/, $line;
L18: if ($in[0] =~ /^[_\d\w]+$/) {
L19: $suffix = shift @in;
```

### Validation and access evidence

Source: `cmd/set/badip.pl` · SHA-256 `ec246ffc05cff066cdeddb5261a89a0e7102b93924b588736e331df481bc5c2e`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L18: if ($in[0] =~ /^[_\d\w]+$/) {
```

### Output and error evidence

Source: `cmd/set/badip.pl` · SHA-256 `ec246ffc05cff066cdeddb5261a89a0e7102b93924b588736e331df481bc5c2e`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L12: return (1, q{Please install Net::CIDR::Lite or libnet-cidr-lite-perl to use this command}) unless $DXCIDR::active;
L21: return (1, "set/badip: need [suffix (def: local])] IP, IP-IP or IP/24") unless @in;
L25: push @out, "set/badip: '$ip' is not an ip address, ignored";
L29: return (1, "set/badip: $ip $@") if $@;
L31: push @out, "set/badip: $ip exists, not added";
L43: push @out, "set/badip: added $count entries to badip.$suffix : '$list'";
L45: push @out, "set/badip: No valid IPs, not updating badip.$suffix with '$list'";
L47: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SET/BADIP <ip address>..
```

**Stop logins and spots with this IP address**

## Details

This command will prevent logins to this node from this IP address.
It will also drop spots (PC61) from this address thus preventing them
from being propagated.

```text
set/badip 217.61.58.23
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/badip.pl){ .md-button }

## Verify on a running node

```text
HELP SET/BADIP
```

Compare the installed handler with this page when local overrides or a different revision may be present.