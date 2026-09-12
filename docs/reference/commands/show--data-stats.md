# `SHOW/DATA_STATS`

<div class="command-hero" markdown>

**show the users on this cluster from the routing tables**

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
SHOW/DATA_STATS [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Observable implementation effects

- Uses the internal message subsystem.

### Important calls

`DXChannel::get()`, `DXChannel::get_all()`, `DXChannel::get_all_node_calls()`, `DXChannel::get_all_user_calls()`

### Argument parsing evidence

Source: `cmd/show/data_stats.pl` · SHA-256 `df35de23bf469668da870da0ca8f6b49a6913fd2a590cbf4a325dd422fcf5735`

```perl
L11: my ($self, $line) = @_;
L12: my @in = map { uc } split /\s+/, $line; # list of callsigns of nodes
L14: my @list;
L17: @list = keys %DXChannel::channels;
L20: my $in = shift @in;
L21: if ($in =~ /^NOD/){
L22: push @list, DXChannel::get_all_node_calls();
L23: } elsif ($in =~ /^USE/) {
L24: push @list, DXChannel::get_all_user_calls();
L25: } elsif ($in =~ /^RBN|SKI/) {
L26: push @list, map {$_->is_rbn ? $_->call : undef} DXChannel::get_all();
L28: push @list, $in;
L37: push @list, $self->call unless @list;
L38: foreach my $call (sort @list) {
L55: my $num = shift;
```

### Validation and access evidence

Source: `cmd/show/data_stats.pl` · SHA-256 `df35de23bf469668da870da0ca8f6b49a6913fd2a590cbf4a325dd422fcf5735`

```perl
L21: if ($in =~ /^NOD/){
```

### Output and error evidence

Source: `cmd/show/data_stats.pl` · SHA-256 `df35de23bf469668da870da0ca8f6b49a6913fd2a590cbf4a325dd422fcf5735`

```perl
L34: push @out, sprintf "Transfered in:%-12.12s IN OUT", $dt;
L35: push @out, "Callsign Lines Data Lines Data";
L36: push @out, "-----------------------------------------------------------------------------";
L43: push @out, sprintf("%-9.9s %16s %16s %16s %16s", $call, comma($conn->{linesin}), comma($conn->{datain}), comma($conn->{linesout}), comma($conn->{dataout}));
L47: push @out, "-----------------------------------------------------------------------------" if @out > 3;
L48: push @out, sprintf("%-9.9s %16s %16s %16s %16s", "TOTALS", comma($Msg::total_lines_in), comma($Msg::total_in), comma($Msg::total_lines_out), comma($Msg::total_out));
L50: return (1, @out);
```

!!! info "No built-in help entry"
    This command exists in `cmd/` but has no matching header in `Commands_en.hlp`. Its page is therefore derived from implementation evidence only.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/data_stats.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/DATA_STATS
```

Compare the installed handler with this page when local overrides or a different revision may be present.