# `EXPORT`

<div class="command-hero" markdown>

**Export a message to a file**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
EXPORT [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.
- The handler restricts execution from scripts.
- The handler requires a local connection context.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::get()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/export.pl` · SHA-256 `efc5994b1314f54996d225d07a36a78e94d8d79ccc432644f9c277134565381f`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
L19: return (1, $self->msg("export1")) unless @f == 2 && $f[0] =~ /^\d+$/;
```

### Validation and access evidence

Source: `cmd/export.pl` · SHA-256 `efc5994b1314f54996d225d07a36a78e94d8d79ccc432644f9c277134565381f`

```perl
L17: return (1, $self->msg("e5")) if $self->priv < 9 || $self->consort ne 'local' || $self->remotecmd || $self->inscript;
L19: return (1, $self->msg("export1")) unless @f == 2 && $f[0] =~ /^\d+$/;
L24: return (1, $self->msg('read2', $msgno)) unless $ref;
L32: return (1, $self->msg('e16', $fn)) if -e $fn;
```

### Output and error evidence

Source: `cmd/export.pl` · SHA-256 `efc5994b1314f54996d225d07a36a78e94d8d79ccc432644f9c277134565381f`

```perl
L17: return (1, $self->msg("e5")) if $self->priv < 9 || $self->consort ne 'local' || $self->remotecmd || $self->inscript;
L19: return (1, $self->msg("export1")) unless @f == 2 && $f[0] =~ /^\d+$/;
L24: return (1, $self->msg('read2', $msgno)) unless $ref;
L26: my $m = $self->msg('e16', $fn);
L29: return (1, $m);
L32: return (1, $self->msg('e16', $fn)) if -e $fn;
L45: $m = $self->msg('export3', $msgno, $fn, $self->call);
L47: $m = $self->msg('export2', $msgno, $fn, $!, $self->call);
L51: push @out, $m;
L53: return (1, @out);
```

### Message keys returned

`e16`, `e5`, `export1`, `export2`, `export3`, `read2`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
EXPORT <msgno> <filename>
```

**Export a message to a file**

## Details

Export a message to a file. This command can only be executed on a local
console with a fully privileged user. The file produced will be in a form
ready to be imported back into the cluster by placing it in the import
directory (/spider/msg/import).

This command cannot overwrite an existing file. This is to provide some
measure of security. Any files written will owned by the same user as the
main cluster, otherwise you can put the new files anywhere the cluster can
access. For example:-

```text
EXPORT 2345 /tmp/a
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/export.pl){ .md-button }

## Verify on a running node

```text
HELP EXPORT
```

Compare the installed handler with this page when local overrides or a different revision may be present.