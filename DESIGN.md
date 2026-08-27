# Documentation design goals

The documentation must be more useful than typing `HELP` at the node.

A command page is considered complete only when it provides, where applicable:

- purpose and operational context;
- all current syntax variants;
- clear User/SYSOP placement without publishing internal authorization levels;
- argument names and accepted values;
- current built-in help detail;
- practical copy/paste examples;
- side effects, persistence and warnings when verified;
- related commands;
- a source link pinned to the exact DXSpider commit used to build the site.

Task-oriented guides sit above the command reference so users do not need to know a command name before they can solve a problem.

No placeholder descriptions such as “Enable X”, “Disable Y” or “Show Z” are generated merely from a filename. If DXSpider's current help/source does not explain a command sufficiently, it is treated as a documentation gap rather than publishing meaningless prose.
