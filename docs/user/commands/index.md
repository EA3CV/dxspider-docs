# User command reference

Commands available to normal users are listed here. DUAL commands also have a separate authorization d form.

| Command | authorization | Scope |
|---|---:|---|
| [`ACCEPT/ANNOUNCE`](../../reference/commands/accept--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/RBN`](../../reference/commands/accept--rbn.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/SPOTS`](../../reference/commands/accept--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/WCY`](../../reference/commands/accept--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ACCEPT/WWV`](../../reference/commands/accept--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`ANNOUNCE`](../../reference/commands/announce.md) | 0 / 5 | Send local or cluster-wide announcements; SYSOP form targets sysops. |
| [`APROPOS`](../../reference/commands/apropos.md) | 0 | Search the built-in help database. |
| [`BLANK`](../../reference/commands/blank.md) | 0 | Print blank or repeated separator lines. |
| [`BYE`](../../reference/commands/bye.md) | 0 | Disconnect from the cluster. |
| [`CHAT`](../../reference/commands/chat.md) | 0 | Send a message to a joined chat/conference group. |
| [`CLEAR/ANNOUNCE`](../../reference/commands/clear--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/RBN`](../../reference/commands/clear--rbn.md) | 0 / 8 | User form clears own RBN filter; SYSOP form can target another callsign/default. |
| [`CLEAR/ROUTE`](../../reference/commands/clear--route.md) | 0 / 8 | User and SYSOP route-filter forms exist. |
| [`CLEAR/SPOTS`](../../reference/commands/clear--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/WCY`](../../reference/commands/clear--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`CLEAR/WWV`](../../reference/commands/clear--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`DBAVAIL`](../../reference/commands/dbavail.md) | 0 | List databases defined on the node. |
| [`DBSHOW`](../../reference/commands/dbshow.md) | 0 | Query a defined database. |
| [`DIRECTORY`](../../reference/commands/directory.md) | 0 / 5 | List messages; SYSOP can see otherwise hidden/private entries. |
| [`DISABLE/AUTOFTX`](../../reference/commands/disable--autoftx.md) | 0 | Disable `autoftx`. |
| [`DISABLE/FTX`](../../reference/commands/disable--ftx.md) | 0 | Disable `ftx`. |
| [`DX`](../../reference/commands/dx.md) | 0 / 2 | Send a DX spot; authorization d form accepts additional origin metadata. |
| [`ECHO`](../../reference/commands/echo.md) | 0 | Echo text/input. |
| [`ENABLE/AUTOFTX`](../../reference/commands/enable--autoftx.md) | 0 | Enable `autoftx`. |
| [`ENABLE/FTX`](../../reference/commands/enable--ftx.md) | 0 | Enable `ftx`. |
| [`HELP`](../../reference/commands/help.md) | 0 | Show command help. |
| [`JOIN`](../../reference/commands/join.md) | 0 | Join a chat/conference group. |
| [`KILL`](../../reference/commands/kill.md) | 0 / 5 | Delete permitted messages; SYSOP has broader message-deletion scope. |
| [`LEAVE`](../../reference/commands/leave.md) | 0 | Leave a chat/conference group. |
| [`LINKS`](../../reference/commands/links.md) | 0 | Show link information. |
| [`PING`](../../reference/commands/ping.md) | 0 / 1 | Ping a node; authorization d mode provides broader operational access. |
| [`READ`](../../reference/commands/read.md) | 0 / 5 | Read permitted messages; SYSOP may read any message. |
| [`REJECT/ANNOUNCE`](../../reference/commands/reject--announce.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/RBN`](../../reference/commands/reject--rbn.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/SPOTS`](../../reference/commands/reject--spots.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/WCY`](../../reference/commands/reject--wcy.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REJECT/WWV`](../../reference/commands/reject--wwv.md) | 0 / 8 | User form plus SYSOP form for another callsign/default filter. |
| [`REPLY`](../../reference/commands/reply.md) | 0 | Reply to a message, with bulletin/private/read-receipt variants. |
| [`RUN`](../../reference/commands/run.md) | 0 / 8 | Run a script; higher authorization is required for scripts targeted at another callsign. |
| [`SEND`](../../reference/commands/send.md) | 0 | Compose and send personal or bulletin messages. |
| [`SET/ADDRESS`](../../reference/commands/set--address.md) | 0 | Enable or configure `address`. |
| [`SET/ANNOUNCE`](../../reference/commands/set--announce.md) | 0 | Enable or configure `announce`. |
| [`SET/ANNTALK`](../../reference/commands/set--anntalk.md) | 0 | Enable or configure `anntalk`. |
| [`SET/BEEP`](../../reference/commands/set--beep.md) | 0 | Enable or configure `beep`. |
| [`SET/BUDDY`](../../reference/commands/set--buddy.md) | 0 | Enable or configure `buddy`. |
| [`SET/DX`](../../reference/commands/set--dx.md) | 0 | Enable or configure `dx`. |
| [`SET/DXCQ`](../../reference/commands/set--dxcq.md) | 0 | Enable or configure `dxcq`. |
| [`SET/DXGRID`](../../reference/commands/set--dxgrid.md) | 0 | Enable or configure `dxgrid`. |
| [`SET/DXITU`](../../reference/commands/set--dxitu.md) | 0 | Enable or configure `dxitu`. |
| [`SET/ECHO`](../../reference/commands/set--echo.md) | 0 | Enable or configure `echo`. |
| [`SET/EMAIL`](../../reference/commands/set--email.md) | 0 | Enable or configure `email`. |
| [`SET/GTK`](../../reference/commands/set--gtk.md) | 0 | Enables GTK/enhanced mode for the current session. |
| [`SET/HERE`](../../reference/commands/set--here.md) | 0 | Enable or configure `here`. |
| [`SET/HOMEBBS`](../../reference/commands/set--homebbs.md) | code: current user | Exists in code; sets and persists current user's home BBS; absent from help/manual/wiki. |
| [`SET/HOMENODE`](../../reference/commands/set--homenode.md) | 0 | Enable or configure `homenode`. |
| [`SET/LANGUAGE`](../../reference/commands/set--language.md) | 0 | Enable or configure `language`. |
| [`SET/LOCATION`](../../reference/commands/set--location.md) | 0 | Enable or configure `location`. |
| [`SET/LOGININFO`](../../reference/commands/set--logininfo.md) | 0 | Enable or configure `logininfo`. |
| [`SET/NAME`](../../reference/commands/set--name.md) | 0 | Enable or configure `name`. |
| [`SET/PAGE`](../../reference/commands/set--page.md) | 0 | Sets the user paging preference and stores it in the profile. |
| [`SET/PASSWORD`](../../reference/commands/set--password.md) | 0 / 9 | Own-password form is user-level; targeted form requires authorization . |
| [`SET/PROMPT`](../../reference/commands/set--prompt.md) | 0 | Enable or configure `prompt`. |
| [`SET/QRA`](../../reference/commands/set--qra.md) | 0 | Enable or configure `qra`. |
| [`SET/QTH`](../../reference/commands/set--qth.md) | 0 | Enable or configure `qth`. |
| [`SET/SEEME`](../../reference/commands/set--seeme.md) | 0 | Enables the current user/session RBN “seeme” preference. |
| [`SET/SEEMEE`](../../reference/commands/set--seemee.md) | 0 | Enables and persists the current user “seemee” preference. |
| [`SET/STARTUP`](../../reference/commands/set--startup.md) | 0 / 6 | User creates own startup script; SYSOP may create one for another callsign. |
| [`SET/TALK`](../../reference/commands/set--talk.md) | 0 | Enables talk messages for the current user. |
| [`SET/USSTATE`](../../reference/commands/set--usstate.md) | 0 | Enable or configure `usstate`. |
| [`SET/VE7CC`](../../reference/commands/set--ve7cc.md) | 0 | Enables VE7CC compatibility mode for the current session. |
| [`SET/WANTRBN`](../../reference/commands/set--wantrbn.md) | 0 / 9 | User selects RBN categories; a authorization -9 targeted form is available to SYSOP. |
| [`SET/WCY`](../../reference/commands/set--wcy.md) | 0 | Enable or configure `wcy`. |
| [`SET/WIDTH`](../../reference/commands/set--width.md) | code: current user | Exists in code; updates active width and stored user width; absent from help/manual/wiki. |
| [`SET/WWV`](../../reference/commands/set--wwv.md) | 0 | Enable or configure `wwv`. |
| [`SET/WX`](../../reference/commands/set--wx.md) | 0 | Enable or configure `wx`. |
| [`SHOW/425`](../../reference/commands/show--425.md) | 0 | Queries the 425 DX News service asynchronously. |
| [`SHOW/ANNOUNCE`](../../reference/commands/show--announce.md) | 0 | Display `announce`. |
| [`SHOW/BANDS`](../../reference/commands/show--bands.md) | 0 | Display `bands`. |
| [`SHOW/BUDDY`](../../reference/commands/show--buddy.md) | 0 | Display `buddy`. |
| [`SHOW/CHAT`](../../reference/commands/show--chat.md) | 0 | Display `chat`. |
| [`SHOW/CLUSTER`](../../reference/commands/show--cluster.md) | 0 | Shows current cluster information. |
| [`SHOW/CONFIGURATION`](../../reference/commands/show--configuration.md) | 0 | Display `configuration`. |
| [`SHOW/CONTEST`](../../reference/commands/show--contest.md) | 0 | Display `contest`. |
| [`SHOW/DATA_STATS`](../../reference/commands/show--data-stats.md) | 0 | Shows node data-transfer statistics. |
| [`SHOW/DATE`](../../reference/commands/show--date.md) | 0 | Display `date`. |
| [`SHOW/DB0SDX`](../../reference/commands/show--db0sdx.md) | 0 | Display `db0sdx`. |
| [`SHOW/DX`](../../reference/commands/show--dx.md) | 0 | Display `dx`. |
| [`SHOW/DXQSL`](../../reference/commands/show--dxqsl.md) | 0 | Display `dxqsl`. |
| [`SHOW/DXSTATS`](../../reference/commands/show--dxstats.md) | 0 | Display `dxstats`. |
| [`SHOW/FILES`](../../reference/commands/show--files.md) | 0 | Display `files`. |
| [`SHOW/FILTER`](../../reference/commands/show--filter.md) | 0 | Display `filter`. |
| [`SHOW/GRAYLINE`](../../reference/commands/show--grayline.md) | 0 | Display `grayline`. |
| [`SHOW/GROUPS`](../../reference/commands/show--groups.md) | 0 | Shows chat/conference groups. |
| [`SHOW/HEADING`](../../reference/commands/show--heading.md) | 0 | Shows heading information. |
| [`SHOW/HFSTATS`](../../reference/commands/show--hfstats.md) | 0 | Display `hfstats`. |
| [`SHOW/HFTABLE`](../../reference/commands/show--hftable.md) | 0 | Display `hftable`. |
| [`SHOW/IK3QAR`](../../reference/commands/show--ik3qar.md) | 0 | Display `ik3qar`. |
| [`SHOW/MOON`](../../reference/commands/show--moon.md) | 0 | Display `moon`. |
| [`SHOW/MOTD`](../../reference/commands/show--motd.md) | 0 | Display `motd`. |
| [`SHOW/MUF`](../../reference/commands/show--muf.md) | 0 | Display `muf`. |
| [`SHOW/NEWCONFIGURATION`](../../reference/commands/show--newconfiguration.md) | 0 | Display `newconfiguration`. |
| [`SHOW/PREFIX`](../../reference/commands/show--prefix.md) | 0 | Display `prefix`. |
| [`SHOW/QRA`](../../reference/commands/show--qra.md) | 0 | Display `qra`. |
| [`SHOW/QRZ`](../../reference/commands/show--qrz.md) | 0 | Display `qrz`. |
| [`SHOW/ROUTE`](../../reference/commands/show--route.md) | 0 | Display `route`. |
| [`SHOW/SATELLITE`](../../reference/commands/show--satellite.md) | 0 | Display `satellite`. |
| [`SHOW/STARTUP`](../../reference/commands/show--startup.md) | 0 / 6 | Own startup script is user-level; another callsign requires authorization . |
| [`SHOW/STATION`](../../reference/commands/show--station.md) | 0 / 6 | Normal lookup is user-level; SHOW/STATION ALL requires authorization . |
| [`SHOW/SUN`](../../reference/commands/show--sun.md) | 0 | Display `sun`. |
| [`SHOW/TALK`](../../reference/commands/show--talk.md) | 0 / 6 | User can view own talk log; SYSOP can inspect another callsign. |
| [`SHOW/TIME`](../../reference/commands/show--time.md) | 0 | Display `time`. |
| [`SHOW/USDB`](../../reference/commands/show--usdb.md) | 0 | Display `usdb`. |
| [`SHOW/USERS`](../../reference/commands/show--users.md) | 0 | Shows users from current routing/user data. |
| [`SHOW/VERSION`](../../reference/commands/show--version.md) | 0 / 6 | Normal version summary is user-visible; extended node/version query requires higher authorization . |
| [`SHOW/VHFSTATS`](../../reference/commands/show--vhfstats.md) | 0 | Display `vhfstats`. |
| [`SHOW/VHFTABLE`](../../reference/commands/show--vhftable.md) | 0 | Display `vhftable`. |
| [`SHOW/WCY`](../../reference/commands/show--wcy.md) | 0 | Display `wcy`. |
| [`SHOW/WM7D`](../../reference/commands/show--wm7d.md) | 0 | Display `wm7d`. |
| [`SHOW/WWV`](../../reference/commands/show--wwv.md) | 0 | Display `wwv`. |
| [`SHOW/WX`](../../reference/commands/show--wx.md) | 0 | Shows recent weather messages. |
| [`STAT/NODECONFIG`](../../reference/commands/stat--nodeconfig.md) | 0 | Advanced diagnostic view of node configuration state. |
| [`STAT/ROUTE`](../../reference/commands/stat--route.md) | 0 | Advanced diagnostic view of routing state. |
| [`STAT/USERCONFIG`](../../reference/commands/stat--userconfig.md) | 0 | Advanced diagnostic view of user configuration state. |
| [`SYSOP`](../../reference/commands/sysop.md) | 0 | Regain configured SYSOP authorization s after a remote login challenge. |
| [`TALK`](../../reference/commands/talk.md) | 0 | Send a talk message or enter talk mode. |
| [`TYPE`](../../reference/commands/type.md) | 0 | Display a file from a configured file area. |
| [`UNSET/ANNOUNCE`](../../reference/commands/unset--announce.md) | 0 | Disable or clear `announce`. |
| [`UNSET/ANNTALK`](../../reference/commands/unset--anntalk.md) | 0 | Disable or clear `anntalk`. |
| [`UNSET/BEEP`](../../reference/commands/unset--beep.md) | 0 | Disable or clear `beep`. |
| [`UNSET/BUDDY`](../../reference/commands/unset--buddy.md) | 0 | Disable or clear `buddy`. |
| [`UNSET/DX`](../../reference/commands/unset--dx.md) | 0 | Disable or clear `dx`. |
| [`UNSET/DXCQ`](../../reference/commands/unset--dxcq.md) | 0 | Disable or clear `dxcq`. |
| [`UNSET/DXGRID`](../../reference/commands/unset--dxgrid.md) | 0 | Disable or clear `dxgrid`. |
| [`UNSET/DXITU`](../../reference/commands/unset--dxitu.md) | 0 | Disable or clear `dxitu`. |
| [`UNSET/ECHO`](../../reference/commands/unset--echo.md) | 0 | Disable or clear `echo`. |
| [`UNSET/EMAIL`](../../reference/commands/unset--email.md) | 0 | Disable or clear `email`. |
| [`UNSET/GTK`](../../reference/commands/unset--gtk.md) | 0 | Disables GTK/enhanced mode for the current session. |
| [`UNSET/HERE`](../../reference/commands/unset--here.md) | 0 | Disable or clear `here`. |
| [`UNSET/LOGININFO`](../../reference/commands/unset--logininfo.md) | 0 | Disable or clear `logininfo`. |
| [`UNSET/authorization `](../../reference/commands/unset--authorization .md) | 0 | Drops authorization for the current session. |
| [`UNSET/PROMPT`](../../reference/commands/unset--prompt.md) | 0 | Disable or clear `prompt`. |
| [`UNSET/SEEME`](../../reference/commands/unset--seeme.md) | 0 | Disables current-user RBN seeme preference. |
| [`UNSET/STARTUP`](../../reference/commands/unset--startup.md) | 0 / 6 | User removes own startup script; SYSOP may remove another callsign’s startup. |
| [`UNSET/TALK`](../../reference/commands/unset--talk.md) | 0 | Disables talk messages for the current user. |
| [`UNSET/USSTATE`](../../reference/commands/unset--usstate.md) | 0 | Disable or clear `usstate`. |
| [`UNSET/VE7CC`](../../reference/commands/unset--ve7cc.md) | 0 | Disables VE7CC compatibility mode. |
| [`UNSET/WANTRBN`](../../reference/commands/unset--wantrbn.md) | 0 | Disable or clear `wantrbn`. |
| [`UNSET/WCY`](../../reference/commands/unset--wcy.md) | 0 | Disable or clear `wcy`. |
| [`UNSET/WWV`](../../reference/commands/unset--wwv.md) | 0 | Disable or clear `wwv`. |
| [`UNSET/WX`](../../reference/commands/unset--wx.md) | 0 | Disable or clear `wx`. |
| [`UPTIME`](../../reference/commands/uptime.md) | 0 | Show node uptime. |
| [`WHO`](../../reference/commands/who.md) | 0 | Show callsigns physically connected to the node. |
| [`WX`](../../reference/commands/wx.md) | 0 / 5 | Send local/full weather messages; SYSOP form targets other clusters. |