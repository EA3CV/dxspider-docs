# `SHOW/BADWORD`

<div class="command-hero" markdown>

**Show all the bad words in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">SYSOP</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "SYSOP form"

    ```text
    SHOW/BADWORD
    ```

    **Show all the bad words in the system**


=== "SYSOP form"

    ```text
    SHOW/BADWORD full
    ```

    **Show all badwords with their Regex**


=== "SYSOP form"

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

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/badword.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/BADWORD
```

The built-in help is useful when checking the exact command set installed on a particular node.