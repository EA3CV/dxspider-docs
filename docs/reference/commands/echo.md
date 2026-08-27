# `ECHO`

<div class="command-hero" markdown>

**Echo the line to the output**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/echo.pl){ .md-button }

## Verify on a running node

```text
HELP ECHO
```

The built-in help is useful when checking the exact command set installed on a particular node.