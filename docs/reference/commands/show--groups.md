# `SHOW/GROUPS`

<div class="command-hero" markdown>

**show recently used groups by Tommy SM3OSM**

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
SHOW/GROUPS
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXLog::print()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/groups.pl` · SHA-256 `df2f88d51dd003f39236496c97a922fd713668a44fe0113fd773747f44476aaa`

```perl
L15: my $self = shift;
L16: $to = shift;
L18: if ($to =~ /\D/) {
L30: my $self = shift;
L56: ($time, $call, $group) = ($row =~ m/^(\S+) (\S+) -> (\S+) /o);
L58: $time =~ m/^(\d\d)(\w{3})(\d{4})\@(\d\d):(\d\d):(\d\d)/o;
L60: $time =~ s/\@/ at /;
```

### Validation and access evidence

Source: `cmd/show/groups.pl` · SHA-256 `df2f88d51dd003f39236496c97a922fd713668a44fe0113fd773747f44476aaa`

```perl
L18: if ($to =~ /\D/) {
```

### Output and error evidence

Source: `cmd/show/groups.pl` · SHA-256 `df2f88d51dd003f39236496c97a922fd713668a44fe0113fd773747f44476aaa`

```perl
L19: return (1, "try sh/chatgroups xxx where xxx is the number of chat messages to search.");
L24: return (1, doit($self, DXLog::print(undef, $to, $main::systime, 'chat', undef)));
L26: return (1, $self->spawn_cmd("show/groups $to", \&DXLog::print, args => [0, $to, $main::systime, 'chat', undef], cb => \&doit));
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/groups.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/GROUPS
```

Compare the installed handler with this page when local overrides or a different revision may be present.