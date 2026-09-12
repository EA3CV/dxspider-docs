# `LOAD/MESSAGES`

<div class="command-hero" markdown>

**Reload the system messages file**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
LOAD/MESSAGES
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

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

## Verify on a running node

```text
HELP LOAD/MESSAGES
```

Use the node help to check for local overrides or differences in another installed revision.