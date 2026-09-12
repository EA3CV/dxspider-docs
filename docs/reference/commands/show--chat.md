# `SHOW/CHAT`

<div class="command-hero" markdown>

**Show any chat or conferencing**

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
SHOW/CHAT
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/chat.pl` · SHA-256 `d5bad601571a6fe9232254d602bf4cbc7883a710bfb567c08ea15c0e162c7a30`

```perl
L8: my $self = shift;
L13: my $cmdline = shift;
L14: my @f = split /\s+/, $cmdline;
L20: while ($f = shift @f) { # next field
L23: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L27: ($to) = $f =~ /^(\d+)$/o if !$to; # is it a to count?
```

### Validation and access evidence

Source: `cmd/show/chat.pl` · SHA-256 `d5bad601571a6fe9232254d602bf4cbc7883a710bfb567c08ea15c0e162c7a30`

```perl
L31: if ($f !~ /^\d+$/) {
```

### Output and error evidence

Source: `cmd/show/chat.pl` · SHA-256 `d5bad601571a6fe9232254d602bf4cbc7883a710bfb567c08ea15c0e162c7a30`

```perl
L45: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/CHAT [<group>] [<lines>]
```

**Show any chat or conferencing**

## Details

This command allows you to see any chat or conferencing that has
occurred whilst you were away. SHOW/CHAT on its own will show data for
all groups. If you use a group name then it will show only chat for
that group.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/chat.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CHAT
```

Compare the installed handler with this page when local overrides or a different revision may be present.