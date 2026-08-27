# SYSOP command reference

authorization d commands and commands with additional SYSOP forms are listed here.

| Command | authorization | Scope |
|---|---:|---|
| [`ACCEPT/ANNOUNCE`](../../reference/commands/accept--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/RBN`](../../reference/commands/accept--rbn.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/ROUTE`](../../reference/commands/accept--route.md) | 8 | Create/update an accept filter for `route`. |
| [`ACCEPT/SPOTS`](../../reference/commands/accept--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/WCY`](../../reference/commands/accept--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/WWV`](../../reference/commands/accept--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`AGWRESTART`](../../reference/commands/agwrestart.md) | 5 | Restart the AGW connection subsystem. |
| [`ANNOUNCE`](../../reference/commands/announce.md) | 0 / 5 | Send local or cluster-wide announcements; SYSOP form targets sysops. |
| [`CATCHUP`](../../reference/commands/catchup.md) | 5 | Mark messages as already sent to a forwarding node. |
| [`CLEAR/ANNOUNCE`](../../reference/commands/clear--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/CMD_CACHE`](../../reference/commands/clear--cmd-cache.md) | 9 | Alias to LOAD/CMD_CACHE; clears/reloads the command cache. |
| [`CLEAR/DUPEFILE`](../../reference/commands/clear--dupefile.md) | 6 | Clears the duplicate tracking file; use only for diagnosed duplicate problems. |
| [`CLEAR/RBN`](../../reference/commands/clear--rbn.md) | 0 / 8 | User form clears own RBN filter; SYSOP form can target another callsign/default. |
| [`CLEAR/ROUTE`](../../reference/commands/clear--route.md) | 0 / 8 | User and SYSOP route-filter forms exist. |
| [`CLEAR/SPOTS`](../../reference/commands/clear--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/WCY`](../../reference/commands/clear--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/WWV`](../../reference/commands/clear--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CONNECT`](../../reference/commands/connect.md) | 5 | Start an outbound connection to another cluster node. |
| [`CREATE/USER`](../../reference/commands/create--user.md) | 5 | Create `user`. |
| [`DBCREATE`](../../reference/commands/dbcreate.md) | 9 | Define a local, chained, remote or command-backed database. |
| [`DBEXPORT`](../../reference/commands/dbexport.md) | 9 | Export database data. |
| [`DBIMPORT`](../../reference/commands/dbimport.md) | 9 | Import database data. |
| [`DBREMOVE`](../../reference/commands/dbremove.md) | 9 | Remove a database definition/data. |
| [`DEBUG`](../../reference/commands/debug.md) | 9 | Enter Perl debugger mode when the node is running under the debugger. |
| [`DELETE/USDB`](../../reference/commands/delete--usdb.md) | 9 | Delete `usdb`. |
| [`DELETE/USER`](../../reference/commands/delete--user.md) | 9 | Delete `user`. |
| [`DEMONSTRATE`](../../reference/commands/demonstrate.md) | 9 | Run a command as another user for demonstration/support. |
| [`DIRECTORY`](../../reference/commands/directory.md) | 0 / 5 | List messages; SYSOP can see otherwise hidden/private entries. |
| [`DISCONNECT`](../../reference/commands/disconnect.md) | 8 | Disconnect local users, nodes or groups of connections. |
| [`DMESG`](../../reference/commands/dmesg.md) | 9 | Alias to SHOW/DEBUG_RING. |
| [`DOWNLOAD`](../../reference/commands/download.md) | 9 | Download a URL into local_data, including from cron. |
| [`DX`](../../reference/commands/dx.md) | 0 / 2 | Send a DX spot; authorization d form accepts additional origin metadata. |
| [`DXQSL_EXPORT`](../../reference/commands/dxqsl-export.md) | 9 | Export accumulated DX QSL-manager information. |
| [`DXQSL_IMPORT`](../../reference/commands/dxqsl-import.md) | 9 | Import accumulated DX QSL-manager information. |
| [`EXPORT`](../../reference/commands/export.md) | 9 | Export a message to a file from a authorization d local console. |
| [`EXPORT_USERS`](../../reference/commands/export-users.md) | 9 | Export the user database to ASCII. |
| [`FORWARD/LATLONG`](../../reference/commands/forward--latlong.md) | 8 | Administrative forwarding operation for latitude/longitude data. |
| [`FORWARD/OPERNAME`](../../reference/commands/forward--opername.md) | 1 | Administrative forwarding operation; current help spells the command OPERNAM. |
| [`GET/KEPS`](../../reference/commands/get--keps.md) | 8 | Fetches current satellite Keplerian data asynchronously, then loads it. |
| [`INIT`](../../reference/commands/init.md) | 5 | Re-initialise a legacy-compatible node link. |
| [`KILL`](../../reference/commands/kill.md) | 0 / 5 | Delete permitted messages; SYSOP has broader message-deletion scope. |
| [`LOAD/ALIASES`](../../reference/commands/load--aliases.md) | 9 | Reload aliases. |
| [`LOAD/BADIP`](../../reference/commands/load--badip.md) | 6 | Reload bad-IP data. |
| [`LOAD/BADMSG`](../../reference/commands/load--badmsg.md) | 9 | Reload bad-message data. |
| [`LOAD/BADWORDS`](../../reference/commands/load--badwords.md) | 9 | Reload bad-word data. |
| [`LOAD/BANDS`](../../reference/commands/load--bands.md) | 9 | Reload band definitions. |
| [`LOAD/CMD_CACHE`](../../reference/commands/load--cmd-cache.md) | 9 | Reload command cache. |
| [`LOAD/DB`](../../reference/commands/load--db.md) | 9 | Reload database definitions/state. |
| [`LOAD/DXQSL`](../../reference/commands/load--dxqsl.md) | 9 | Reload DX QSL data. |
| [`LOAD/FORWARD`](../../reference/commands/load--forward.md) | 9 | Reload message forwarding configuration. |
| [`LOAD/HOPS`](../../reference/commands/load--hops.md) | 9 | Reload hop configuration. |
| [`LOAD/KEPS`](../../reference/commands/load--keps.md) | 5 | Reload satellite Keplerian data. |
| [`LOAD/MESSAGES`](../../reference/commands/load--messages.md) | 9 | Reload message text/configuration. |
| [`LOAD/PREFIXES`](../../reference/commands/load--prefixes.md) | 9 | Reload prefix data. |
| [`LOAD/QSL`](../../reference/commands/load--qsl.md) | 9 | Alias of LOAD/DXQSL. |
| [`LOAD/SWOP`](../../reference/commands/load--swop.md) | 9 | Reload SWOP data. |
| [`LOAD/USDB`](../../reference/commands/load--usdb.md) | 9 | Reload US callsign database data. |
| [`MERGE`](../../reference/commands/merge.md) | 5 | Administrative merge operation. |
| [`MRTG`](../../reference/commands/mrtg.md) | operational | Generate MRTG configuration/data and optional plots for node statistics. |
| [`MSG`](../../reference/commands/msg.md) | 9 | Administrative message-system command. |
| [`NOSPAWN`](../../reference/commands/nospawn.md) | 2 | Run a command without the normal spawn/user impersonation path; local only. |
| [`PC`](../../reference/commands/pc.md) | 8 | Send arbitrary text/protocol to a connected callsign. |
| [`PING`](../../reference/commands/ping.md) | 0 / 1 | Ping a node; authorization d mode provides broader operational access. |
| [`authorization `](../../reference/commands/authorization .md) | 9 | authorization -management command/compatibility entry; prefer SET/authorization . |
| [`RCMD`](../../reference/commands/rcmd.md) | 1 | Send a remote command to another cluster node. |
| [`READ`](../../reference/commands/read.md) | 0 / 5 | Read permitted messages; SYSOP may read any message. |
| [`REJECT/ANNOUNCE`](../../reference/commands/reject--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/RBN`](../../reference/commands/reject--rbn.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/ROUTE`](../../reference/commands/reject--route.md) | 8 | Create/update a reject filter for `route`. |
| [`REJECT/SPOTS`](../../reference/commands/reject--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/WCY`](../../reference/commands/reject--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/WWV`](../../reference/commands/reject--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`RINIT`](../../reference/commands/rinit.md) | 5 | Reverse-initialise a connected node and resend local configuration. |
| [`RUN`](../../reference/commands/run.md) | 0 / 8 | Run a script; higher authorization is required for scripts targeted at another callsign. |
| [`SAVE`](../../reference/commands/save.md) | 9 | Save command output to a file. |
| [`SEND_CONFIG`](../../reference/commands/send-config.md) | 6 | Broadcast PC92 C configuration records. |
| [`SET/AGWENGINE`](../../reference/commands/set--agwengine.md) | 9 | Enable or configure `agwengine`. |
| [`SET/AGWMONITOR`](../../reference/commands/set--agwmonitor.md) | 9 | Enable or configure `agwmonitor`. |
| [`SET/ARCLUSTER`](../../reference/commands/set--arcluster.md) | 5 | Enable or configure `arcluster`. |
| [`SET/BADDX`](../../reference/commands/set--baddx.md) | 6 | Enable or configure `baddx`. |
| [`SET/BADIP`](../../reference/commands/set--badip.md) | 6 | Enable or configure `badip`. |
| [`SET/BADNODE`](../../reference/commands/set--badnode.md) | 6 | Enable or configure `badnode`. |
| [`SET/BADSPOTTER`](../../reference/commands/set--badspotter.md) | 6 | Enable or configure `badspotter`. |
| [`SET/BADWORD`](../../reference/commands/set--badword.md) | 6 | Enable or configure `badword`. |
| [`SET/BBS`](../../reference/commands/set--bbs.md) | 5 | Enable or configure `bbs`. |
| [`SET/BELIEVE`](../../reference/commands/set--believe.md) | 6 | Administrative node flag. |
| [`SET/CCLUSTER`](../../reference/commands/set--ccluster.md) | 5 | Enable or configure `ccluster`. |
| [`SET/CLX`](../../reference/commands/set--clx.md) | 5 | Enable or configure `clx`. |
| [`SET/DEBUG`](../../reference/commands/set--debug.md) | 9 | Enable or configure `debug`. |
| [`SET/DXNET`](../../reference/commands/set--dxnet.md) | 5 | Enable or configure `dxnet`. |
| [`SET/EXTERNAL_IP`](../../reference/commands/set--external-ip.md) | 8 | Sets or refreshes the node external IP/host information. |
| [`SET/HOPS`](../../reference/commands/set--hops.md) | 8 | Enable or configure `hops`. |
| [`SET/ISOLATE`](../../reference/commands/set--isolate.md) | 9 | Enable or configure `isolate`. |
| [`SET/LOCAL_NODE`](../../reference/commands/set--local-node.md) | 5 | Enable or configure `local_node`. |
| [`SET/LOCKOUT`](../../reference/commands/set--lockout.md) | 9 | Enable or configure `lockout`. |
| [`SET/MAXCONNECT`](../../reference/commands/set--maxconnect.md) | 8 | Enable or configure `maxconnect`. |
| [`SET/NODE`](../../reference/commands/set--node.md) | 5 | Enable or configure `node`. |
| [`SET/OBSCOUNT`](../../reference/commands/set--obscount.md) | 8 | Enable or configure `obscount`. |
| [`SET/PASSPHRASE`](../../reference/commands/set--passphrase.md) | 9 | Sets a passphrase; local authorization d operation. |
| [`SET/PASSWORD`](../../reference/commands/set--password.md) | 0 / 9 | Own-password form is user-level; targeted form requires authorization . |
| [`SET/PINGINTERVAL`](../../reference/commands/set--pinginterval.md) | 9 | Enable or configure `pinginterval`. |
| [`SET/authorization `](../../reference/commands/set--authorization .md) | 9 | Enable or configure `authorization `. |
| [`SET/RBN`](../../reference/commands/set--rbn.md) | 9 | Enable or configure `rbn`. |
| [`SET/REGISTER`](../../reference/commands/set--register.md) | 9 | Enable or configure `register`. |
| [`SET/ROUTEPC19`](../../reference/commands/set--routepc19.md) | 9 | Administrative legacy-routing compatibility flag. |
| [`SET/SEND_DBG`](../../reference/commands/set--send-dbg.md) | 8 | Enables debug sending on the target/node context. |
| [`SET/SENDPC16`](../../reference/commands/set--sendpc16.md) | 9 | Administrative legacy PC16 sending flag. |
| [`SET/SPIDER`](../../reference/commands/set--spider.md) | 5 | Marks a callsign as a DXSpider node. |
| [`SET/STARTUP`](../../reference/commands/set--startup.md) | 0 / 6 | User creates own startup script; SYSOP may create one for another callsign. |
| [`SET/SYS_LOCATION`](../../reference/commands/set--sys-location.md) | 9 | Enable or configure `sys_location`. |
| [`SET/SYS_QRA`](../../reference/commands/set--sys-qra.md) | 9 | Enable or configure `sys_qra`. |
| [`SET/USDB`](../../reference/commands/set--usdb.md) | 9 | Enable or configure `usdb`. |
| [`SET/USER`](../../reference/commands/set--user.md) | 5 | Marks a callsign as a normal user. |
| [`SET/VAR`](../../reference/commands/set--var.md) | 9 | Sets an internal variable; local authorization d operation. |
| [`SET/WANTPC16`](../../reference/commands/set--wantpc16.md) | 9 | Administrative legacy PC16 preference. |
| [`SET/WANTPC9X`](../../reference/commands/set--wantpc9x.md) | 9 | Administrative PC9x preference. |
| [`SET/WANTRBN`](../../reference/commands/set--wantrbn.md) | 0 / 9 | User selects RBN categories; a authorization -9 targeted form is available to SYSOP. |
| [`SHOW/BADDX`](../../reference/commands/show--baddx.md) | 1 | Display `baddx`. |
| [`SHOW/BADIP`](../../reference/commands/show--badip.md) | 6 | Shows bad-IP data. |
| [`SHOW/BADNODE`](../../reference/commands/show--badnode.md) | 1 | Display `badnode`. |
| [`SHOW/BADSPOTTER`](../../reference/commands/show--badspotter.md) | 1 | Display `badspotter`. |
| [`SHOW/BADWORD`](../../reference/commands/show--badword.md) | 6 | Shows bad-word data. |
| [`SHOW/CMD_CACHE`](../../reference/commands/show--cmd-cache.md) | 9 | Display `cmd_cache`. |
| [`SHOW/CONNECT`](../../reference/commands/show--connect.md) | 1 | Display `connect`. |
| [`SHOW/DEBUG`](../../reference/commands/show--debug.md) | 9 | Display `debug`. |
| [`SHOW/DEBUG_RING`](../../reference/commands/show--debug-ring.md) | 9 | Shows the in-memory debug ring. |
| [`SHOW/DUP_ANN`](../../reference/commands/show--dup-ann.md) | 9 | Shows duplicate announcement tracking. |
| [`SHOW/DUP_EPH`](../../reference/commands/show--dup-eph.md) | 9 | Shows duplicate ephemeral tracking. |
| [`SHOW/DUP_SPOTS`](../../reference/commands/show--dup-spots.md) | 9 | Shows duplicate spot tracking. |
| [`SHOW/DUP_WCY`](../../reference/commands/show--dup-wcy.md) | 9 | Shows duplicate WCY tracking. |
| [`SHOW/DUP_WWV`](../../reference/commands/show--dup-wwv.md) | 9 | Shows duplicate WWV tracking. |
| [`SHOW/EXTERNAL_IP`](../../reference/commands/show--external-ip.md) | 8 | Shows the node external IP information. |
| [`SHOW/HOPS`](../../reference/commands/show--hops.md) | 8 | Display `hops`. |
| [`SHOW/ISOLATE`](../../reference/commands/show--isolate.md) | 1 | Display `isolate`. |
| [`SHOW/LOCKOUT`](../../reference/commands/show--lockout.md) | 9 | Display `lockout`. |
| [`SHOW/LOG`](../../reference/commands/show--log.md) | 8 | Display `log`. |
| [`SHOW/MSG_STATUS`](../../reference/commands/show--msg-status.md) | 5 | Shows message-system status information. |
| [`SHOW/NODE`](../../reference/commands/show--node.md) | 1 | Shows node type/version information. |
| [`SHOW/PROGRAM`](../../reference/commands/show--program.md) | 5 | Shows loaded program module locations. |
| [`SHOW/RBN`](../../reference/commands/show--rbn.md) | 1 | Display `rbn`. |
| [`SHOW/RCMD`](../../reference/commands/show--rcmd.md) | 9 | Display `rcmd`. |
| [`SHOW/REGISTERED`](../../reference/commands/show--registered.md) | 9 | Display `registered`. |
| [`SHOW/SEEME`](../../reference/commands/show--seeme.md) | 9 | Shows RBN seeme state. |
| [`SHOW/SPOTSTATS`](../../reference/commands/show--spotstats.md) | 1 | Display `spotstats`. |
| [`SHOW/STARTUP`](../../reference/commands/show--startup.md) | 0 / 6 | Own startup script is user-level; another callsign requires authorization . |
| [`SHOW/STATION`](../../reference/commands/show--station.md) | 0 / 6 | Normal lookup is user-level; SHOW/STATION ALL requires authorization . |
| [`SHOW/TALK`](../../reference/commands/show--talk.md) | 0 / 6 | User can view own talk log; SYSOP can inspect another callsign. |
| [`SHOW/VAR`](../../reference/commands/show--var.md) | 9 | Shows internal variables; local authorization d operation. |
| [`SHOW/VERSION`](../../reference/commands/show--version.md) | 0 / 6 | Normal version summary is user-visible; extended node/version query requires higher authorization . |
| [`SHU`](../../reference/commands/shu.md) | 5 | Guard/abbreviation handler requiring a longer SHUTDOWN command. |
| [`SHUTDOWN`](../../reference/commands/shutdown.md) | 5 | Shut down the cluster and disconnect users. |
| [`SPOOF`](../../reference/commands/spoof.md) | 9 | Run a command as another user. |
| [`STAT/CHANNEL`](../../reference/commands/stat--channel.md) | 5 | Shows internal channel-object state. |
| [`STAT/DB`](../../reference/commands/stat--db.md) | 5 | Shows internal database descriptor state. |
| [`STAT/MSG`](../../reference/commands/stat--msg.md) | 1 | Shows message-system or message internal state. |
| [`STAT/PC19LIST`](../../reference/commands/stat--pc19list.md) | 9 | Shows internal PC19 tracking/list state. |
| [`STAT/ROUTE_NODE`](../../reference/commands/stat--route-node.md) | 5 | Shows Route::Node object data. |
| [`STAT/ROUTE_USER`](../../reference/commands/stat--route-user.md) | 5 | Shows Route::User object data. |
| [`STAT/USER`](../../reference/commands/stat--user.md) | 5 | Shows full internal user-record state. |
| [`UNCATCHUP`](../../reference/commands/uncatchup.md) | 5 | Undo CATCHUP forwarding marks. |
| [`UNSET/AGWENGINE`](../../reference/commands/unset--agwengine.md) | 9 | Disable or clear `agwengine`. |
| [`UNSET/AGWMONITOR`](../../reference/commands/unset--agwmonitor.md) | 9 | Disable or clear `agwmonitor`. |
| [`UNSET/BADDX`](../../reference/commands/unset--baddx.md) | 6 | Disable or clear `baddx`. |
| [`UNSET/BADNODE`](../../reference/commands/unset--badnode.md) | 6 | Disable or clear `badnode`. |
| [`UNSET/BADSPOTTER`](../../reference/commands/unset--badspotter.md) | 6 | Disable or clear `badspotter`. |
| [`UNSET/BADWORD`](../../reference/commands/unset--badword.md) | 6 | Disable or clear `badword`. |
| [`UNSET/BELIEVE`](../../reference/commands/unset--believe.md) | 6 | Clears the administrative believe flag. |
| [`UNSET/DEBUG`](../../reference/commands/unset--debug.md) | 9 | Disable or clear `debug`. |
| [`UNSET/HOPS`](../../reference/commands/unset--hops.md) | 8 | Disable or clear `hops`. |
| [`UNSET/ISOLATE`](../../reference/commands/unset--isolate.md) | 9 | Disable or clear `isolate`. |
| [`UNSET/LOCAL_NODE`](../../reference/commands/unset--local-node.md) | 5 | Disable or clear `local_node`. |
| [`UNSET/LOCKOUT`](../../reference/commands/unset--lockout.md) | 9 | Disable or clear `lockout`. |
| [`UNSET/PASSPHRASE`](../../reference/commands/unset--passphrase.md) | 9 | Clears a passphrase; local authorization d operation. |
| [`UNSET/PASSWORD`](../../reference/commands/unset--password.md) | 9 | Disable or clear `password`. |
| [`UNSET/REGISTER`](../../reference/commands/unset--register.md) | 9 | Disable or clear `register`. |
| [`UNSET/ROUTEPC19`](../../reference/commands/unset--routepc19.md) | 9 | Clears legacy route-PC19 compatibility flag. |
| [`UNSET/SEND_DBG`](../../reference/commands/unset--send-dbg.md) | 8 | Disables debug sending. |
| [`UNSET/SENDPC16`](../../reference/commands/unset--sendpc16.md) | 9 | Clears legacy PC16 sending flag. |
| [`UNSET/STARTUP`](../../reference/commands/unset--startup.md) | 0 / 6 | User removes own startup script; SYSOP may remove another callsign’s startup. |
| [`UNSET/WANTPC16`](../../reference/commands/unset--wantpc16.md) | 9 | Clears administrative PC16 preference. |
| [`UNSET/WANTPC9X`](../../reference/commands/unset--wantpc9x.md) | 9 | Clears administrative PC9x preference. |
| [`WCY`](../../reference/commands/wcy.md) | operational | Inject/send WCY data; operational command. |
| [`WWV`](../../reference/commands/wwv.md) | operational | Inject/send WWV data; operational command. |
| [`WX`](../../reference/commands/wx.md) | 0 / 5 | Send local/full weather messages; SYSOP form targets other clusters. |