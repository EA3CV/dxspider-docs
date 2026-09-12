# `UNSET/PROMPT`

<div class="command-hero" markdown>

**Set your prompt back to default**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/PROMPT [arguments; see parser evidence]
```

## Command description

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

## Verify on a running node

```text
HELP UNSET/PROMPT
```

Use the node help to check for local overrides or differences in another installed revision.