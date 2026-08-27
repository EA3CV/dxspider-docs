# SYSOP command reference

This list is generated from the current DXSpider help metadata. Commands marked **DUAL** contain both user and privileged variants.

| Command | Guide | Purpose |
|---|---|---|
| [`ACCEPT/ANNOUNCE`](../../reference/commands/accept--announce.md) | User + SYSOP | Set an 'accept' filter line for announce |
| [`ACCEPT/ROUTE`](../../reference/commands/accept--route.md) | SYSOP | Set an 'accept' filter line for routing |
| [`ACCEPT/SPOTS`](../../reference/commands/accept--spots.md) | User + SYSOP | Allow only DX spots that match one or more filter rules. |
| [`ACCEPT/WCY`](../../reference/commands/accept--wcy.md) | User + SYSOP | set an 'accept' WCY filter |
| [`ACCEPT/WWV`](../../reference/commands/accept--wwv.md) | User + SYSOP | set an 'accept' WWV filter |
| [`ANNOUNCE`](../../reference/commands/announce.md) | User + SYSOP | Send local, cluster-wide or SYSOP-only announcements. |
| [`CATCHUP`](../../reference/commands/catchup.md) | SYSOP | Mark a message as sent |
| [`CLEAR/ANNOUNCE`](../../reference/commands/clear--announce.md) | User + SYSOP | Clear a announce filter line |
| [`CLEAR/DUPEFILE`](../../reference/commands/clear--dupefile.md) | SYSOP | Clear out the dupefile completely |
| [`CLEAR/ROUTE`](../../reference/commands/clear--route.md) | User + SYSOP | Clear a route filter line |
| [`CLEAR/SPOTS`](../../reference/commands/clear--spots.md) | User + SYSOP | Remove one line or the complete DX spot filter. |
| [`CLEAR/WCY`](../../reference/commands/clear--wcy.md) | User + SYSOP | Clear a WCY filter line |
| [`CLEAR/WWV`](../../reference/commands/clear--wwv.md) | User + SYSOP | Clear a WWV filter line |
| [`CONNECT`](../../reference/commands/connect.md) | SYSOP | Start a connection to another DX Cluster |
| [`CREATE/USER`](../../reference/commands/create--user.md) | SYSOP | Create this user from the User Database |
| [`DBCREATE`](../../reference/commands/dbcreate.md) | SYSOP | Create a database entry |
| [`DBEXPORT`](../../reference/commands/dbexport.md) | SYSOP | Export an AK1A data to a file |
| [`DBIMPORT`](../../reference/commands/dbimport.md) | SYSOP | Import AK1A data into a database |
| [`DBREMOVE`](../../reference/commands/dbremove.md) | SYSOP | Delete a database |
| [`DEBUG`](../../reference/commands/debug.md) | SYSOP | Set the cluster program into debug mode |
| [`DELETE/USDB`](../../reference/commands/delete--usdb.md) | SYSOP | Delete this user from the US State Database |
| [`DELETE/USER`](../../reference/commands/delete--user.md) | SYSOP | Delete this user from the User Database |
| [`DEMONSTRATE`](../../reference/commands/demonstrate.md) | SYSOP | Demonstrate a command to another user |
| [`DIRECTORY`](../../reference/commands/directory.md) | User + SYSOP | Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range. |
| [`DISCONNECT`](../../reference/commands/disconnect.md) | SYSOP | Disconnect user(s) or node(s) |
| [`DOWNLOAD`](../../reference/commands/download.md) | SYSOP | Download a file into local_data |
| [`DX`](../../reference/commands/dx.md) | User + SYSOP | Send a DX spot into the cluster network. |
| [`DXQSL_EXPORT`](../../reference/commands/dxqsl-export.md) | SYSOP | Export SH/DXSQL information to a file |
| [`DXQSL_IMPORT`](../../reference/commands/dxqsl-import.md) | SYSOP | Import SH/DXSQL information from a file |
| [`EXPORT`](../../reference/commands/export.md) | SYSOP | Export a message to a file |
| [`EXPORT_USERS`](../../reference/commands/export-users.md) | SYSOP | Export the users database to ascii |
| [`FORWARD/LATLONG`](../../reference/commands/forward--latlong.md) | SYSOP | Send latitude and longitude information to another cluster |
| [`FORWARD/OPERNAM`](../../reference/commands/forward--opernam.md) | SYSOP | Send out information on this <call> to all clusters |
| [`GET/KEPS`](../../reference/commands/get--keps.md) | SYSOP | Obtain the latest AMSAT Keplarian Elements from the web |
| [`INIT`](../../reference/commands/init.md) | SYSOP | Re-initialise a link to an AK1A compatible node |
| [`KILL`](../../reference/commands/kill.md) | User + SYSOP | Delete a message from the local system |
| [`LOAD/ALIASES`](../../reference/commands/load--aliases.md) | SYSOP | Reload the command alias table |
| [`LOAD/BADIP`](../../reference/commands/load--badip.md) | SYSOP | Reload the bad IP address table |
| [`LOAD/BADMSG`](../../reference/commands/load--badmsg.md) | SYSOP | Reload the bad msg table |
| [`LOAD/BADWORDS`](../../reference/commands/load--badwords.md) | SYSOP | Reload the bad words table |
| [`LOAD/BANDS`](../../reference/commands/load--bands.md) | SYSOP | Reload the band limits table |
| [`LOAD/CMD_CACHE`](../../reference/commands/load--cmd-cache.md) | SYSOP | Reload the automatic command cache |
| [`LOAD/FORWARD`](../../reference/commands/load--forward.md) | SYSOP | Reload the msg forwarding routing table |
| [`LOAD/KEPS`](../../reference/commands/load--keps.md) | SYSOP | Load new keps data |
| [`LOAD/MESSAGES`](../../reference/commands/load--messages.md) | SYSOP | Reload the system messages file |
| [`LOAD/PREFIXES`](../../reference/commands/load--prefixes.md) | SYSOP | Reload the prefix table |
| [`MERGE`](../../reference/commands/merge.md) | SYSOP | Ask for the latest spots and WWV |
| [`MSG`](../../reference/commands/msg.md) | SYSOP | Alter various message parameters |
| [`PC`](../../reference/commands/pc.md) | SYSOP | Send text (eg PC Protocol) to <call> |
| [`PING`](../../reference/commands/ping.md) | User + SYSOP | User level link check command |
| [`RCMD`](../../reference/commands/rcmd.md) | SYSOP | Send a command to another DX Cluster |
| [`READ`](../../reference/commands/read.md) | User + SYSOP | Read the next unread personal message addressed to you |
| [`REJECT/ANNOUNCE`](../../reference/commands/reject--announce.md) | User + SYSOP | Set a 'reject' filter line for announce |
| [`REJECT/ROUTE`](../../reference/commands/reject--route.md) | SYSOP | Set an 'reject' filter line for routing |
| [`REJECT/SPOTS`](../../reference/commands/reject--spots.md) | User + SYSOP | Reject DX spots that match one or more filter rules. |
| [`REJECT/WCY`](../../reference/commands/reject--wcy.md) | User + SYSOP | set a 'reject' WCY filter |
| [`REJECT/WWV`](../../reference/commands/reject--wwv.md) | User + SYSOP | set a 'reject' WWV filter |
| [`SAVE`](../../reference/commands/save.md) | SYSOP | Save command output to a file |
| [`SEND_CONFIG`](../../reference/commands/send-config.md) | SYSOP | Broadcast PC92 C records |
| [`SET/AGWENGINE`](../../reference/commands/set--agwengine.md) | SYSOP | Enable the AGW Engine |
| [`SET/AGWMONITOR`](../../reference/commands/set--agwmonitor.md) | SYSOP | Enable Monitoring on the AGW Engine |
| [`SET/ARCLUSTER`](../../reference/commands/set--arcluster.md) | SYSOP | Make the callsign an AR-Cluster node |
| [`SET/BADDX`](../../reference/commands/set--baddx.md) | SYSOP | Stop callsigns in a dx spot being propagated |
| [`SET/BADIP`](../../reference/commands/set--badip.md) | SYSOP | Stop logins and spots with this IP address |
| [`SET/BADNODE`](../../reference/commands/set--badnode.md) | SYSOP | Stop spots from this node being propagated |
| [`SET/BADSPOTTER`](../../reference/commands/set--badspotter.md) | SYSOP | Stop spots from this callsign being propagated |
| [`SET/BADWORD`](../../reference/commands/set--badword.md) | SYSOP | Stop things like this word being propagated |
| [`SET/BBS`](../../reference/commands/set--bbs.md) | SYSOP | Make the callsign a BBS |
| [`SET/CCLUSTER`](../../reference/commands/set--ccluster.md) | SYSOP | Make the callsign an CC Cluster node |
| [`SET/CLX`](../../reference/commands/set--clx.md) | SYSOP | Make the callsign an CLX node |
| [`SET/DEBUG`](../../reference/commands/set--debug.md) | SYSOP | Add a debug level to the debug set |
| [`SET/DXNET`](../../reference/commands/set--dxnet.md) | SYSOP | Make the callsign an DXNet node |
| [`SET/HOPS`](../../reference/commands/set--hops.md) | SYSOP | Set hop count |
| [`SET/ISOLATE`](../../reference/commands/set--isolate.md) | SYSOP | Isolate a node from the rest of the network |
| [`SET/LOCAL_NODE`](../../reference/commands/set--local-node.md) | SYSOP | Add node to the local_node group |
| [`SET/LOCKOUT`](../../reference/commands/set--lockout.md) | SYSOP | Stop a callsign connecting to the cluster |
| [`SET/MAXCONNECT`](../../reference/commands/set--maxconnect.md) | SYSOP | Set max incoming connections for user/node |
| [`SET/NODE`](../../reference/commands/set--node.md) | SYSOP | Make the callsign an AK1A cluster |
| [`SET/OBSCOUNT`](../../reference/commands/set--obscount.md) | SYSOP | Set the 'pump-up' obscelence PING counter |
| [`SET/PASSWORD`](../../reference/commands/set--password.md) | User + SYSOP | Change your own password interactively, or—at SYSOP privilege—set another user's password. |
| [`SET/PINGINTERVAL`](../../reference/commands/set--pinginterval.md) | SYSOP | Set ping time to neighbouring nodes |
| [`SET/PRIVILEGE`](../../reference/commands/set--privilege.md) | SYSOP | Set privilege level on a call |
| [`SET/RBN`](../../reference/commands/set--rbn.md) | SYSOP | Mark this call as an RBN node |
| [`SET/REGISTER`](../../reference/commands/set--register.md) | SYSOP | Mark a user as registered |
| [`SET/SKIMMER`](../../reference/commands/set--skimmer.md) | User + SYSOP | [category ..]^Allow (some) RBN/Skimmer spotsT |
| [`SET/SPIDER`](../../reference/commands/set--spider.md) | SYSOP | Make the callsign an DXSpider node |
| [`SET/STARTUP`](../../reference/commands/set--startup.md) | User + SYSOP | Create a user startup script |
| [`SET/SYS_LOCATION`](../../reference/commands/set--sys-location.md) | SYSOP | Set your cluster latitude and longitude |
| [`SET/SYS_QRA`](../../reference/commands/set--sys-qra.md) | SYSOP | Set your cluster QRA Grid locator |
| [`SET/USDB`](../../reference/commands/set--usdb.md) | SYSOP | add/update a US DB callsign |
| [`SET/USER`](../../reference/commands/set--user.md) | SYSOP | Make the callsign a normal user |
| [`SET/WANTRBN`](../../reference/commands/set--wantrbn.md) | User + SYSOP | Choose which curated RBN/Skimmer categories are delivered to the user. |
| [`SHOW/BADDX`](../../reference/commands/show--baddx.md) | SYSOP | Show all the bad dx calls in the system |
| [`SHOW/BADNODE`](../../reference/commands/show--badnode.md) | SYSOP | Show all the bad nodes in the system |
| [`SHOW/BADSPOTTER`](../../reference/commands/show--badspotter.md) | SYSOP | Show all the bad spotters in the system |
| [`SHOW/BADWORD`](../../reference/commands/show--badword.md) | SYSOP | Show all the bad words in the system |
| [`SHOW/CMD_CACHE`](../../reference/commands/show--cmd-cache.md) | SYSOP | Show the real source path of commands |
| [`SHOW/CONNECT`](../../reference/commands/show--connect.md) | SYSOP | Show all the active connections |
| [`SHOW/DEBUG`](../../reference/commands/show--debug.md) | SYSOP | Show what levels of debug information you are logging |
| [`SHOW/HOPS`](../../reference/commands/show--hops.md) | SYSOP | Show the hop counts for a node |
| [`SHOW/ISOLATE`](../../reference/commands/show--isolate.md) | SYSOP | Show list of ISOLATED nodes |
| [`SHOW/LOCKOUT`](../../reference/commands/show--lockout.md) | SYSOP | Show the list of locked out or excluded callsigns |
| [`SHOW/LOG`](../../reference/commands/show--log.md) | SYSOP | Show excerpts from the system log |
| [`SHOW/NODE`](../../reference/commands/show--node.md) | SYSOP | Show the type and version number of nodes |
| [`SHOW/PROGRAM`](../../reference/commands/show--program.md) | SYSOP | Show the locations of all the included program modules |
| [`SHOW/RBN`](../../reference/commands/show--rbn.md) | SYSOP | Show which connected users want RBN spots |
| [`SHOW/RCMD`](../../reference/commands/show--rcmd.md) | SYSOP | Show log of rcmds |
| [`SHOW/REGISTERED`](../../reference/commands/show--registered.md) | SYSOP | Show the registered users |
| [`SHOW/SPOTSTATS`](../../reference/commands/show--spotstats.md) | SYSOP | Show the current Spot statistics |
| [`SHOW/STARTUP`](../../reference/commands/show--startup.md) | User + SYSOP | View a user startup script |
| [`SHOW/STATION`](../../reference/commands/show--station.md) | User + SYSOP | Show list of users in the system |
| [`SHUTDOWN`](../../reference/commands/shutdown.md) | SYSOP | Shutdown the cluster |
| [`SPOOF`](../../reference/commands/spoof.md) | SYSOP | Do a command as though you are another user |
| [`STAT/CHANNEL`](../../reference/commands/stat--channel.md) | SYSOP | Show the status of a channel on the cluster |
| [`STAT/DB`](../../reference/commands/stat--db.md) | SYSOP | Show the status of a database |
| [`STAT/MSG`](../../reference/commands/stat--msg.md) | SYSOP | Show the status of the message system |
| [`STAT/ROUTE_NODE`](../../reference/commands/stat--route-node.md) | SYSOP | Show the data in a Route::Node object |
| [`STAT/ROUTE_USER`](../../reference/commands/stat--route-user.md) | SYSOP | Show the data in a Route::User object |
| [`STAT/USER`](../../reference/commands/stat--user.md) | SYSOP | Show the full status of a user |
| [`UNCATCHUP`](../../reference/commands/uncatchup.md) | SYSOP | Unmark a message as sent |
| [`UNSET/AGWENGINE`](../../reference/commands/unset--agwengine.md) | SYSOP | Disable the AGW Engine |
| [`UNSET/AGWMONITOR`](../../reference/commands/unset--agwmonitor.md) | SYSOP | Disable Monitoring on the AGW Engine |
| [`UNSET/AK1A`](../../reference/commands/unset--ak1a.md) | SYSOP | Make the callsign a normal user |
| [`UNSET/ARCLUSTER`](../../reference/commands/unset--arcluster.md) | SYSOP | Make the callsign a normal user |
| [`UNSET/BADDX`](../../reference/commands/unset--baddx.md) | SYSOP | Propagate a dx spot with this callsign again |
| [`UNSET/BADNODE`](../../reference/commands/unset--badnode.md) | SYSOP | Allow spots from this node again |
| [`UNSET/BADSPOTTER`](../../reference/commands/unset--badspotter.md) | SYSOP | Allow spots from this callsign again |
| [`UNSET/BADWORD`](../../reference/commands/unset--badword.md) | SYSOP | Propagate things like this word again |
| [`UNSET/DEBUG`](../../reference/commands/unset--debug.md) | SYSOP | Remove a debug level from the debug set |
| [`UNSET/HOPS`](../../reference/commands/unset--hops.md) | SYSOP | Unset hop count |
| [`UNSET/ISOLATE`](../../reference/commands/unset--isolate.md) | SYSOP | Stop Isolation of a node from the rest of the network |
| [`UNSET/LOCAL_NODE`](../../reference/commands/unset--local-node.md) | SYSOP | Remove node from the local_node group |
| [`UNSET/LOCKOUT`](../../reference/commands/unset--lockout.md) | SYSOP | Allow a callsign to connect to the cluster |
| [`UNSET/NODE`](../../reference/commands/unset--node.md) | SYSOP | Make the callsign a normal user |
| [`UNSET/PASSWORD`](../../reference/commands/unset--password.md) | SYSOP | Delete (remove) a user's password |
| [`UNSET/REGISTER`](../../reference/commands/unset--register.md) | SYSOP | Mark a user as not registered |
| [`UNSET/SPIDER`](../../reference/commands/unset--spider.md) | SYSOP | Make the callsign a normal user |
| [`UNSET/STARTUP`](../../reference/commands/unset--startup.md) | User + SYSOP | Remove a user startup script |
| [`WX`](../../reference/commands/wx.md) | User + SYSOP | Send a weather message to local users |