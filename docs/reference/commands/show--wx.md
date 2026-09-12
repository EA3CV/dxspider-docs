# `SHOW/WX`

<div class="command-hero" markdown>

**show wx data this appears to be a reasonable thing for users to do (thank you JE1SGH) return (1, $self->msg('e5')) if $self->priv < 9;**

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
SHOW/WX
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`DXLog::print()`, `self->msg()`, `self->spawn_cmd()`

### Argument parsing evidence

Source: `cmd/show/wx.pl` · SHA-256 `27deb607ce0badbc73b58ac822ec0f185afb8458b728ea4768e5c212f24cc7f2`

```perl
L4: my $self = shift;
L9: my $cmdline = shift;
L10: my @f = split /\s+/, $cmdline;
L16: while ($f = shift @f) { # next field
L19: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L23: ($to) = $f =~ /^(\d+)$/o if !$to; # is it a to count?
```

### Output and error evidence

Source: `cmd/show/wx.pl` · SHA-256 `27deb607ce0badbc73b58ac822ec0f185afb8458b728ea4768e5c212f24cc7f2`

```perl
L37: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/wx.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/WX
```

Compare the installed handler with this page when local overrides or a different revision may be present.