# `TESTBADIP`

<div class="command-hero" markdown>

**set list of bad dx nodes are we permitted?**

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
TESTBADIP [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`DXCIDR::find()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/testbadip.pl` · SHA-256 `a51f496bb9fab2785d25b260957098cc5c073faf740d1ede7bf46677dd40dd31`

```perl
L8: my ($self, $line) = @_;
L16: my @in = split /\s+/, $line;
L18: if ($in[0] =~ /^[_\d\w]+$/) {
L19: $suffix = shift @in;
```

### Validation and access evidence

Source: `cmd/testbadip.pl` · SHA-256 `a51f496bb9fab2785d25b260957098cc5c073faf740d1ede7bf46677dd40dd31`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L18: if ($in[0] =~ /^[_\d\w]+$/) {
```

### Output and error evidence

Source: `cmd/testbadip.pl` · SHA-256 `a51f496bb9fab2785d25b260957098cc5c073faf740d1ede7bf46677dd40dd31`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L12: return (1, q{Please install Net::CIDR::Lite or libnet-cidr-lite-perl to use this command}) unless $DXCIDR::active;
L21: return (1, "testbadip: need [suffix (def: local])] IP, IP-IP or IP/24") unless @in;
L25: push @out, "set/badip: '$ip' is not an ip address, ignored";
L33: return (1, $list);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/testbadip.pl){ .md-button }

## Verify on a running node

```text
HELP TESTBADIP
```

Compare the installed handler with this page when local overrides or a different revision may be present.