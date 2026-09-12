# `SHOW/QRZ`

<div class="command-hero" markdown>

**Show any callbook details on a callsign**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User / general</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/QRZ [arguments; see parser evidence]
```

### Available options and values

`addr2`, `ADIF`, `blank`, `call`, `country`, `county`, `dxcc`, `Error`, `fname`, `go`, `grid`, `lat`, `lon`, `moddate`, `name`, `qslmgr`, `state`

The valid combinations are described in the command forms and examples below.

## Command description

```text
SHOW/QRZ <callsign>
```

**Show any callbook details on a callsign**

## Details

This command queries the QRZ callbook server on the internet
and returns any information available for that callsign. This service
is provided for users of this software by http://www.qrz.com

See also SHOW/WM7D for an alternative.

## Verify on a running node

```text
HELP SHOW/QRZ
```

Use the node help to check for local overrides or differences in another installed revision.