# `SHOW/VHFTABLE`

<div class="command-hero" markdown>

**Show the VHF DX Spotter Table**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
SHOW/VHFTABLE [days] [date] [prefix ...]
```

**Show the VHF DX Spotter Table**

## Details

Show the VHF DX Spotter table for the list of prefixes for the last
<days> no of days (default is 31), starting from a date (default: today).

If there are no prefixes then it will show the table for your country.

Remember that some countries have more than one "DXCC country" in them
(eg G :-), to show them (assuming you are not in G already which is
specially treated in the code) you must list all the relevant prefixes

```text
sh/vhftable g gm gd gi gj gw gu
```

Note that the prefixes are converted into country codes so you don't have
to list all possible prefixes for each country.

If you want more or less days than the default simply include the
number you require:-

```text
sh/vhftable 20 pa
```

If you want to start at a different day, simply add the date in some
recognizable form:-

```text
sh/vhftable 2 25nov02
sh/vhftable 2 25-nov-02
sh/vhftable 2 021125
sh/vhftable 2 25/11/02
```

This will show the stats for your DXCC for that CQWW contest weekend.

You can specify either prefixes or full callsigns (so you can see how you
did against all your mates). You can also say 'all' which will then print
the worldwide statistics.

```text
sh/vhftable all
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/vhftable.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/VHFTABLE
```

The built-in help is useful when checking the exact command set installed on a particular node.