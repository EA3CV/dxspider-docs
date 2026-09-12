# `SHOW/DB0SDX`

<div class="command-hero" markdown>

**Show QSL infomation from DB0SDX database**

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
SHOW/DB0SDX [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`AsyncMsg->post()`, `dxchan->msg()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/db0sdx.pl` · SHA-256 `849151248a09958a6efac115f7e713e0d962a69d358b799ec3c6fa58f8e87808`

```perl
L13: my $conn = shift;
L14: my $dxchan = shift;
L21: my ($info) = $conn->{sdxin} =~ m|<qslinfoResult>([^<]*)</qslinfoResult>|;
L25: my @in = split /[\r\n]/, $info if $info;
L31: ($info) = $conn->{sdxin} =~ m|<faultstring>([^<]*)</faultstring>|;
L40: my $conn = shift;
L41: my $msg = shift;
L52: my ($self, $line) = @_;
L56: $line = uc $line;
L58: return (1, "SHOW/DB0SDX <callsign>, e.g. SH/DB0SDX ea7wa") unless $line && is_callsign($line);
L70: <callsign>$line</callsign>
L78: Log('call', "$call: show/db0sdx $line");
L88: $conn->{sdxline} = $line;
```

### Validation and access evidence

Source: `cmd/show/db0sdx.pl` · SHA-256 `849151248a09958a6efac115f7e713e0d962a69d358b799ec3c6fa58f8e87808`

```perl
L57: return (1, $self->msg('e24')) unless $Internet::allow;
L58: return (1, "SHOW/DB0SDX <callsign>, e.g. SH/DB0SDX ea7wa") unless $line && is_callsign($line);
```

### Output and error evidence

Source: `cmd/show/db0sdx.pl` · SHA-256 `849151248a09958a6efac115f7e713e0d962a69d358b799ec3c6fa58f8e87808`

```perl
L28: push @out, map {"$prefix$_"} @in;
L32: push @out, "$prefix$info" if $info;
L33: push @out, $dxchan->msg('e3', 'DB0SDX', $conn->{sdxline}) unless @out;
L35: $dxchan->send(@out);
L57: return (1, $self->msg('e24')) unless $Internet::allow;
L58: return (1, "SHOW/DB0SDX <callsign>, e.g. SH/DB0SDX ea7wa") unless $line && is_callsign($line);
L89: push @out, $self->msg('m21', "show/db0sdx");
L91: push @out, $self->msg('e18', 'DB0SDX Database server');
L94: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `e3`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/DB0SDX <callsign>
```

**Show QSL infomation from DB0SDX database**

## Details

This command queries the DB0SDX QSL server on the internet
and returns any information available for that callsign. This service
is provided for users of this software by http://www.qslinfo.de.

See also SHOW/QRZ, SHOW/WM7D.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/db0sdx.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DB0SDX
```

Compare the installed handler with this page when local overrides or a different revision may be present.