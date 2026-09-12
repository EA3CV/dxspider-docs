# `SET/STARTUP`

<div class="command-hero" markdown>

**Create a user startup script**

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
SET/STARTUP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`self->func()`, `self->msg()`, `self->state()`

### Argument parsing evidence

Source: `cmd/set/startup.pl` · SHA-256 `1814d79e0f70499ccf4fb4577be499f4d823374ac5640bed334d9fe4d7403ae5`

```perl
L8: my ($self, $line) = @_;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 6;
L11: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
L14: my $loc = $self->{loc} = { call => ($line || $self->call),
```

### Validation and access evidence

Source: `cmd/set/startup.pl` · SHA-256 `1814d79e0f70499ccf4fb4577be499f4d823374ac5640bed334d9fe4d7403ae5`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 6;
L11: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
```

### Output and error evidence

Source: `cmd/set/startup.pl` · SHA-256 `1814d79e0f70499ccf4fb4577be499f4d823374ac5640bed334d9fe4d7403ae5`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 6;
L11: return (1, $self->msg('e36')) unless $self->state =~ /^prompt/;
L22: push @out, $self->msg('m8');
L23: return (1, @out);
```

### Message keys returned

`e36`, `e5`, `m8`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SET/STARTUP <call>
    ```

    **Create a user startup script**


=== "Help variant"

    ```text
    SET/STARTUP
    ```

    **Create your own startup script**

    Create a startup script of DXSpider commands which will be executed
    everytime that you login into this node. You can only input the whole
    script afresh, it is not possible to 'edit' it. Inputting a new script is
    just like typing in a message using SEND. To finish inputting type: /EX
    on a newline, to abandon the script type: /ABORT.

    You may find the (curiously named) command BLANK useful to break
    up the output. If you simply want a blank line, it is easier to
    input one or more spaces and press the <return> key.

    See UNSET/STARTUP to remove a script.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/startup.pl){ .md-button }

## Verify on a running node

```text
HELP SET/STARTUP
```

Compare the installed handler with this page when local overrides or a different revision may be present.