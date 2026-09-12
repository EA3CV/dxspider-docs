# `SHOW/CONTEST`

<div class="command-hero" markdown>

**Show all the contests for a month**

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
SHOW/CONTEST [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Recognized tokens, keys or enumerated values in this handler

`mai`, `maj`, `okt`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`AsyncMsg->get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/contest.pl` · SHA-256 `0156434c6832fd224484ff42cc2618669d59cf2c13c2f0c45785601110459163`

```perl
L11: my ($self, $line) = @_;
L22: $line = lc $line;
L24: ($y) = $line =~ /(\d+)/;
L25: ($m) = $line =~ /([a-z]{3})/;
```

### Validation and access evidence

Source: `cmd/show/contest.pl` · SHA-256 `0156434c6832fd224484ff42cc2618669d59cf2c13c2f0c45785601110459163`

```perl
L13: return (1, $self->msg('e24')) unless $Internet::allow;
```

### Output and error evidence

Source: `cmd/show/contest.pl` · SHA-256 `0156434c6832fd224484ff42cc2618669d59cf2c13c2f0c45785601110459163`

```perl
L13: return (1, $self->msg('e24')) unless $Internet::allow;
L57: push @out, $self->msg('m21', "show/contest");
L60: push @out, $self->msg('e18','sk3bg.se');
L63: return (1, @out);
```

### Message keys returned

`e18`, `e24`, `m21`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/CONTEST [<year>] [<month>]
```

**Show all the contests for a month**

## Details

Show all known contests which are maintained at http://www.sk3bg.se/contest/
for a particular month or year. The format is reasonably flexible.
For example:-

```text
SH/CONTEST
SH/CONTEST mar
SH/CONTEST mar 13
SH/CONTEST 13 march
```

If there is no month/year then the current month's contests are shown.

Note that it expects ENGLISH (jan/feb/mar/apr/may/jun/jul/aug/sep/oct/nov/dec)
month names.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/contest.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CONTEST
```

Compare the installed handler with this page when local overrides or a different revision may be present.