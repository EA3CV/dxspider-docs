# `SHOW/DXQSL`

<div class="command-hero" markdown>

**Show any QSL info gathered from spots**

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
SHOW/DXQSL [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`QSL::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/dxqsl.pl` · SHA-256 `84357d3005cc7dc43ea599966b5bf822845a1889cb9f0ea1c76aa9cb95bc7a01`

```perl
L9: my ($self, $line) = @_;
L10: my @call = split /\s+/, uc $line;
```

### Validation and access evidence

Source: `cmd/show/dxqsl.pl` · SHA-256 `84357d3005cc7dc43ea599966b5bf822845a1889cb9f0ea1c76aa9cb95bc7a01`

```perl
L15: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
```

### Output and error evidence

Source: `cmd/show/dxqsl.pl` · SHA-256 `84357d3005cc7dc43ea599966b5bf822845a1889cb9f0ea1c76aa9cb95bc7a01`

```perl
L15: return (1, $self->msg('db3', 'QSL')) unless $QSL::dbm;
L17: push @out, $self->msg('qsl1');
L23: push @out, sprintf "%-14s %-10s %4d %s %s", $c, $_->[0], $_->[1], cldatetime($_->[2]), $_->[3];
L27: push @out, $self->msg('db2', $call, 'QSL');
L31: return (1, @out);
```

### Message keys returned

`db2`, `db3`, `qsl1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
SHOW/DXQSL <callsign>
```

**Show any QSL info gathered from spots**

## Details

The node collects information from the comment fields in spots (things
like 'VIA EA7WA' or 'QSL-G1TLH') and stores these in a database.

This command allows you to interrogate that database and if the callsign
is found will display the manager(s) that people have spotted. This
information is NOT reliable, but it is normally reasonably accurate if
it is spotted enough times.

For example:-

```text
sh/dxqsl 4k9w
```

You can check the raw input spots yourself with:-

```text
sh/dx 4k9w qsl
```

This gives you more background information.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/dxqsl.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DXQSL
```

Compare the installed handler with this page when local overrides or a different revision may be present.