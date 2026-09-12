# `SET/QRA`

<div class="command-hero" markdown>

**Set your QRA Grid locator**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/QRA [arguments; see parser evidence]
```

## Command description

```text
SET/QRA <locator>
```

**Set your QRA Grid locator**

## Details

Tell the system what your QRA (or Maidenhead) locator is. If you have not
done a SET/LOCATION then your latitude and longitude will be set roughly
correctly (assuming your locator is correct ;-). For example:-
```text
SET/QRA JO02LQ
```

## Verify on a running node

```text
HELP SET/QRA
```

Use the node help to check for local overrides or differences in another installed revision.