# `UPTIME`

<div class="command-hero" markdown>

**do a tradiotional "uptime" clone**

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
UPTIME
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Argument parsing evidence

Source: `cmd/uptime.pl` · SHA-256 `5f1de81ca192b19b630bbc337b56dba093383dd8a03607998daab80247338ae1`

```perl
L4: my $self = shift;
```

### Output and error evidence

Source: `cmd/uptime.pl` · SHA-256 `5f1de81ca192b19b630bbc337b56dba093383dd8a03607998daab80247338ae1`

```perl
L6: return (1, sprintf("%s $main::mycall uptime: %s", ztime(), difft($main::starttime, ' ')));
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/uptime.pl){ .md-button }

## Verify on a running node

```text
HELP UPTIME
```

Compare the installed handler with this page when local overrides or a different revision may be present.