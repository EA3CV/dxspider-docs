# `PRIVILEGE`

<div class="command-hero" markdown>

**check the privilege of the user is at least n**

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
PRIVILEGE [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Important calls

`self->msg()`

### Argument parsing evidence

Source: `cmd/privilege.pl` · SHA-256 `25414ac7a532ed47dac8febc1fd82313dd3507281faf8e9cecf02230942da77d`

```perl
L9: my ($self, $line) = @_;
L11: $line = '1' unless defined $line;
L12: push @out, $self->msg('e5') unless $line =~ /^\d+$/ && $self->priv >= $line;
```

### Validation and access evidence

Source: `cmd/privilege.pl` · SHA-256 `25414ac7a532ed47dac8febc1fd82313dd3507281faf8e9cecf02230942da77d`

```perl
L11: $line = '1' unless defined $line;
L12: push @out, $self->msg('e5') unless $line =~ /^\d+$/ && $self->priv >= $line;
```

### Output and error evidence

Source: `cmd/privilege.pl` · SHA-256 `25414ac7a532ed47dac8febc1fd82313dd3507281faf8e9cecf02230942da77d`

```perl
L12: push @out, $self->msg('e5') unless $line =~ /^\d+$/ && $self->priv >= $line;
L13: return (1, @out);
```

### Message keys returned

`e5`

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/privilege.pl){ .md-button }

## Verify on a running node

```text
HELP PRIVILEGE
```

Compare the installed handler with this page when local overrides or a different revision may be present.