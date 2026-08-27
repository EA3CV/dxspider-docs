# `SHOW/DX`

<div class="command-hero" markdown>

**Search the spot database by band, frequency, callsign, age, spotter, country, zone, state, origin, IP address and other selectors.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>DX spots</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/DX
```

**Interrogate the spot database**

## Details

If you just type SHOW/DX you will get the last so many spots
(sysop configurable, but usually 10).

In addition you can add any number of these commands in very nearly
any order to the basic SHOW/DX command, they are:-

 on <band>       - eg 160m 20m 2m 23cm 6mm
 on <region>     - eg hf vhf uhf shf      (see SHOW/BANDS)
 on <from>/<to>  - eg 1000/4000 14000-30000  (in Khz)
```text
  <from>-<to>
```

 <number>        - the number of spots you want
 <from>-<to>     - <from> spot no <to> spot no in the selected list
 <from>/<to>

 <prefix>        - for a spotted callsign beginning with <prefix>
 *<suffix>       - for a spotted callsign ending in <suffix>
 *<string>*      - for a spotted callsign containing <string>
 <call> exact    - for a spotted callsign *exactly* as typed.

 day <number>    - starting <number> days ago
 day <from>-<to> - <from> days <to> days ago
```text
   <from>/<to>
```

 info <text>     - any spots containing <text> in the info or remarks

 by <call>       - any spots spotted by <call> (spotter <call> is the
```text
                 same).
```

 qsl             - this automatically looks for any qsl info on the call
```text
                 held in the spot database.
```

 iota [<iota>]   - If the iota island number is missing it will look for
```text
                the string iota and anything which looks like an iota
                island number. If you specify then it will look for
                that island.
```

 qra [<locator>] - this will look for the specific locator if you specify
```text
                 one or else anything that looks like a locator.
```

 dxcc            - treat the prefix as a 'country' and look for spots
```text
                 from that country regardless of actual prefix.
                 eg dxcc oq2
```

```text
                 You can also use this with the 'by' keyword so
                 eg by W dxcc
```

 real or rt      - Format the output the same as for real time spots. The
```text
                 formats are deliberately different (so you can tell
                 one sort from the other). This is useful for some
                 logging programs that can't cope with normal sh/dx
                 output. An alias of SHOW/FDX is available.
```

 filter          - Filter the spots, before output, with the user's
```text
                 spot filter. An alias of SHOW/MYDX is available.
```

 zone <zones>    - look for spots in the cq zone (or zones) specified.
```text
                 zones are numbers separated by commas.
```

 by_zone <zones> - look for spots spotted by people in the cq zone
```text
                 specified.
```

 itu <itus>      - look for spots in the itu zone (or zones) specified
```text
                 itu zones are numbers separated by commas.
```

 by_itu <itus>   - look for spots spotted by people in the itu zone
```text
                 specified.
```

 state <list>    - look for spots in the US state (or states) specified
```text
                 The list is two letter state codes separated by commas.
```

 by_state <list> - look for spots spotted by people in the US state
```text
                 specified.
```

 origin          - the node from which this spot originated (must be an
```text
                 exact callsign with SSID e.g. gb7tlh-4)
```

 ip              - the IP address of the spotter (either in IPV4 or IPV6)
```text
                 format. These addresses can be partial.
```

 e.g.

```text
 SH/DX 9m0
 SH/DX on 20m info iota
 SH/DX 9a on vhf day 30
 SH/DX rf1p qsl
 SH/DX iota
 SH/DX iota eu-064
 SH/DX qra jn86
 SH/DX dxcc oq2
 SH/DX dxcc oq2 by w dxcc
 SH/DX zone 4,5,6
 SH/DX by_zone 4,5,6
 SH/DX state in,oh
 SH/DX by_state in,oh
 SH/DX hb2008g exact
 SH/DX origin gb7tlh-4
 SH/DX ip 82.65.128.4       (or SH/DX ip 2a00:1450:4009:800::200e)
```

## When would I use this?

SHOW/DX is much more than “show the last spots”: its selectors can be combined to answer very specific questions.

## Practical examples

### Last spots

```text
SHOW/DX
```

### 20 m spots mentioning IOTA

```text
SHOW/DX ON 20M INFO IOTA
```

### VHF spots for calls beginning with 9A from the last 30 days

```text
SHOW/DX 9A ON VHF DAY 30
```

### Exact callsign only

```text
SHOW/DX HB2008G EXACT
```

### Spots for CQ zones 4, 5 and 6

```text
SHOW/DX ZONE 4,5,6
```

### Spots made by stations in CQ zones 4, 5 and 6

```text
SHOW/DX BY_ZONE 4,5,6
```

### US states Indiana and Ohio

```text
SHOW/DX STATE IN,OH
```

### Filter by origin node

```text
SHOW/DX ORIGIN GB7TLH-4
```

### Filter by spotter IP

```text
SHOW/DX IP 82.65.128.4
```

### IOTA search

```text
SHOW/DX IOTA EU-064
```

### Locator search

```text
SHOW/DX QRA JN86
```

### Country search

```text
SHOW/DX DXCC OQ2
```

### Apply your personal spot filter

```text
SHOW/MYDX
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/dx.pl){ .md-button }

## Related commands

- [`SHOW/MYDX`](show--mydx.md)
- [`SHOW/DXCC`](show--dxcc.md)
- [`SHOW/FDX`](show--fdx.md)
- [`DX`](dx.md)
- [`ACCEPT/SPOTS`](accept--spots.md)
- [`REJECT/SPOTS`](reject--spots.md)

## Verify on a running node

```text
HELP SHOW/DX
```

The built-in help is useful when checking the exact command set installed on a particular node.