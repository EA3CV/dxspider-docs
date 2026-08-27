# `FILTERING...`

<div class="command-hero" markdown>

**Filtering things in DXSpider**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
FILTERING...
```

**Filtering things in DXSpider**

## Details

There are a number of things you can filter in the DXSpider system. They
all use the same general mechanism.

In general terms you can create a 'reject' or an 'accept' filter which
can have up to 10 lines in it. You do this using, for example:-

```text
accept/spots .....
reject/spots .....
```

where ..... are the specific commands for that type of filter. There
are filters for spots, wwv, announce, wcy and (for sysops)
connects. See each different accept or reject command reference for
more details.

There is also a command to clear out one or more lines in a filter and
one to show you what you have set. They are:-

```text
clear/spots 1
clear/spots all
```

and

```text
show/filter
```

There is clear/xxxx command for each type of filter.

For now we are going to use spots for the examples, but you can apply
the principles to all types of filter.

There are two main types of filter 'accept' or 'reject'; which you use
depends entirely on how you look at the world and what is least
writing to achieve what you want. Each filter has 10 lines (of any
length) which are tried in order. If a line matches then the action
you have specified is taken (ie reject means ignore it and accept
means gimme it).

The important thing to remember is that if you specify a 'reject'
filter (all the lines in it say 'reject/spots' (for instance)) then if
a spot comes in that doesn't match any of the lines then you will get
it BUT if you specify an 'accept' filter then any spots that don't
match are dumped. For example if I have a one line accept filter:-

```text
accept/spots on vhf and (by_zone 14,15,16 or call_zone 14,15,16)
```

then automatically you will ONLY get VHF spots from or to CQ zones 14
15 and 16.  If you set a reject filter like:

```text
reject/spots on hf/cw
```

Then you will get everything EXCEPT HF CW spots, If you am interested in IOTA
and will work it even on CW then you could say:-

```text
reject/spots on hf/cw and not info iota
```

But in that case you might only be interested in iota and say:-

```text
accept/spots not on hf/cw or info iota
```

which is exactly the same. You should choose one or the other until
you are confortable with the way it works. Yes, you can mix them
(actually you can have an accept AND a reject on the same line) but
don't try this at home until you can analyse the results that you get
without ringing up the sysop for help.

Another useful addition now is filtering by US state

```text
accept/spots by_state VA,NH,RI,ME
```

You can arrange your filter lines into logical units, either for your
own understanding or simply convenience. I have one set frequently:-

```text
reject/spots 1 on hf/cw
reject/spots 2 on 50000/1400000 not (by_zone 14,15,16 or call_zone 14,15,16)
```

What this does is to ignore all HF CW spots (being a class B I can't
read any CW and couldn't possibly be interested in HF :-) and also
rejects any spots on VHF which don't either originate or spot someone
in Europe.

This is an exmaple where you would use the line number (1 and 2 in
this case), if you leave the digit out, the system assumes '1'. Digits
'0'-'9' are available.

You can leave the word 'and' out if you want, it is implied. You can
use any number of brackets to make the 'expression' as you want
it. There are things called precedence rules working here which mean
that you will NEED brackets in a situation like line 2 because,
without it, will assume:-

```text
(on 50000/1400000 and by_zone 14,15,16) or call_zone 14,15,16
```

annoying, but that is the way it is. If you use OR - use
brackets. Whilst we are here CASE is not important. 'And BY_Zone' is
just 'and by_zone'.

If you want to alter your filter you can just redefine one or more
lines of it or clear out one line. For example:-

```text
reject/spots 1 on hf/ssb
```

or

```text
clear/spots 1
```

To remove the filter in its entirty:-

```text
clear/spots all
```

There are similar CLEAR commands for the other filters:-

```text
clear/announce
clear/wcy
clear/wwv
```

ADVANCED USERS:-

Once you are happy with the results you get, you may like to experiment.

my example that filters hf/cw spots and accepts vhf/uhf spots from EU
can be written with a mixed filter, eg:

```text
rej/spot on hf/cw
acc/spot on 0/30000
acc/spot 2 on 50000/1400000 and (by_zone 14,15,16 or call_zone 14,15,16)
```

each filter slot actually has a 'reject' slot and an 'accept'
slot. The reject slot is executed BEFORE the accept slot.

It was mentioned earlier that after a reject test that doesn't match,
the default for following tests is 'accept', the reverse is true for
'accept'. In the example what happens is that the reject is executed
first, any non hf/cw spot is passed to the accept line, which lets
thru everything else on HF.

The next filter line lets through just VHF/UHF spots from EU.

## Verify on a running node

```text
HELP FILTERING...
```

The built-in help is useful when checking the exact command set installed on a particular node.