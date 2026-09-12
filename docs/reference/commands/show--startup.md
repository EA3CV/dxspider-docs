# `SHOW/STARTUP`

<div class="command-hero" markdown>

**View a user startup script**

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
SHOW/STARTUP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`Script->new()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/startup.pl` · SHA-256 `e2a11a83af593ea6fa91a7cbed955761222018db8ffda8e37b1ff6a08d3e7ff2`

```perl
L8: my ($self, $line) = @_;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
L14: my $s = Script->new($line || $self->call);
```

### Validation and access evidence

Source: `cmd/show/startup.pl` · SHA-256 `e2a11a83af593ea6fa91a7cbed955761222018db8ffda8e37b1ff6a08d3e7ff2`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
```

### Output and error evidence

Source: `cmd/show/startup.pl` · SHA-256 `e2a11a83af593ea6fa91a7cbed955761222018db8ffda8e37b1ff6a08d3e7ff2`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
L15: push @out, $s->lines if $s;
L16: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/STARTUP <call>
    ```

    **View a user startup script**


=== "Help variant"

    ```text
    SHOW/STARTUP
    ```

    **View your own startup script**

    View the contents of a startup script created with SET/STARTUP.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/startup.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/STARTUP
```

Compare the installed handler with this page when local overrides or a different revision may be present.