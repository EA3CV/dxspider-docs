# `UNSET/STARTUP`

<div class="command-hero" markdown>

**Remove a user startup script**

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
UNSET/STARTUP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.

### Important calls

`Script::erase()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/unset/startup.pl` · SHA-256 `460f8d2a9f697b95bd687d8663d4282a112bbbbe7d49f8c7a74375b5b1752d95`

```perl
L8: my ($self, $line) = @_;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
```

### Validation and access evidence

Source: `cmd/unset/startup.pl` · SHA-256 `460f8d2a9f697b95bd687d8663d4282a112bbbbe7d49f8c7a74375b5b1752d95`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
```

### Output and error evidence

Source: `cmd/unset/startup.pl` · SHA-256 `460f8d2a9f697b95bd687d8663d4282a112bbbbe7d49f8c7a74375b5b1752d95`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd || $self->inscript;
L10: return (1, $self->msg('e5')) if $line && $self->priv < 5;
L12: return (1, Script::erase($self));
```

### Message keys returned

`e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    UNSET/STARTUP <call>
    ```

    **Remove a user startup script**


=== "Help variant"

    ```text
    UNSET/STARTUP
    ```

    **Remove your own startup script**

    You can remove your startup script with UNSET/STARTUP.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/startup.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/STARTUP
```

Compare the installed handler with this page when local overrides or a different revision may be present.