# `SHOW/WWV`

<div class="command-hero" markdown>

**Show last 10 WWV broadcasts**

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
SHOW/WWV
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`Geomag::print_item()`, `Geomag::search()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/wwv.pl` · SHA-256 `d7411755a70a878d43601cfb124450104cfc7bb9f48f2a3d1493fd1fc4d8a763`

```perl
L8: my $self = shift;
L10: my $cmdline = shift;
L11: my @f = split /\s+/, $cmdline;
L17: while ($f = shift @f) { # next field
L20: ($from, $to) = $f =~ /^(\d+)-(\d+)$/o; # is it a from -> to count?
L24: ($to) = $f =~ /^(\d+)$/o; # is it a to count?
```

### Output and error evidence

Source: `cmd/show/wwv.pl` · SHA-256 `d7411755a70a878d43601cfb124450104cfc7bb9f48f2a3d1493fd1fc4d8a763`

```perl
L32: push @out, $self->msg('wwv3');
L35: push @out, Geomag::print_item($_);
L37: return (1, @out);
```

### Message keys returned

`wwv3`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/WWV
    ```

    **Show last 10 WWV broadcasts**


=== "Help variant"

    ```text
    SHOW/WWV <n>
    ```

    **Show last <n> WWV broadcasts**

    Display the most recent WWV information that has been received by the system

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/wwv.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/WWV
```

Compare the installed handler with this page when local overrides or a different revision may be present.