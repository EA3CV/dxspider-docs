# `DOWNLOAD`

<div class="command-hero" markdown>

**Download a file into local_data**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/download.pl){ .md-button }

## Verify on a running node

```text
HELP DOWNLOAD
```

The built-in help is useful when checking the exact command set installed on a particular node.