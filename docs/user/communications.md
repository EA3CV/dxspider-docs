# Announcements, chat and talk

## Announcements

```text
ANNOUNCE <text>
ANNOUNCE FULL <text>
```

The first form is local; `FULL` distributes the announcement through the cluster network.

## Chat groups

```text
JOIN <group>
CHAT <group> <text>
LEAVE <group>
SHOW/CHAT
```

## Talk

```text
TALK <callsign> [text]
TALK <callsign> > <node> [text]
```

If text is omitted, DXSpider can enter talk mode. In talk mode, prefix a normal command with `/` to execute it.

```text
/DX 14001 G1ABC test
/HELP TALK
```

Leave talk mode with `/EX`.
