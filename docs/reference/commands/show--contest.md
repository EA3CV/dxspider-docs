# `SHOW/CONTEST`

<div class="command-hero" markdown>

**Show all the contests for a month**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/CONTEST [<year>] [<month>]
```

**Show all the contests for a month**

## Details

Show all known contests which are maintained at http://www.sk3bg.se/contest/
for a particular month or year. The format is reasonably flexible.
For example:-

```text
SH/CONTEST
SH/CONTEST mar
SH/CONTEST mar 13
SH/CONTEST 13 march
```

If there is no month/year then the current month's contests are shown.

Note that it expects ENGLISH (jan/feb/mar/apr/may/jun/jul/aug/sep/oct/nov/dec)
month names.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/contest.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/CONTEST
```

The built-in help is useful when checking the exact command set installed on a particular node.