# `ECHO`

<div class="command-hero" markdown>

**Echo the line to the output**

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
ECHO [arguments; see parser evidence]
```

The handler uses a custom parser or treats the argument line as free text. See parser evidence.

### Access and execution restrictions

No direct privilege, remote-command, script, or local-context guard was found in this handler. This does not rule out checks in delegated functions or the surrounding session path.

### Argument parsing evidence

Source: `cmd/echo.pl` · SHA-256 `0993cffc7bb52b0db24f6e33e21178760b031318f497e3dcb483b5831a66381b`

```perl
L10: my ($self, $line) = @_;
L12: $line =~ s/\\t/\t/g; # tabs
L13: $line =~ s/\\a/\a/g; # beeps
L14: my @out = split /\\[n]/, $line;
```

### Output and error evidence

Source: `cmd/echo.pl` · SHA-256 `0993cffc7bb52b0db24f6e33e21178760b031318f497e3dcb483b5831a66381b`

```perl
L15: return (1, @out);
```

## Built-in help (secondary)

This section comes from `Commands_en.hlp` and may lag the implementation.

```text
ECHO <line>
```

**Echo the line to the output**

## Details

This command is useful in scripts and so forth for printing the
line that you give to the command to the output. You can use this
in user_default scripts and the SAVE command for titling and so forth

The script will interpret certain standard "escape" sequences as follows:-

```text
\t - becomes a TAB character (0x09 in ascii)
\a - becomes a BEEP character (0x07 in ascii)
\n - prints a new line
```

So the following example:-

```text
echo GB7DJK is a dxcluster
```

produces:-

```text
GB7DJK is a dxcluster
```

on the output. You don't need a \n on the end of the line you want to send.

A more complex example:-

```text
echo GB7DJK\n\tg1tlh\tDirk\n\tg3xvf\tRichard
```

produces:-

```text
GB7DJK
        g1tlh   Dirk
        g3xvf   Richard
```

on the output.

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/b53589e2425e5ba27b6623611571470f278140c1/cmd/echo.pl){ .md-button }

## Verify on a running node

```text
HELP ECHO
```

Compare the installed handler with this page when local overrides or a different revision may be present.