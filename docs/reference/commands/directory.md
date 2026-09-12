# `DIRECTORY`

<div class="command-hero" markdown>

**Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range.**

<div class="command-meta" markdown>
<div><span class="meta-label">Code classification</span><br><span class="badge badge-sysop">Direct administration guard</span></div>
<div><span class="meta-label">Category</span><br>Messages</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

!!! warning "Implementation is authoritative"
    The command source determines real behaviour. Built-in help is shown later only for comparison and may lag the implementation.

## Effective interface from code

```text
DIRECTORY [token ...]
```

The handler tokenizes the argument line on whitespace; branches below determine ordering and cardinality.

### Access and execution restrictions

- The handler contains a direct privilege guard.

### Observable implementation effects

- Uses the internal message subsystem.

### Recognized tokens, keys or enumerated values in this handler

`<`, `>`, `ALL`

These values are extracted from comparisons, argument hashes and `qw(...)` lists in the handler. Their exact role and combinations are established by the parser evidence below.

### Important calls

`DXMsg::get_all()`, `self->msg()`

### Argument parsing evidence

Source: `cmd/directory.pl` · SHA-256 `d98ebb24bac540d250f1ef8333c26a53c247876864454867649e97eb4b609020`

```perl
L9: my ($self, $line) = @_;
L10: my @f = split /\s+/, $line;
L27: $f = uc shift @f;
L32: } elsif ($f =~ /^O/o) { # dir/own
L35: } elsif ($f =~ /^N/o) { # dir/new
L38: } elsif ($f =~ /^S/o) { # dir/subject
L39: $f = shift @f;
L41: $f =~ s{(.)}{"\Q$1"}ge;
L42: @ref = grep { $_->subject =~ m{$f}i } @all;
L45: } elsif ($f eq '>' || $f =~ /^T/o){
L46: $f = uc shift @f;
L49: @ref = grep { $_->to =~ m{$f} } @all;
L52: } elsif ($f eq '<' || $f =~ /^F/o){
L53: $f = uc shift @f;
L56: @ref = grep { $_->from =~ m{$f} } @all;
L59: } elsif ($f =~ /^(\d+)-(\d+)$/) { # a range of items
L62: } elsif ($f =~ /^\d+$/ && $f > 0) { # a number of items
```

### Validation and access evidence

Source: `cmd/directory.pl` · SHA-256 `d98ebb24bac540d250f1ef8333c26a53c247876864454867649e97eb4b609020`

```perl
L21: return (1, $self->msg('dir1')) unless @all;
```

### Output and error evidence

Source: `cmd/directory.pl` · SHA-256 `d98ebb24bac540d250f1ef8333c26a53c247876864454867649e97eb4b609020`

```perl
L21: return (1, $self->msg('dir1')) unless @all;
L79: push @out, $ref->dir;
L83: push @out, $self->msg('dir1');
L85: return (1, @out);
```

### Message keys returned

`dir1`

## Built-in help (secondary)

The following forms come from `Commands_en.hlp`; compare them with the implementation evidence above.

=== "Help variant"

    ```text
    DIRECTORY
    ```

    **List messages**


=== "Help variant"

    ```text
    DIRECTORY ALL
    ```

    **List all messages**


=== "Help variant"

    ```text
    DIRECTORY OWN
    ```

    **List your own messages**


=== "Help variant"

    ```text
    DIRECTORY NEW
    ```

    **List all new messages**


=== "Help variant"

    ```text
    DIRECTORY TO <call>
    ```

    **List all messages to <call>**


=== "Help variant"

    ```text
    DIRECTORY FROM <call>
    ```

    **List all messages from <call>**


=== "Help variant"

    ```text
    DIRECTORY SUBJECT <string>
    ```

    **List all messages with <string> in subject**


=== "Help variant"

    ```text
    DIRECTORY <nn>
    ```

    **List last <nn> messages**


=== "Help variant"

    ```text
    DIRECTORY <from>-<to>
    ```

    **List messages <from> message <to> message**

    List the messages in the messages directory.

    If there is a 'p' one space after the message number then it is a
    personal message. If there is a '-' between the message number and the
    'p' then this indicates that the message has been read.

    You can use shell escape characters such as '*' and '?' in the <call>
    fields.

    You can combine some of the various directory commands together eg:-

    ```text
     DIR TO G1TLH 5
    ```
    or
    ```text
     DIR SUBJECT IOTA 200-250
    ```

    You can abbreviate all the commands to one letter and use ak1a syntax:-

    ```text
     DIR/T G1* 10
     DIR/S QSL 10-100 5
    ```

=== "Help variant"

    ```text
    DIRECTORY-
    ```

    ****

    Sysops can see all users' messages.

## When would I use this?

DIRECTORY is the entry point to the message system. Its selectors can be combined instead of scrolling through an undifferentiated list.

## Practical examples

### List messages

```text
DIRECTORY
```

### Your own messages

```text
DIRECTORY OWN
```

### New messages

```text
DIRECTORY NEW
```

### Messages to a callsign

```text
DIRECTORY TO G1TLH 5
```

### Subject search within a range

```text
DIRECTORY SUBJECT IOTA 200-250
```

### Wildcard callsign search

```text
DIR/T G1* 10
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/directory.pl){ .md-button }

## Related commands

- [`READ`](read.md)
- [`SEND`](send.md)
- [`REPLY`](reply.md)
- [`KILL`](kill.md)

## Verify on a running node

```text
HELP DIRECTORY
```

Compare the installed handler with this page when local overrides or a different revision may be present.