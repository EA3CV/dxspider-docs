# `SHOW/BADWORD`

<div class="command-hero" markdown>

**Show all the bad words in the system**

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
SHOW/BADWORD [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.
- The handler restricts remote-command execution.

### Important calls

`BadWords::check()`, `BadWords::list_regex()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/show/badword.pl` · SHA-256 `7b89b9c9da148ca17ea1d3625ddff658af55e8d2e9d179455e1440fecd600690`

```perl
L9: my ($self, $line) = @_;
L17: my @words = BadWords::check($line);
L23: if ($line =~ /^\s*full/i || @words) {
L26: if ($line =~ /^\s*full/) {
L29: ($cand) = split /\s+/, $w;
```

### Validation and access evidence

Source: `cmd/show/badword.pl` · SHA-256 `7b89b9c9da148ca17ea1d3625ddff658af55e8d2e9d179455e1440fecd600690`

```perl
L10: return (1, $self->msg('e5')) if $self->remotecmd;
L12: return (1, $self->msg('e5')) if $self->priv < 6;
L23: if ($line =~ /^\s*full/i || @words) {
L26: if ($line =~ /^\s*full/) {
```

### Output and error evidence

Source: `cmd/show/badword.pl` · SHA-256 `7b89b9c9da148ca17ea1d3625ddff658af55e8d2e9d179455e1440fecd600690`

```perl
L10: return (1, $self->msg('e5')) if $self->remotecmd;
L12: return (1, $self->msg('e5')) if $self->priv < 6;
L21: push @out, "Words: " . join ',', @words;
L27: push @out, $w;
L31: push @out, $w if grep {$cand eq $_} @words;
L39: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L45: push @out, sprintf "%-12s %-12s %-12s %-12s %-12s", @l;
L48: push @out, "$count BadWords";
L50: return (1, @out);
```

### Message keys returned

`e5`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    SHOW/BADWORD
    ```

    **Show all the bad words in the system**


=== "Help variant"

    ```text
    SHOW/BADWORD full
    ```

    **Show all badwords with their Regex**


=== "Help variant"

    ```text
    SHOW/BADWORD <word> ...
    ```

    **Show all badwords with their Regex**

    Display all the bad words in the system, see SET/BADWORD
    for more information.

    The first form shows all the base words that are stored in a simple list.

    The second form list all words with their associated perl regex.

    The third form shows just the regexes for the words asked for. If no
    answer for a word is given then it is not defined.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/show/badword.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BADWORD
```

Compare the installed handler with this page when local overrides or a different revision may be present.