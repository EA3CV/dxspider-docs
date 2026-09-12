# `LOAD/KEPS`

<div class="command-hero" markdown>

**Load new keps data**

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
LOAD/KEPS [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::filename()`, `DXMsg::get()`, `Sun::load()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/keps.pl` · SHA-256 `0a92fc5f0fc1d2a2083c276a1d93e73393634170228842cff3b8447cbac84def`

```perl
L4: my ($self, $line) = @_;
L7: if ($line =~ /^(\d+)$/) {
L11: return (1, $self->msg('sat5')) unless $mref->subject =~ /\b\d{3,6}\.AMSAT\b/i;
```

### Validation and access evidence

Source: `cmd/load/keps.pl` · SHA-256 `0a92fc5f0fc1d2a2083c276a1d93e73393634170228842cff3b8447cbac84def`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 5;
L7: if ($line =~ /^(\d+)$/) {
L10: return (1, $self->msg('m4', $msgno)) unless $mref;
L11: return (1, $self->msg('sat5')) unless $mref->subject =~ /\b\d{3,6}\.AMSAT\b/i;
```

### Output and error evidence

Source: `cmd/load/keps.pl` · SHA-256 `0a92fc5f0fc1d2a2083c276a1d93e73393634170228842cff3b8447cbac84def`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 5;
L10: return (1, $self->msg('m4', $msgno)) unless $mref;
L11: return (1, $self->msg('sat5')) unless $mref->subject =~ /\b\d{3,6}\.AMSAT\b/i;
L16: return (1, @in) if @in;
L19: @out = ($self->msg('ok')) if !@out;
L20: return (1, @out);
```

### Message keys returned

`e5`, `m4`, `ok`, `sat5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    LOAD/KEPS
    ```

    **Load new keps data**


=== "Help variant"

    ```text
    LOAD/KEPS [nn]
    ```

    **Load new keps data from message**

    If there is no message number then reload the current Keps data from
    the Keps.pm data file. You create this file by running

     /spider/perl/convkeps.pl <filename>

    on a file containing NASA 2 line keps as a message issued by AMSAT.

    If there is a message number, then it will take the message, run
    convkeps.pl on it and then load the data, all in one step.

    These messages are sent to ALL by GB7DJK (and others) from time to time.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/keps.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/KEPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.