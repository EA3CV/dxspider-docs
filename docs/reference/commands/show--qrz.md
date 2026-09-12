# `SHOW/QRZ`

<div class="command-hero" markdown>

**Show any callbook details on a callsign**

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
SHOW/QRZ [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`addr2`, `ADIF`, `blank`, `call`, `country`, `county`, `dxcc`, `Error`, `fname`, `go`, `grid`, `lat`, `lon`, `moddate`, `name`, `qslmgr`, `state`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`AsyncMsg->get()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/qrz.pl` · SHA-256 `7a68aa18ef6f7f04da1f04531fb503c57f741bc36382e88043073c580910b6ce`

```perl
L19: my $conn = shift;
L20: my $msg = shift;
L21: my $dxchan = shift;
L23: my ($tag, $data) = $msg =~ m|^\s*<(\w+)>(.*)</|;
L33: my $conn = shift;
L34: my $dxchan = shift;
L40: my $conn = shift;
L41: my $msg = shift;
L42: my $dxchan = shift;
L49: if ($msg =~ /^\s*<Callsign>/) {
L51: } elsif ($msg =~ /^\s*<Error>/) {
L55: if ($msg =~ m|</Callsign>|) {
L66: my ($self, $line) = @_;
L71: return (1, "SHOW/QRZ <callsign>, e.g. SH/QRZ g1tlh") unless $line;
L74: my $path = qq{/xml/current/?callsign=$line;username=$Internet::qrz_uid;password=$Internet::qrz_pw;agent=dxspider};
L77: Log('cmd', "$self->{call}|$addr|show/qrz|$line");
```

### Validation and access evidence

Source: `cmd/show/qrz.pl` · SHA-256 `7a68aa18ef6f7f04da1f04531fb503c57f741bc36382e88043073c580910b6ce`

```perl
L49: if ($msg =~ /^\s*<Callsign>/) {
L55: if ($msg =~ m|</Callsign>|) {
L70: return (1, $self->msg('e24')) unless $Internet::allow;
```

### Output and error evidence

Source: `cmd/show/qrz.pl` · SHA-256 `7a68aa18ef6f7f04da1f04531fb503c57f741bc36382e88043073c580910b6ce`

```perl
L27: $dxchan->send($prefix . sprintf("%-10s: $data", $tag));
L35: $dxchan->send("Data provided by www.qrz.com");
L70: return (1, $self->msg('e24')) unless $Internet::allow;
L71: return (1, "SHOW/QRZ <callsign>, e.g. SH/QRZ g1tlh") unless $line;
L81: push @out, $self->msg('m21', "show/qrz");
L83: push @out, $self->msg('e18', 'QRZ.com');
L86: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/QRZ <callsign>
```

**Show any callbook details on a callsign**

## Details

This command queries the QRZ callbook server on the internet
and returns any information available for that callsign. This service
is provided for users of this software by http://www.qrz.com

See also SHOW/WM7D for an alternative.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/qrz.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/QRZ
```

Compare the installed handler with this page when local overrides or a different revision may be present.