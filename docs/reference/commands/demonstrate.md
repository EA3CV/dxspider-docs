# `DEMONSTRATE`

<div class="command-hero" markdown>

**Demonstrate a command to another user**

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
DEMONSTRATE [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Named fields consumed by the parser

`call`, `newline`

### Important calls

`DXChannel::get()`, `dxchan->run_cmd()`, `dxchan->send()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/demonstrate.pl` · SHA-256 `38dcefcae8b88301b3dd9fdadba482b379df69248092b2bd8b56a77ade1d5233`

```perl
L10: my ($self, $line) = @_;
L12: my ($call, $newline) = split /\s+/, $line, 2;
```

### Validation and access evidence

Source: `cmd/demonstrate.pl` · SHA-256 `38dcefcae8b88301b3dd9fdadba482b379df69248092b2bd8b56a77ade1d5233`

```perl
L17: return (1, $self->msg('e7', $call)) unless $dxchan;
L18: return (1, $self->msg('e31', $call)) unless $dxchan->is_user;
L19: if ($self->remotecmd || $self->inscript) {
L21: return (1, $self->msg('e5'));
L23: if ($self->priv < 9) {
L25: return (1, $self->msg('e5'));
```

### Output and error evidence

Source: `cmd/demonstrate.pl` · SHA-256 `38dcefcae8b88301b3dd9fdadba482b379df69248092b2bd8b56a77ade1d5233`

```perl
L17: return (1, $self->msg('e7', $call)) unless $dxchan;
L18: return (1, $self->msg('e31', $call)) unless $dxchan->is_user;
L21: return (1, $self->msg('e5'));
L25: return (1, $self->msg('e5'));
L30: $dxchan->send($newline, @in);
L32: return (1, map { "->$call: $_" } @in);
```

### Message keys returned

`e31`, `e5`, `e7`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DEMONSTRATE <call> <command>
```

**Demonstrate a command to another user**

## Details

This command is provided so that sysops can demonstrate commands to
other users. It runs a command as though that user had typed it in and
then sends the output to that user, together with the command that
caused it.

```text
DEMO g7brn sh/dx iota oc209
DEMO g1tlh set/here
```

Note that this command is similar to SPOOF and will have the same side
effects. Commands are run at the privilege of the user which is being
demonstrated to.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/demonstrate.pl){ .md-button }

## Verify on a running node

```text
HELP DEMONSTRATE
```

Compare the installed handler with this page when local overrides or a different revision may be present.