# `GET/KEPS`

<div class="command-hero" markdown>

**Obtain the latest AMSAT Keplarian Elements from the web**

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
GET/KEPS [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Performs file I/O.

### Recognized tokens, keys or enumerated values in this handler

` `, `keps`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`AsyncMsg->get()`, `Data::Dumper()`, `dd->Indent()`, `dd->Quotekeys()`, `dxchan->run_cmd()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/get/keps.pl` · SHA-256 `e0e332edb759d7657862ae912d6081b1d866ec7dc8c085aa3341e8ea6bfc39cc`

```perl
L17: my ($sign, $frac, $esign, $exp) = unpack "aa5aa", shift;
L25: my $conn = shift;
L26: my $dxchan = shift;
L32: my @lines = split /[\r\n]+/, $conn->{kepsin};
L34: my $line = 0;
L65: $n =~ s/\s/-/g;
L136: my $conn = shift;
L137: my $msg = shift;
L146: my ($self, $line) = @_;
L150: $line = uc $line;
L159: Log('call', "$call: show/keps $line");
```

### Validation and access evidence

Source: `cmd/get/keps.pl` · SHA-256 `e0e332edb759d7657862ae912d6081b1d866ec7dc8c085aa3341e8ea6bfc39cc`

```perl
L90: delete $keps{$name} if defined $name;
L151: return (1, $self->msg('e24')) unless $Internet::allow;
L152: return (1, $self->msg('e5')) if $self->priv < 8;
```

### Output and error evidence

Source: `cmd/get/keps.pl` · SHA-256 `e0e332edb759d7657862ae912d6081b1d866ec7dc8c085aa3341e8ea6bfc39cc`

```perl
L129: $dxchan->send($dxchan->run_cmd("load/keps"));
L151: return (1, $self->msg('e24')) unless $Internet::allow;
L152: return (1, $self->msg('e5')) if $self->priv < 8;
L165: push @out, $self->msg('m21', "show/keps");
L167: push @out, $self->msg('e18', 'get/keps error');
L170: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `e5`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
GET/KEPS
```

**Obtain the latest AMSAT Keplarian Elements from the web**

## Details

There are various ways that one can obtain the AMSAT keps. Traditionally the
regular method was to get on the mailing list and then arrange for the email
to be piped into convkeps.pl and arrange from the crontab to run LOAD/KEPS.
For various reasons, it was quite easy for one to be silently dropped
from this mailing list.

With the advent of asynchronous (web) connections in DXSpider it is now
possible to use this command to get the latest keps direct from the
AMSAT web site. One can do this from the command line or one can add a line
in the local DXSpider crontab file to do periodically (say once a week).

This command will clear out the existing keps and then run LOAD/KEPS
for you (but only) after a successful download from the AMSAT website.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/get/keps.pl){ .md-button }

## Verify on a running node

```text
HELP GET/KEPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.