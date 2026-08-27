# `SET/QRA`

<div class="command-hero" markdown>

**Set your QRA Grid locator**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/set/qra.pl){ .md-button }

## Verify on a running node

```text
HELP SET/QRA
```

The built-in help is useful when checking the exact command set installed on a particular node.