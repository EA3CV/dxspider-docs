# `LOAD/BADIP`

<div class="command-hero" markdown>

**Reload the bad IP address table**

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
LOAD/BADIP [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`DXCIDR::reload()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/load/badip.pl` · SHA-256 `327c27beefd35b446b0a0e5ff15c2dd1f3da6a9c3f678c06108029cccc81bcc3`

```perl
L7: my ($self, $line) = @_;
```

### Validation and access evidence

Source: `cmd/load/badip.pl` · SHA-256 `327c27beefd35b446b0a0e5ff15c2dd1f3da6a9c3f678c06108029cccc81bcc3`

```perl
L8: return (1, $self->msg('e5')) if $self->remotecmd;
L10: return (1, $self->msg('e5')) if $self->priv < 6;
```

### Output and error evidence

Source: `cmd/load/badip.pl` · SHA-256 `327c27beefd35b446b0a0e5ff15c2dd1f3da6a9c3f678c06108029cccc81bcc3`

```perl
L8: return (1, $self->msg('e5')) if $self->remotecmd;
L10: return (1, $self->msg('e5')) if $self->priv < 6;
L11: return (1, q{Please install Net::CIDR::Lite or libnet-cidr-lite-perl to use this command}) unless $DXCIDR::active;
L17: return (1, "load/badip: $_ $@") if $@;
L19: push @out, "load/badip: added $count entries";
L20: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
LOAD/BADIP
```

**Reload the bad IP address table**

## Details

Reload the badip address file(s) if you have changed any of them  manually
whilst the cluster is running.

You can edit the badip.* files manually in local_data or (for instance)
obtain some bad IP addresses from the web to replace badip.base for TOR
IP addresses (this filename may change).

There is (currently) no UNSET/BADIP command so you will need to edit
the badip.local file to remove IP addresses.

After modification, you can reload the database with:

```text
LOAD/BADIP
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/load/badip.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/BADIP
```

Compare the installed handler with this page when local overrides or a different revision may be present.