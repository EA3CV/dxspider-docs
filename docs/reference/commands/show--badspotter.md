# `SHOW/BADSPOTTER`

<div class="command-hero" markdown>

**Show all the bad spotters in the system**

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
SHOW/BADSPOTTER [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`badspotter->show()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/badspotter.pl` · SHA-256 `d80a8ea639e0fc584005fbf55b4d174dfa1420ad2da92fbd2333a6c7f305a251`

```perl
L8: my ($self, $line) = @_;
L12: $line = join(' ', map {s|[/-]\d+$||; $_} split(/\s+/, $line));
```

### Validation and access evidence

Source: `cmd/show/badspotter.pl` · SHA-256 `d80a8ea639e0fc584005fbf55b4d174dfa1420ad2da92fbd2333a6c7f305a251`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
```

### Output and error evidence

Source: `cmd/show/badspotter.pl` · SHA-256 `d80a8ea639e0fc584005fbf55b4d174dfa1420ad2da92fbd2333a6c7f305a251`

```perl
L9: return (1, $self->msg('e5')) if $self->remotecmd;
L11: return (1, $self->msg('e5')) if $self->priv < 6;
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/BADSPOTTER
```

**Show all the bad spotters in the system**

## Details

Display all the bad spotter's callsigns in the system, see SET/BADSPOTTER
for more information.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/badspotter.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BADSPOTTER
```

Compare the installed handler with this page when local overrides or a different revision may be present.