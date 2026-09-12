# `UNSET/EMAIL`

<div class="command-hero" markdown>

**Stop personal msgs being forwarded by email**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
UNSET/EMAIL [arguments; see parser evidence]
```

## Command description

```text
UNSET/EMAIL
```

**Stop personal msgs being forwarded by email**

## Details

If any personal messages come in for your callsign then you can use
these commands to control whether they are forwarded onto your email
address. To enable the forwarding do something like:-

```text
SET/EMAIL mike.tubby@somewhere.com
```

You can have more than one email address (each one separated by a space).
Emails are forwarded to all the email addresses you specify.

You can disable forwarding by:-

```text
UNSET/EMAIL
```

## Verify on a running node

```text
HELP UNSET/EMAIL
```

Use the node help to check for local overrides or differences in another installed revision.