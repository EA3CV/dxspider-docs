# `SHOW/WM7D`

<div class="command-hero" markdown>

**Show callbook details on a US callsigns**

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
SHOW/WM7D [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`AsyncMsg->raw()`, `conn->handle_raw()`, `conn->send_later()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/wm7d.pl` · SHA-256 `7e5d08d73e3a438ff24da93f24e3f02bcf48feecef5a33f8fe5d25d5d8a1b281`

```perl
L13: my $conn = shift;
L14: my $msg = shift;
L15: $msg =~ s/\cM//g;
L18: $buf =~ s/\r/\\r/g;
L19: $buf =~ s/\n/\\n/g;
L26: if ($msg =~ /utc$/ ) {
L31: if ($conn->{msg} =~ /^\rquery->\s*$/) {
L35: return if $msg =~ /^query->/;
L38: return if $msg =~ /^query->/ || $msg =~ /bye/;
L46: my $conn = shift;
L47: my $dxchan = shift;
L57: my ($self, $line) = @_;
L66: return (1, "SHOW/WM7D <callsign>, e.g. SH/WM7D k1xx") unless $line;
L71: Log('call', "$call: show/wm7d \U$line");
L77: $conn->{target_call} = $line;
```

### Validation and access evidence

Source: `cmd/show/wm7d.pl` · SHA-256 `7e5d08d73e3a438ff24da93f24e3f02bcf48feecef5a33f8fe5d25d5d8a1b281`

```perl
L26: if ($msg =~ /utc$/ ) {
L31: if ($conn->{msg} =~ /^\rquery->\s*$/) {
L35: return if $msg =~ /^query->/;
L38: return if $msg =~ /^query->/ || $msg =~ /bye/;
L65: return (1, $self->msg('e24')) unless $Internet::allow;
```

### Output and error evidence

Source: `cmd/show/wm7d.pl` · SHA-256 `7e5d08d73e3a438ff24da93f24e3f02bcf48feecef5a33f8fe5d25d5d8a1b281`

```perl
L50: $dxchan->send(map {"$conn->{prefix}$_"} @{$conn->{_wm7d}});
L65: return (1, $self->msg('e24')) unless $Internet::allow;
L66: return (1, "SHOW/WM7D <callsign>, e.g. SH/WM7D k1xx") unless $line;
L79: push @out, $self->msg('m21', "show/wm7d");
L81: push @out, $self->msg('e18', 'WM7D.net');
L84: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/WM7D <callsign>
```

**Show callbook details on a US callsigns**

## Details

This command queries the WM7D callbook server on the internet
and returns any information available for that US callsign. This service
is provided for users of this software by http://www.wm7d.net.

See also SHOW/QRZ.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/wm7d.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/WM7D
```

Compare the installed handler with this page when local overrides or a different revision may be present.