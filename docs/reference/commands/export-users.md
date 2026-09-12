# `EXPORT_USERS`

<div class="command-hero" markdown>

**Export the users database to ascii**

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
EXPORT_USERS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Named fields consumed by the parser

`fn`

### Recognized tokens, keys or enumerated values in this handler

`user_json`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXUser::export()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/export_users.pl` · SHA-256 `d1e93f769a64a70f9ca77e3c4c3e9094c5aabac860e6b073576c96cee7836b4f`

```perl
L6: my $self = shift;
L7: my $line = shift;;
L10: $line ||= 'user_json';
L11: my ($fn) = split /\s+/, $line;
L13: $fn =~ s|[/\.]||g;
```

### Validation and access evidence

Source: `cmd/export_users.pl` · SHA-256 `d1e93f769a64a70f9ca77e3c4c3e9094c5aabac860e6b073576c96cee7836b4f`

```perl
L8: return (1, $self->msg('e5')) unless $self->priv >= 9;
```

### Output and error evidence

Source: `cmd/export_users.pl` · SHA-256 `d1e93f769a64a70f9ca77e3c4c3e9094c5aabac860e6b073576c96cee7836b4f`

```perl
L8: return (1, $self->msg('e5')) unless $self->priv >= 9;
L19: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
EXPORT_USERS [<filename>]
```

**Export the users database to ascii**

## Details

Export the users database to a file in ascii format. If no filename
is given then it will export the file to /spider/data/user_asc.

If the file already exists it will be renamed to <filename>.o. In fact
up to 5 generations of the file can be kept each one with an extra 'o' on the
suffix.

BE WARNED: this will write to any file you have write access to. No check is
made on the filename (if any) that you specify.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/export_users.pl){ .md-button }

## Verify on a running node

```text
HELP EXPORT_USERS
```

Compare the installed handler with this page when local overrides or a different revision may be present.