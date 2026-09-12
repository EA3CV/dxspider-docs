# `LOAD/MESSAGES`

<div class="command-hero" markdown>

**Reload the system messages file**

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
LOAD/MESSAGES
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXM::load()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/messages.pl` · SHA-256 `ebfc56a728d377527950b7e4f4eb8ea4e6e920d1399edbd92272c51f58c7738d`

```perl
L4: my $self = shift;
```

### Validation and access evidence

Source: `cmd/load/messages.pl` · SHA-256 `ebfc56a728d377527950b7e4f4eb8ea4e6e920d1399edbd92272c51f58c7738d`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/load/messages.pl` · SHA-256 `ebfc56a728d377527950b7e4f4eb8ea4e6e920d1399edbd92272c51f58c7738d`

```perl
L5: return (1, $self->msg('e5')) if $self->priv < 9;
L7: @out = ($self->msg('ok')) if !@out;
L8: return (1, @out);
```

### Message keys returned

`e5`, `ok`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/MESSAGES
```

**Reload the system messages file**

## Details

If you change the /spider/perl/Messages file (usually whilst
fiddling/writing new commands) you can have them take effect during a
cluster session by executing this command. You need to do this if get
something like :-

unknown message 'xxxx' in lang 'en'

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/messages.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/MESSAGES
```

Compare the installed handler with this page when local overrides or a different revision may be present.