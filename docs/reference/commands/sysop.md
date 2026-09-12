# `SYSOP`

<div class="command-hero" markdown>

**Regain your privileges if you login remotely**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SYSOP [arguments; see parser evidence]
```

## Command description

```text
SYSOP
```

**Regain your privileges if you login remotely**

## Details

The system automatically reduces your privilege level to that of a
normal user if you login in remotely. This command allows you to
regain your normal privilege level. It uses the normal system: five
numbers are returned that are indexes into the character array that is
your assigned password (see SET/PASSWORD). The indexes start from
zero.

You are expected to return a string which contains the characters
required in the correct order. You may intersperse those characters
with others to obscure your reply for any watchers. For example (and
these values are for explanation :-):

```text
password = 012345678901234567890123456789
> sysop
22 10 15 17 3
```
you type:-
 aa2bbbb0ccc5ddd7xxx3n
 or 2 0 5 7 3
 or 20573

They will all match. If there is no password you will still be offered
numbers but nothing will happen when you input a string. Any match is
case sensitive.

## Verify on a running node

```text
HELP SYSOP
```

Use the node help to check for local overrides or differences in another installed revision.