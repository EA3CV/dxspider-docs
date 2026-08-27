# `SHOW/QRA`

<div class="command-hero" markdown>

**Show distance between QRA Grid locators**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Command reference</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    SHOW/QRA <locator> [<locator>]
    ```

    **Show distance between QRA Grid locators**


=== "User form"

    ```text
    SHOW/QRA <lat> <long>
    ```

    **Convert lat/long to a QRA Grid locator**

    This is a multipurpose command that allows you either to calculate the
    distance and bearing between two locators or (if only one locator is
    given on the command line) the distance and beraing from your station
    to the locator. For example:-

     SH/QRA IO92QL
     SH/QRA JN06 IN73

    The first example will show the distance and bearing to the locator from
    yourself, the second example will calculate the distance and bearing from
    the first locator to the second. You can use 4 or 6 character locators.

    It is also possible to convert a latitude and longitude to a locator by
    using this command with a latitude and longitude as an argument, for
    example:-

     SH/QRA 52 41 N 0 58 E

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/show/qra.pl){ .md-button }

## Verify on a running node

```text
HELP SHOW/QRA
```

The built-in help is useful when checking the exact command set installed on a particular node.