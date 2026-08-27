# `LOAD/MESSAGES`

<div class="command-hero" markdown>

**Reload the system messages file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
LOAD/MESSAGES
```

**Reload the system messages file**

## Details

If you change the /spider/perl/Messages file (usually whilst
fiddling/writing new commands) you can have them take effect during a
cluster session by executing this command. You need to do this if get
something like :-

unknown message 'xxxx' in lang 'en'

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/load/messages.pl){ .md-button }

## Verify on a running node

```text
HELP LOAD/MESSAGES
```

The built-in help is useful when checking the exact command set installed on a particular node.