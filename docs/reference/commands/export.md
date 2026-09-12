# `EXPORT`

<div class="command-hero" markdown>

**Export a message to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
EXPORT [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.
- It cannot be run from a command script.
- It must be run from a local connection.

## Command description

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

## Verify on a running node

```text
HELP EXPORT
```

Use the node help to check for local overrides or differences in another installed revision.