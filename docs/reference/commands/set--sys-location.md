# `SET/SYS_LOCATION`

<div class="command-hero" markdown>

**Set your cluster latitude and longitude**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SET/SYS_LOCATION [arguments; see parser evidence]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.

## Command description

```text
SET/SYS_LOCATION <lat & long>
```

**Set your cluster latitude and longitude**

## Details

In order to get accurate headings and such like you must tell the system
what your latitude and longitude is. If you have not yet done a SET/QRA
then this command will set your QRA locator for you. For example:-
```text
SET/LOCATION 52 22 N 0 57 E
```

## Verify on a running node

```text
HELP SET/SYS_LOCATION
```

Use the node help to check for local overrides or differences in another installed revision.