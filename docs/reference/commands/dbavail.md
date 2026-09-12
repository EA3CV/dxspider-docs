# `DBAVAIL`

<div class="command-hero" markdown>

**Show a list of all the Databases in the system**

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
DBAVAIL [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/dbavail.pl` · SHA-256 `a47836ea9faad17748bb9371521af4595591b332ac54e4d45a6834b647c6540d`

```perl
L7: my ($self, $line) = @_;
```

### Output and error evidence

Source: `cmd/dbavail.pl` · SHA-256 `a47836ea9faad17748bb9371521af4595591b332ac54e4d45a6834b647c6540d`

```perl
L13: push @out, $self->msg('db12') unless @out;
L14: push @out, sprintf "%-15s %-10s %-15s %s", $f->name, $f->remote ? $f->remote : $self->msg('local1'), ($f->localcmd || ""), $f->chain ? parray($f->chain) : "";
L16: return (1, @out);
```

### Message keys returned

`db12`, `local1`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
DBAVAIL
```

**Show a list of all the Databases in the system**

## Details

Title says it all really, this command lists all the databases defined
in the system. It is also aliased to SHOW/COMMAND.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/dbavail.pl){ .md-button }

## Verify on a running node

```text
HELP DBAVAIL
```

Compare the installed handler with this page when local overrides or a different revision may be present.