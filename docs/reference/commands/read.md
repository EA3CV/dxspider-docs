# `READ`

<div class="command-hero" markdown>

**Read the next unread personal message addressed to you**

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
READ [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg->alloc()`, `DXMsg::add_dir()`, `DXMsg::get()`, `DXMsg::get_all()`, `DXMsg::next_transno()`, `DXMsg::queue_msg()`, `ref->read()`, `ref->store()`, `rref->gotit()`, `rref->msgno()`, `rref->store()`, `self->lastread()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/read.pl` · SHA-256 `36e195939d1dcc52ff0ae4aefa3c9a9a9c60d02e72169c7e6a379aeb3027c43a`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
L53: $sub = "Re: $sub" unless $sub =~ /^\s*re:/i;
```

### Validation and access evidence

Source: `cmd/read.pl` · SHA-256 `36e195939d1dcc52ff0ae4aefa3c9a9a9c60d02e72169c7e6a379aeb3027c43a`

```perl
L20: if ($ref->to eq $self->call && $ref->private && !$ref->read && !$ref->delete) {
L27: return (1, $self->msg('read1')) if @f == 0;
L35: if ($self->priv < 5 && $ref->private && $ref->to ne $self->call && $ref->from ne $self->call ) {
L45: unless ($ref->private && $ref->to ne $self->call) {
L53: $sub = "Re: $sub" unless $sub =~ /^\s*re:/i;
```

### Output and error evidence

Source: `cmd/read.pl` · SHA-256 `36e195939d1dcc52ff0ae4aefa3c9a9a9c60d02e72169c7e6a379aeb3027c43a`

```perl
L27: return (1, $self->msg('read1')) if @f == 0;
L32: push @out, $self->msg('read2', $msgno);
L36: push @out, $self->msg('read3', $msgno);
L39: push @out, sprintf "Msg: %d From: %s Date: %6.6s %5.5s Subj: %-30.30s", $msgno,
L42: push @out, @body;
L71: return (1, @out);
```

### Message keys returned

`read1`, `read2`, `read3`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    READ
    ```

    **Read the next unread personal message addressed to you**


=== "Help variant"

    ```text
    READ <msgno>
    ```

    **Read the specified message**

    You can read any messages that are sent as 'non-personal' and also any
    message either sent by or sent to your callsign.

=== "Help variant"

    ```text
    READ-
    ```

    ****

    As a sysop you may read any message on the system

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/read.pl){ .md-button }

## Verify on a running node

```text
HELP READ
```

Compare the installed handler with this page when local overrides or a different revision may be present.