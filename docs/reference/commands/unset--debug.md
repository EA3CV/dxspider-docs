# `UNSET/DEBUG`

<div class="command-hero" markdown>

**Remove a debug level from the debug set**

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
UNSET/DEBUG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Argument parsing evidence

Source: `cmd/unset/debug.pl` · SHA-256 `8859a8d142d35adf2d15ddd09c785195b446941e39a4071480f791cfaa0ce8f4`

```perl
L9: my ($self, $line) = @_;
L12: dbgsub(split /\s+/, $line);
```

### Validation and access evidence

Source: `cmd/unset/debug.pl` · SHA-256 `8859a8d142d35adf2d15ddd09c785195b446941e39a4071480f791cfaa0ce8f4`

```perl
L10: return (0) if $self->priv < 9;
```

### Output and error evidence

Source: `cmd/unset/debug.pl` · SHA-256 `8859a8d142d35adf2d15ddd09c785195b446941e39a4071480f791cfaa0ce8f4`

```perl
L10: return (0) if $self->priv < 9;
L15: return (1, "Debug Levels now: $set");
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNSET/DEBUG <name>
```

**Remove a debug level from the debug set**

## Details

You can choose to log several different levels.  The levels are

 chan
 state
 msg
 cron
 connect

You can show what levels you are logging with SHOW/DEBUG

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/unset/debug.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/DEBUG
```

Compare the installed handler with this page when local overrides or a different revision may be present.