# `SHOW/IK3QAR`

<div class="command-hero" markdown>

**Obtain QSL info from IK3QAR database**

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
SHOW/IK3QAR [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Performs file I/O.
- Uses cluster synchronization/state code.

### Important calls

`AsyncMsg->get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/ik3qar.pl` · SHA-256 `85ea199b9d3482f38b4b74d707e69c27975ce5effa7a3407b1528fbbfced74bd`

```perl
L11: my ($self, $line) = @_;
L17: return (1, "SHOW/IK3QAR <callsign>\n e.g. SH/IK3QAR II5I, SH/IK3QAR V51AS\n") unless $line;
L22: $line = uc $line;
L23: dbg("IK3QAR: call = $line") if isdbg('ik3qar');
L24: $op="call=$line\&node=$main::mycall\&passwd=$Internet::ik3qar_pw\&user=$call";
L27: Log('call', "$call: SH/IK3QAR $line");
```

### Validation and access evidence

Source: `cmd/show/ik3qar.pl` · SHA-256 `85ea199b9d3482f38b4b74d707e69c27975ce5effa7a3407b1528fbbfced74bd`

```perl
L16: return (1, $self->msg('e24')) unless $Internet::allow;
```

### Output and error evidence

Source: `cmd/show/ik3qar.pl` · SHA-256 `85ea199b9d3482f38b4b74d707e69c27975ce5effa7a3407b1528fbbfced74bd`

```perl
L16: return (1, $self->msg('e24')) unless $Internet::allow;
L17: return (1, "SHOW/IK3QAR <callsign>\n e.g. SH/IK3QAR II5I, SH/IK3QAR V51AS\n") unless $line;
L32: push @out, $self->msg('m21', "show/ik3qar");
L34: push @out, $self->msg('e18', 'Open(IK3QAR.it)');
L37: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/IK3QAR <callsign>
```

**Obtain QSL info from IK3QAR database**

## Details

Get QSL information from the online dabase run by IK3QAR.

Your sysop needs to set up this command by obtaining a password from IK3QAR.
Instructions are available in local/Internet.pm

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/ik3qar.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/IK3QAR
```

Compare the installed handler with this page when local overrides or a different revision may be present.