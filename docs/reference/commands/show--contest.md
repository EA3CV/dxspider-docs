# `SHOW/CONTEST`

<div class="command-hero" markdown>

**Show all the contests for a month**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/CONTEST [arguments; see parser evidence]
```

### Available options and values

`mai`, `maj`, `okt`

The valid combinations are described in the command forms and examples below.

## Command description

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

## Verify on a running node

```text
HELP SHOW/CONTEST
```

Use the node help to check for local overrides or differences in another installed revision.