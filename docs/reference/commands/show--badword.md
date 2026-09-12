# `SHOW/BADWORD`

<div class="command-hero" markdown>

**Show all the bad words in the system**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-sysop">Administration</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Usage

```text
SHOW/BADWORD [token ...]
```

### Who can use it

- This command is restricted to an appropriately privileged operator.
- It cannot be run through remote-command execution.

## Command forms and examples

=== "Available form"

    ```text
    SHOW/BADWORD
    ```

    **Show all the bad words in the system**


=== "Available form"

    ```text
    SHOW/BADWORD full
    ```

    **Show all badwords with their Regex**


=== "Available form"

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

## Verify on a running node

```text
HELP SHOW/BADWORD
```

Use the node help to check for local overrides or differences in another installed revision.