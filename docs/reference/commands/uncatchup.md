# `UNCATCHUP`

<div class="command-hero" markdown>

**Unmark a message as sent**

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
UNCATCHUP [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::get()`, `DXMsg::get_all()`, `DXUser::get_current()`, `ref->read_msg_body()`, `ref->store()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/uncatchup.pl` · SHA-256 `5c12a910dd1c850b7de9b02900480c70cd4582b390e40780ed40cf305f13eb3b`

```perl
L12: my ($self, $line) = @_;
L15: my @f = split /\s+/, $line;
L18: my $call = uc shift @f;
L28: if ($msgno =~ /^al/oi) {
L31: } elsif (my ($f, $t) = $msgno =~ /(\d+)-(\d+)/) {
```

### Validation and access evidence

Source: `cmd/uncatchup.pl` · SHA-256 `5c12a910dd1c850b7de9b02900480c70cd4582b390e40780ed40cf305f13eb3b`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L28: if ($msgno =~ /^al/oi) {
L47: next if $ref->{private};
```

### Output and error evidence

Source: `cmd/uncatchup.pl` · SHA-256 `5c12a910dd1c850b7de9b02900480c70cd4582b390e40780ed40cf305f13eb3b`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L16: return (1, "usage: catchup <node call> all|[<msgno ...]") unless @f >= 2;
L20: return (1, "$call not a node") unless $user && $user->sort ne 'U';
L39: push @out, $self->msg('m13', $msgno);
L51: push @out, $self->msg('m15', $ref->{msgno}, $call);
L55: return (1, @out);
```

### Message keys returned

`e5`, `m13`, `m15`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
UNCATCHUP <node call> All|[msgno> ...]
```

**Unmark a message as sent**

## Details

When you send messages the fact that you have forwarded it to another node
is remembered so that it isn't sent again. When you have a new partner
node and you add their callsign to your /spider/msg/forward.pl file, all
outstanding non-private messages will be forwarded to them. This may well
be ALL the non-private messages. You can prevent this by using these
commmands:-

```text
catchup GB7DJK all
catchup GB7DJK 300 301 302 303 500-510
```

and to undo what you have just done:-

```text
uncatchup GB7DJK all
uncatchup GB7DJK 300 301 302 303 500-510
```

which will arrange for them to be forward candidates again.

Order is not important.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/uncatchup.pl){ .md-button }

## Verify on a running node

```text
HELP UNCATCHUP
```

Compare the installed handler with this page when local overrides or a different revision may be present.