# `REPLY`

<div class="command-hero" markdown>

**Reply (privately) to the last message that you have read**

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
REPLY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses the internal message subsystem.

### Recognized tokens, keys or enumerated values in this handler

`RR`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXMsg::get()`, `self->func()`, `self->loc()`, `self->msg()`, `self->state()`

### Argument parsing evidence

Source: `cmd/reply.pl` · SHA-256 `56e4317448d193ad32363cd798927592fdc49d481dd42d9a572c885ef1b4f019`

```perl
L19: my ($self, $line) = @_;
L27: my @f = split /\s+/, $line if $line;
L39: my $w = shift @f;
L40: if ($w =~ /^\d+$/) {
L42: } elsif ($w =~ /^(B|NOP)/i) {
L44: } elsif ($w =~ /^P/i) {
L74: $loc->{subject} = "Re: " . $loc->{subject} if !($loc->{subject} =~ /^Re:\s/io);
```

### Validation and access evidence

Source: `cmd/reply.pl` · SHA-256 `56e4317448d193ad32363cd798927592fdc49d481dd42d9a572c885ef1b4f019`

```perl
L40: if ($w =~ /^\d+$/) {
L59: return (1, $self->msg('m4', $i)) unless $oref;
L63: if ($loc->{private}) {
L70: return (1, $self->msg('e28')) unless $self->isregistered || $to eq $main::myalias;
L74: $loc->{subject} = "Re: " . $loc->{subject} if !($loc->{subject} =~ /^Re:\s/io);
```

### Output and error evidence

Source: `cmd/reply.pl` · SHA-256 `56e4317448d193ad32363cd798927592fdc49d481dd42d9a572c885ef1b4f019`

```perl
L59: return (1, $self->msg('m4', $i)) unless $oref;
L70: return (1, $self->msg('e28')) unless $self->isregistered || $to eq $main::myalias;
L81: push @out, $self->msg('m6', join(',', $to, @extra));
L82: push @out, $self->msg('m7', $loc->{subject});
L83: push @out, $self->msg('m8');
L86: return (1, @out);
```

### Message keys returned

`e28`, `m4`, `m6`, `m7`, `m8`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    REPLY
    ```

    **Reply (privately) to the last message that you have read**


=== "Help variant"

    ```text
    REPLY <msgno>
    ```

    **Reply (privately) to the specified message**


=== "Help variant"

    ```text
    REPLY B <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "Help variant"

    ```text
    REPLY NOPrivate <msgno>
    ```

    **Reply as a Bulletin to the specified message**


=== "Help variant"

    ```text
    REPLY RR <msgno>
    ```

    **Reply to the specified message with read receipt**

    You can reply to a message and the subject will automatically have
    "Re:" inserted in front of it, if it isn't already present.

    You can also use all the extra qualifiers such as RR, PRIVATE,
    NOPRIVATE, B that you can use with the SEND command (see SEND
    for further details)

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/reply.pl){ .md-button }

## Verify on a running node

```text
HELP REPLY
```

Compare the installed handler with this page when local overrides or a different revision may be present.