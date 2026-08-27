# `EXPORT_USERS`

<div class="command-hero" markdown>

**Export the users database to ascii**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/export_users.pl){ .md-button }

## Verify on a running node

```text
HELP EXPORT_USERS
```

The built-in help is useful when checking the exact command set installed on a particular node.