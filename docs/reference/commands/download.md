# `DOWNLOAD`

<div class="command-hero" markdown>

**Download a file into local_data**

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
DOWNLOAD
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`new->insecure()`, `res->save_to()`, `self->msg()`, `ua->get()`

### Argument parsing evidence

Source: `cmd/download.pl` · SHA-256 `51805ee30c9afb831424261d794532e9a9c56d19526ba1e8d9f3e7fb310a4ada`

```perl
L16: my $self = shift;
L18: my $url = unpad(shift);
L19: my $dest = unpad(shift) if @_;
L39: my @parts = split m|/|, $path;
```

### Validation and access evidence

Source: `cmd/download.pl` · SHA-256 `51805ee30c9afb831424261d794532e9a9c56d19526ba1e8d9f3e7fb310a4ada`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
```

### Output and error evidence

Source: `cmd/download.pl` · SHA-256 `51805ee30c9afb831424261d794532e9a9c56d19526ba1e8d9f3e7fb310a4ada`

```perl
L17: return (1, $self->msg('e5')) if $self->priv < 9 || $self->remotecmd;
```

### Message keys returned

`e5`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DOWNLOAD <url>
```

**Download a file into local_data**

## Details

This command is a direct replacement for the unix 'wget -Qn' command
that is used to download files like badip, spot data, user databases
like usdb. It is designed to work either on the command line in a console
or (more likely) in the crontab, like the example below:

24 * * * * run_cmd('download http://www.dxspider.net/download/badip.torexit')
24 * * * * run_cmd('download http://www.dxspider.net/download/badip.torrelay')
24 * * * * run_cmd('download http://www.dxspider.net/download/badip.global')
25 * * * * run_cmd('load/badip')

If you do use the crontab then *please* use a random minute between 15-40
and not all use minute 24.

Windows users may well find this particularly useful.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/download.pl){ .md-button }

## Verify on a running node

```text
HELP DOWNLOAD
```

Compare the installed handler with this page when local overrides or a different revision may be present.