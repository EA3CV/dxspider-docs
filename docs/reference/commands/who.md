# `WHO`

<div class="command-hero" markdown>

**Show who is physically connected**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-user">No direct handler guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
WHO
```

No command arguments are consumed by this handler.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`conn->isa()`, `dxchan->call()`

### Argument parsing evidence

Source: `cmd/who.pl` · SHA-256 `4a53bbecdba885b1d5201ee76e6e8936bcd0b19ac218f9b3f73bf885aafebf60`

```perl
L10: my $self = shift;
```

### Output and error evidence

Source: `cmd/who.pl` · SHA-256 `4a53bbecdba885b1d5201ee76e6e8936bcd0b19ac218f9b3f73bf885aafebf60`

```perl
L14: push @out, " Callsign Type State Started Name Ave RTT Link";
L43: push @out, sprintf "%10s $type $sort %-8.8s $t %-10.10s $ping $ip", $call, $state, $name;
L46: return (1, @out)
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
WHO
```

**Show who is physically connected**

## Details

This is a quick listing that shows which callsigns are connected and
what sort of connection they have

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/who.pl){ .md-button }

## Verify on a running node

```text
HELP WHO
```

Compare the installed handler with this page when local overrides or a different revision may be present.