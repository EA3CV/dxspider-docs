# `DBDELKEY`

<div class="command-hero" markdown>

**Database update routine**

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
DBDELKEY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Argument parsing evidence

Source: `cmd/dbdelkey.pl` · SHA-256 `78b3623b5c856d584c4de2d76a1bec36f1e7e954d19404b72d200889387c8919`

```perl
L7: my ($self, $line) = @_;
L8: my @f = split /\s+/, $line;
```

### Output and error evidence

Source: `cmd/dbdelkey.pl` · SHA-256 `78b3623b5c856d584c4de2d76a1bec36f1e7e954d19404b72d200889387c8919`

```perl
L12: return (1, @out);
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbdelkey.pl){ .md-button }

## Verify on a running node

```text
HELP DBDELKEY
```

Compare the installed handler with this page when local overrides or a different revision may be present.