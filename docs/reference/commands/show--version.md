# `SHOW/VERSION`

<div class="command-hero" markdown>

**show the version number of the software + copyright info $DB::single=1;**

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
SHOW/VERSION [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses or emits DX protocol data.

### Important calls

`Route::Node::get_all()`

### Argument parsing evidence

Source: `cmd/show/version.pl` · SHA-256 `109fc512bea713c79fe3693c2b8c481fe216a6463f4c121cd4a4bbd98c54c4cd`

```perl
L9: my ($self, $line) = @_;
L11: my @in = map {uc} split /\s+/, $line;
L17: my @n = sort {$a->call cmp $b->call} grep {$_->call =~ /^(?:$q)/} Route::Node::get_all();
```

### Validation and access evidence

Source: `cmd/show/version.pl` · SHA-256 `109fc512bea713c79fe3693c2b8c481fe216a6463f4c121cd4a4bbd98c54c4cd`

```perl
L13: if ($self->priv > 5 && @in) {
```

### Output and error evidence

Source: `cmd/show/version.pl` · SHA-256 `109fc512bea713c79fe3693c2b8c481fe216a6463f4c121cd4a4bbd98c54c4cd`

```perl
L18: push @out, " Node Version Build PC9X via PC92";
L20: push @out, sprintf " %-10s %5s %5s %3s %3s", $n->call, $n->version, $n->build, yesno($n->do_pc9x), yesno($n->via_pc92);
L22: push @out, ' ' . scalar @n . " Nodes found";
L26: push @out, "DXSpider v$main::version (build $main::build git: $main::gitbranch/$main::gitversion) using perl $^V on \u$^O";
L27: push @out, "Copyright (c) 1998-$year Dirk Koopman G1TLH";
L31: return (1, @out);
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/version.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/VERSION
```

Compare the installed handler with this page when local overrides or a different revision may be present.