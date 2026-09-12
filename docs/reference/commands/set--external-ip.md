# `SET/EXTERNAL_IP`

<div class="command-hero" markdown>

**my $new = find_external_ipaddr();**

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
SET/EXTERNAL_IP
```

No command arguments are consumed by this handler.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Important calls

`UserAgent->new()`, `chan->hostname()`, `self->msg()`, `self->send()`, `ua->get()`

### Argument parsing evidence

Source: `cmd/set/external_ip.pl` · SHA-256 `6b6d2739b4dcff8834db028f78b2b099b3486b4472e1b15ca5c0034a09a6b4c8`

```perl
L5: my $self = shift;
L9: my $new = shift;
L39: $old = '127.0.0.1' if $old =~/localhost/;
```

### Validation and access evidence

Source: `cmd/set/external_ip.pl` · SHA-256 `6b6d2739b4dcff8834db028f78b2b099b3486b4472e1b15ca5c0034a09a6b4c8`

```perl
L6: return (1, $self->msg('e5')) if $self->priv < 8 && $self != $main::me;
L39: $old = '127.0.0.1' if $old =~/localhost/;
```

### Output and error evidence

Source: `cmd/set/external_ip.pl` · SHA-256 `6b6d2739b4dcff8834db028f78b2b099b3486b4472e1b15ca5c0034a09a6b4c8`

```perl
L6: return (1, $self->msg('e5')) if $self->priv < 8 && $self != $main::me;
L11: push @out, "$new is not a valid IP address (DNS names not allowed), ignored" if $new && !is_ipaddr($new);
L12: push @out, "$new is a local address, ignored" if is_rfc1918($new);
L15: $self->send($_) for @out;
L29: push @out, "set/external_ip: error getting http://ifconfig.me/ip " . res->message;
L45: push @out, "set/external_ip: Changed $main::mycall IP address from $old -> $new";
L47: push @out, "set/external_ip: $old no IP address change for $main::mycall required";
L51: $self->send($_) for @out;
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/set/external_ip.pl){ .md-button }

## Verify on a running node

```text
HELP SET/EXTERNAL_IP
```

Compare the installed handler with this page when local overrides or a different revision may be present.