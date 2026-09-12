# `CATCHUP`

<div class="command-hero" markdown>

**Mark a message as sent**

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
CATCHUP [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXMsg::get()`, `DXMsg::get_all()`, `DXUser::get_current()`, `ref->read_msg_body()`, `ref->store()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/catchup.pl` · SHA-256 `004e075318aa56e27bae35137716859489e881124279a04473abdc461eff9d5c`

```perl
L12: my ($self, $line) = @_;
L15: my @f = split /\s+/, $line;
L18: my $call = uc shift @f;
L28: if ($msgno =~ /^al/i) {
L31: } elsif (my ($f, $t) = $msgno =~ /(\d+)-(\d+)/) {
```

### Validation and access evidence

Source: `cmd/catchup.pl` · SHA-256 `004e075318aa56e27bae35137716859489e881124279a04473abdc461eff9d5c`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L28: if ($msgno =~ /^al/i) {
L47: next if $ref->{private};
```

### Output and error evidence

Source: `cmd/catchup.pl` · SHA-256 `004e075318aa56e27bae35137716859489e881124279a04473abdc461eff9d5c`

```perl
L13: return (1, $self->msg('e5')) if $self->priv < 5;
L16: return (1, "usage: catchup <node call> all|[<msgno ...]") unless @f >= 2;
L20: return (1, "$call not a node") unless $user && $user->sort ne 'U';
L39: push @out, $self->msg('m13', $msgno);
L51: push @out, $self->msg('m14', $ref->{msgno}, $call);
L55: return (1, @out);
```

### Message keys returned

`e5`, `m13`, `m14`

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
CATCHUP <node call> All|[<msgno> ...]
```

**Mark a message as sent**

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/catchup.pl){ .md-button }

## Verify on a running node

```text
HELP CATCHUP
```

Compare the installed handler with this page when local overrides or a different revision may be present.