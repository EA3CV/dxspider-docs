# `GET/KEPS`

<div class="command-hero" markdown>

**Obtain the latest AMSAT Keplarian Elements from the web**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

```text
GET/KEPS
```

**Obtain the latest AMSAT Keplarian Elements from the web**

## Details

There are various ways that one can obtain the AMSAT keps. Traditionally the
regular method was to get on the mailing list and then arrange for the email
to be piped into convkeps.pl and arrange from the crontab to run LOAD/KEPS.
For various reasons, it was quite easy for one to be silently dropped
from this mailing list.

With the advent of asynchronous (web) connections in DXSpider it is now
possible to use this command to get the latest keps direct from the
AMSAT web site. One can do this from the command line or one can add a line
in the local DXSpider crontab file to do periodically (say once a week).

This command will clear out the existing keps and then run LOAD/KEPS
for you (but only) after a successful download from the AMSAT website.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/get/keps.pl){ .md-button }

## Verify on a running node

```text
HELP GET/KEPS
```

The built-in help is useful when checking the exact command set installed on a particular node.