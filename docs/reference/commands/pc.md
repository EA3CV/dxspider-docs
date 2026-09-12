# `PC`

<div class="command-hero" markdown>

**Send text (eg PC Protocol) to <call>**

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
PC [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`DXChannel::get()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/pc.pl` · SHA-256 `73b65c491bd8e0636d9409efbb5e3f7eb5aa47b7516a0a22b566ede97b6744d9`

```perl
L8: my $self = shift;
L9: my $line = shift;
L10: my @f = split /\s+/, $line;
L14: my $call = uc shift @f;
L19: $line =~ s/$call\s+//i; # remove callsign and space
L20: $dxchan->send($line);
```

### Validation and access evidence

Source: `cmd/pc.pl` · SHA-256 `73b65c491bd8e0636d9409efbb5e3f7eb5aa47b7516a0a22b566ede97b6744d9`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 8 || $self->remotecmd || $self->inscript;
L16: return (1, $self->msg('e10', $call)) if !$dxchan;
L17: return (1, $self->msg('e8')) if @f <= 0;
```

### Output and error evidence

Source: `cmd/pc.pl` · SHA-256 `73b65c491bd8e0636d9409efbb5e3f7eb5aa47b7516a0a22b566ede97b6744d9`

```perl
L12: return (1, $self->msg('e5')) if $self->priv < 8 || $self->remotecmd || $self->inscript;
L16: return (1, $self->msg('e10', $call)) if !$dxchan;
L17: return (1, $self->msg('e8')) if @f <= 0;
L20: $dxchan->send($line);
L22: return (1);
```

### Message keys returned

`e10`, `e5`, `e8`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    PC <call> <text>
    ```

    **Send text (eg PC Protocol) to <call>**

    Send some arbitrary text to a locally connected callsign. No
    processing is done on the text. This command allows you to send PC
    Protocol to unstick things if problems arise (messages get stuck
    etc). eg:-

    ```text
     pc gb7djk PC33^GB7TLH^GB7DJK^400^
    ```
    or
    ```text
     pc G1TLH Try doing that properly!!!
    ```

=== "Help variant"

    ```text
    PC <call> <text>
    ```

    **Send arbitrary text to a connected callsign**

    Send any text you like to the callsign requested. This is used mainly to send
    PC protocol to connected nodes either for testing or to unstick things.

    You can also use in the same way as a talk command to a connected user but
    without any processing, added of "from <blah> to <blah" or whatever.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/pc.pl){ .md-button }

## Verify on a running node

```text
HELP PC
```

Compare the installed handler with this page when local overrides or a different revision may be present.