# `STAT/USER`

<div class="command-hero" markdown>

**Show the full status of a user**

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
STAT/USER [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`DXUser::get_current()`

### Argument parsing evidence

Source: `cmd/stat/user.pl` · SHA-256 `6cb1564e45efb74df8963a9c019aa0f6918d2db7757b76b395dfaecdc6264ead`

```perl
L7: my ($self, $line) = @_;
L8: my @list = split /\s+/, $line; # generate a list of callsigns
L9: @list = ($self->call) if !@list; # my channel if no callsigns
L13: foreach $call (@list) {
L25: push @out, "" if @list > 1;
```

### Output and error evidence

Source: `cmd/stat/user.pl` · SHA-256 `6cb1564e45efb74df8963a9c019aa0f6918d2db7757b76b395dfaecdc6264ead`

```perl
L23: push @out, "User: $call not found";
L25: push @out, "" if @list > 1;
L28: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
STAT/USER [<callsign>]
```

**Show the full status of a user**

## Details

Shows the full contents of a user record including all the secret flags
and stuff.

Only the fields that are defined (in perl term) will be displayed.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/stat/user.pl){ .md-button }

## Verify on a running node

```text
HELP STAT/USER
```

Compare the installed handler with this page when local overrides or a different revision may be present.