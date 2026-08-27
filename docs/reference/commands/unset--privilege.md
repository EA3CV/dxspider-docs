# `UNSET/PRIVILEGE`

<div class="command-hero" markdown>

**Remove any privilege for this session**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/PRIVILEGE
```

**Remove any privilege for this session**

## Details

You can use this command to 'protect' this session from unauthorised
use. If you want to get your normal privilege back you will need to
either logout and login again (if you are on a console) or use the
SYSOP command.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/privilege.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PRIVILEGE
```

The built-in help is useful when checking the exact command set installed on a particular node.