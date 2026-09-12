# `SHOW/BADIP`

<div class="command-hero" markdown>

**show (or find) list of bad dx nodes are we permitted? $DB::single = 1;**

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
SHOW/BADIP [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`DXCIDR::find()`, `DXCIDR::list()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/badip.pl` · SHA-256 `b2bddef8f064452a63df909e0863a06f73091dd8245f39158b3c21015e2aac41`

```perl
L8: my ($self, $line) = @_;
L16: my @in = split /\s+/, $line;
L36: my @list = map {my $s = $_; $s =~ s!/(?:32|128)$!!; $maxlth = length $s if length $s > $maxlth; $s =~ /^1$/?undef:$s} DXCIDR::list();
L43: foreach my $list (@list) {
```

### Validation and access evidence

Source: `cmd/show/badip.pl` · SHA-256 `b2bddef8f064452a63df909e0863a06f73091dd8245f39158b3c21015e2aac41`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L36: my @list = map {my $s = $_; $s =~ s!/(?:32|128)$!!; $maxlth = length $s if length $s > $maxlth; $s =~ /^1$/?undef:$s} DXCIDR::list();
```

### Output and error evidence

Source: `cmd/show/badip.pl` · SHA-256 `b2bddef8f064452a63df909e0863a06f73091dd8245f39158b3c21015e2aac41`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
L12: return (1, q{Please install Net::CIDR::Lite or libnet-cidr-lite-perl to use this command}) unless $DXCIDR::active;
L27: push @out, "$ip DIRTY";
L30: push @out, "$ip CLEAN";
L33: return (1, @out);
L46: push @out, sprintf $format, @l;
L52: push @out, sprintf $format, @l;
L55: push @out, "show/badip: $count records found";
L56: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/badip.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BADIP
```

Compare the installed handler with this page when local overrides or a different revision may be present.