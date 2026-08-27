# `UNSET/PROMPT`

<div class="command-hero" markdown>

**Set your prompt back to default**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
UNSET/PROMPT
```

**Set your prompt back to default**

## Details

This command will set your user prompt to the string that you
say. The point of this command to enable a user to interface to programs
that are looking for a specific prompt (or else you just want a different
prompt).

```text
SET/PROMPT clx >
```

There are some substitutions that can be added to the prompt:

```text
%C - callsign [which will have ( and ) around it if not here]
%D - date
%T - time
%M - cluster 'mycall'
```

The standard prompt is defined as:

```text
SET/PROMPT %C de %M %D %T dxspider >
```

UNSET/PROMPT will undo the SET/PROMPT command and set your prompt back to
normal.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/unset/prompt.pl){ .md-button }

## Verify on a running node

```text
HELP UNSET/PROMPT
```

The built-in help is useful when checking the exact command set installed on a particular node.