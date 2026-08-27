# `RBN`

<div class="command-hero" markdown>

**The Reverse Beacon or Skimmer System**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
RBN
```

**The Reverse Beacon or Skimmer System**

## Details

DXSpider now has the ability to show spots from the Reverse Beacon Network
or "Skimmers", if your sysop has enabled the feed(s) (and has the bandwidth
to both receive the feeds and also to pass them on to you.

Currently there are two RBN/Skimmer feeds available which, at busy
times can send up to 50,000 spots/hour EACH. Somewhere in the low
1000s is more normal. Clearly this is not much use to the average user
and so DXSpider "curates" them by removing duplicates and checking for
invalid callsigns or prefixes, as well as using some algorithms to fix
the rather variable frequencies that some skimmers produce
(particularly for CW spots).

This means that the format of the spot that you see is completely
different to the spots that the RBN feeds supply and, as a result of
the "curation" reduces the volume of spots to you by between 8 and 11
times.

See SET/SKIMMER (or SET/WANTRBN) for more information on enabling
RBN/Skimmer spots and also on selecting particular categories (e.g CW
or FT8/FT4) - which has the side benefit of reducing the volume of
spots that you receive even more!

Here are some examples of the output:

DX de LZ4UX-#:    14015.5 ON7TQ        CW   6dB Q:9 Z:5,14,15,40   14 0646Z 20
DX de VE7CC-#:     3573.0 N8ADO        FT8 -14dB Q:4 Z:4,5          4 0647Z  3
DX de DM7EE-#:    14027.5 R1AC         CW   9dB Q:9* Z:5,15,17,20  16 0643Z 14
DX de WE9V-#:      7074.0 EA7ALL       FT8 -9dB Q:2+ Z:5           14 0641Z  4

Note that UNSET/DXGRID, UNSET/DXITU and SET/DXCQ are in operation in
these examples. This is completely optional.

The comment field has been completely changed in order provide as much
information, in as smaller space, as possible. All the irrelevant
information has been removed.

You can use the Category (CW and FT8 in these examples) to with
SET/SKIMMER (or SET/WANTRBN) to, rather coarsely, select which spots
you require. You can refine this further by the use of Filtering. See
SET/SKIMMER or SET/WANTRBN for more information. But the short answer
is that these are spots and are filtered like any other spot, unless
you want to filter these spots differently, in which case you can use
REJECT/RBN and ACCEPT/RBN in exactly the same way as ACCEPT/SPOT and
REJECT/SPOT. If you don't use RBN filters then these spots will be
filter by any spot filters that you may have.

The next field (6dB, -14dB etc) is the LOWEST reported signal that was
heard.

The Q: field is the number of skimmers that heard this spot (up to 9
shown, but it could easily be many more). If Q: is > 1 (especially on
CW) then you can be reasonably certain that the callsign is accurate,
especially on CW. 'Q' stands for "Qualitee" :-)

If there is a '*', it means that there was a disagreement about
frequency. In fact, particularly for CW spots, I have see
disagreements of 600Hz. Which is a worry. The frequency that is shown
is the majority view of all the skimmers spotting this call. You may
have to fossick about the airwaves to find the actual frequency :-)

There are stations that are permanently on, like Beacons, and also
others that have long sessions on the same frequency and do a lot of
CQing. If they have been on for a certain length of time and they
reappear before their cache entry expires (about 2 hours), then they
are respotted. This is indicated by the '+'. NOTE - if they change
frequency, this will generate new spots. Each callsign/frequency pair
could respotted separately for as long as any individual
callsign/frequency pair remain in the cache.

The Z: field is present then that indicates the other CQ zones that
heard this spot - not including the skimmer that is shown. I show as
many as there are in whatever space is left in the comment
field. Note: if you have any of the optional flags around the time
then they may overwrite part of this field.

If there is NO filter in operation, then the skimmer spot with the
LOWEST signal strength will be shown. This implies that if any extra
Z: zones are shown, then the signal will be higher in those zones.

If you have a filter (for instance: ACCEPT/SPOT by_zone 14 and not
zone 14 or zone 14 and not by_zone 14) where '14' is your QTH CQ
zone. You will, instead be served with the lowest signal strength spot
that satisfies that filter. Incidentally, this particular style of
filter is quite useful for RBN spots, as it reduces the volume and is
likely to be more relevant for casual use. If this filter is too broad
(or narrow) for your normal spotting requirements, then you can use
ACCEPT/RBN with the same filter specification and it will only apply
to RBN spots. You can also replace '14' with a list like '14,15' if
you want to broaden it out. You will still get the same Z: list (if
any) whether you filter or not.

## Verify on a running node

```text
HELP RBN
```

The built-in help is useful when checking the exact command set installed on a particular node.