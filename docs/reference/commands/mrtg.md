# `MRTG`

<div class="command-hero" markdown>

**This is a local command to generate the various statistics that can then be displayed on an MRTG plot Your mrtg binary must live in one of the standard places**

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
MRTG [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.
- Reads or changes spot data.
- Uses the internal message subsystem.

### Recognized tokens, keys or enumerated values in this handler

`gauge`, `integer`, `noi`, `perminute`, `unknaszero`, `withzeroes`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXChannel::get_all_nodes()`, `DXChannel::get_all_users()`, `Route::Node::count()`, `Route::User::count()`, `mc->cfgprint()`, `mc->data()`

### Argument parsing evidence

Source: `cmd/mrtg.pl` · SHA-256 `89307ab8358e0379b0e01957e33a73694cbf6df610b97553c9572e295f6675ce`

```perl
L34: my ($self, $line) = @_;
L40: for (split /\s+/, $line) { $want{lc $_} = 1};
```

### Output and error evidence

Source: `cmd/mrtg.pl` · SHA-256 `89307ab8358e0379b0e01957e33a73694cbf6df610b97553c9572e295f6675ce`

```perl
L43: return (1, "MRTG not installed") unless $want{nomrtg} || -e '/usr/bin/mrtg' || -e '/usr/local/bin/mrtg';
L44: return (1, "MRTG requires top to be installed") unless $want{nomrtg} || -e '/usr/bin/top' || -e '/usr/local/bin/top';
L48: return (1, @out);
L56: my $mc = new Mrtg or return (1, "cannot initialise Mrtg $!");
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/mrtg.pl){ .md-button }

## Verify on a running node

```text
HELP MRTG
```

Compare the installed handler with this page when local overrides or a different revision may be present.