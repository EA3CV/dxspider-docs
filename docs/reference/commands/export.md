# `EXPORT`

<div class="command-hero" markdown>

**Export a message to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
EXPORT <msgno> <filename>
```

**Export a message to a file**

## Details

Export a message to a file. This command can only be executed on a local
console with a fully privileged user. The file produced will be in a form
ready to be imported back into the cluster by placing it in the import
directory (/spider/msg/import).

This command cannot overwrite an existing file. This is to provide some
measure of security. Any files written will owned by the same user as the
main cluster, otherwise you can put the new files anywhere the cluster can
access. For example:-

```text
EXPORT 2345 /tmp/a
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/export.pl){ .md-button }

## Verify on a running node

```text
HELP EXPORT
```

The built-in help is useful when checking the exact command set installed on a particular node.