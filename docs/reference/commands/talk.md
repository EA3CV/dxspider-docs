# `TALK`

<div class="command-hero" markdown>

**Send a private talk message or enter interactive talk mode.**

<div class="command-meta" markdown>
<div><span class="meta-label">Guide</span><br><span class="badge badge-user">User</span></div>
<div><span class="meta-label">Category</span><br>Communications</div>
<div><span class="meta-label">Applies to</span><br>DXSpider 1.57 · Mojo ≥ 686</div>
</div>

</div>

## Syntax and variants

=== "User form"

    ```text
    TALK <call> [<text>]
    ```

    **Send a text message to another station**


=== "User form"

    ```text
    TALK <call> > <node> [<text>]
    ```

    **Send a text message to another station via a node**

    Send a short message to any other station that is visible on the cluster
    system. You can send it to anyone you can see with a SHOW/CONFIGURATION
    command, they don't have to be connected locally.

    The second form of TALK is used when other cluster nodes are connected
    with restricted information. This usually means that they don't send
    the user information usually associated with logging on and off the cluster.

    If you know that G3JNB is likely to be present on GB7TLH, but you can only
    see GB7TLH in the SH/C list but with no users, then you would use the
    second form of the talk message.

    If you want to have a ragchew with someone you can leave the text message
    out and the system will go into 'Talk' mode. What this means is that a
    short message is sent to the recipient telling them that you are in a
    'Talking' frame of mind and then you just type - everything you send will
    go to the station that you asked for.

    All the usual announcements, spots and so on will still come out on your
    terminal.

    If you want to do something (such as send a spot) you preceed the normal
    command with a '/' character, eg:-

    ```text
     /DX 14001 G1TLH What's a B class licensee doing on 20m CW?
     /HELP talk
    ```

    To leave talk mode type:

    ```text
     /EX
    ```

    If you are in 'Talk' mode, there is an extention to the '/' command which
    allows you to send the output to all the people you are talking to. You do
    with the '//' command. For example:-

    ```text
    //sh/hftable
    ```

    will send the hftable as you have it to all the people you are currently
    talking to.

## Practical examples

### Send a message

```text
TALK G1ABC Hello John
```

### Route explicitly through a node

```text
TALK G1ABC > GB7DJK Hello John
```

### Run a DXSpider command while in talk mode

```text
/SHOW/DX
```

## Implementation

[View the current command source on GitHub](https://github.com/EA3CV/dxspider/blob/4904e1866076e1a4d0292caef36e994472a393b6/cmd/talk.pl){ .md-button }

## Related commands

- [`SET/TALK`](set--talk.md)
- [`UNSET/TALK`](unset--talk.md)

## Verify on a running node

```text
HELP TALK
```

The built-in help is useful when checking the exact command set installed on a particular node.