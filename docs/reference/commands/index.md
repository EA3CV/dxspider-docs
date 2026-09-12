# Command Reference

Search or browse the current command set. The inventory is generated from `cmd/*.pl`; implementation evidence is authoritative and `Commands_en.hlp` is secondary.

<div class="command-filter" markdown>
Use the site search (`/`) for instant lookup by command name, option or help text.
</div>

| Command | Guide | What it does |
|---|---|---|
| [`ACCEPT/ANNOUNCE`](accept--announce.md) | No direct handler guard | Set an 'accept' filter line for announce |
| [`ACCEPT/RBN`](accept--rbn.md) | No direct handler guard | Apply an accept filter specifically to RBN/Skimmer spots. |
| [`ACCEPT/ROUTE`](accept--route.md) | No direct handler guard | Set an 'accept' filter line for routing |
| [`ACCEPT/SPOTS`](accept--spots.md) | No direct handler guard | Allow only DX spots that match one or more filter rules. |
| [`ACCEPT/WCY`](accept--wcy.md) | No direct handler guard | set an 'accept' WCY filter |
| [`ACCEPT/WWV`](accept--wwv.md) | No direct handler guard | set an 'accept' WWV filter |
| [`AGWRESTART`](agwrestart.md) | Direct administration guard | restart an agw connection |
| [`ANNOUNCE`](announce.md) | Direct administration guard | Send local, cluster-wide or SYSOP-only announcements. |
| [`APROPOS`](apropos.md) | No direct handler guard | Search help database for <string> |
| [`BLANK`](blank.md) | No direct handler guard | Print nn (default 1) blank lines (or strings) |
| [`BYE`](bye.md) | No direct handler guard | Exit from the cluster |
| [`CATCHUP`](catchup.md) | Direct administration guard | Mark a message as sent |
| [`CHAT`](chat.md) | No direct handler guard | Chat or Conference to a group |
| [`CLEAR/ANNOUNCE`](clear--announce.md) | No direct handler guard | Clear a announce filter line |
| [`CLEAR/CMD_CACHE`](clear--cmd-cache.md) | Direct administration guard | reset/reload the short name command cache you may need to do this if you remove files or the system gets confused about where it should be loading its cmd files |
| [`CLEAR/DUPEFILE`](clear--dupefile.md) | Direct administration guard | Clear out the dupefile completely |
| [`CLEAR/RBN`](clear--rbn.md) | No direct handler guard | clear filters commands |
| [`CLEAR/ROUTE`](clear--route.md) | No direct handler guard | Clear a route filter line |
| [`CLEAR/SPOTS`](clear--spots.md) | No direct handler guard | Remove one line or the complete DX spot filter. |
| [`CLEAR/WCY`](clear--wcy.md) | No direct handler guard | Clear a WCY filter line |
| [`CLEAR/WWV`](clear--wwv.md) | No direct handler guard | Clear a WWV filter line |
| [`CONNECT`](connect.md) | Direct administration guard | Start a connection to another DX Cluster |
| [`CREATE/USER`](create--user.md) | Direct administration guard | Create this user from the User Database |
| [`DBAVAIL`](dbavail.md) | No direct handler guard | Show a list of all the Databases in the system |
| [`DBCREATE`](dbcreate.md) | Direct administration guard | Create a database entry |
| [`DBDELKEY`](dbdelkey.md) | No direct handler guard | Database update routine |
| [`DBEXPORT`](dbexport.md) | Direct administration guard | Export an AK1A data to a file |
| [`DBIMPORT`](dbimport.md) | Direct administration guard | Import AK1A data into a database |
| [`DBREMOVE`](dbremove.md) | Direct administration guard | Delete a database |
| [`DBSHOW`](dbshow.md) | No direct handler guard | Display an entry, if it exists, in a database |
| [`DBUPDATE`](dbupdate.md) | No direct handler guard | Database update routine |
| [`DEBUG`](debug.md) | Direct administration guard | Set the cluster program into debug mode |
| [`DELETE/USDB`](delete--usdb.md) | Direct administration guard | Delete this user from the US State Database |
| [`DELETE/USER`](delete--user.md) | Direct administration guard | Delete this user from the User Database |
| [`DEMONSTRATE`](demonstrate.md) | Direct administration guard | Demonstrate a command to another user |
| [`DIRECTORY`](directory.md) | Direct administration guard | Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range. |
| [`DISABLE/AUTOFTX`](disable--autoftx.md) | No direct handler guard | Suppress FT4/FT8 spots whose comments look automatically generated, while retaining more useful human-entered FT4/FT8 spots. |
| [`DISABLE/FTX`](disable--ftx.md) | No direct handler guard | Suppress all spots whose comment contains FT4 or FT8. |
| [`DISCONNECT`](disconnect.md) | Direct administration guard | Disconnect user(s) or node(s) |
| [`DMESG`](dmesg.md) | No direct handler guard | Log the current values of the DXDebug dbgring butter |
| [`DO`](do.md) | Direct administration guard | do anything Rape me! |
| [`DOWNLOAD`](download.md) | Direct administration guard | Download a file into local_data |
| [`DX`](dx.md) | No direct handler guard | Send a DX spot into the cluster network. |
| [`DXQSL_EXPORT`](dxqsl-export.md) | Direct administration guard | Export SH/DXSQL information to a file |
| [`DXQSL_IMPORT`](dxqsl-import.md) | Direct administration guard | Import SH/DXSQL information from a file |
| [`ECHO`](echo.md) | No direct handler guard | Echo the line to the output |
| [`ENABLE/AUTOFTX`](enable--autoftx.md) | No direct handler guard | Enable Autogenerated FT4/8 spots |
| [`ENABLE/FTX`](enable--ftx.md) | No direct handler guard | Enable ALL FT4/8 Spots |
| [`EXPORT`](export.md) | Direct administration guard | Export a message to a file |
| [`EXPORT_USERS`](export-users.md) | No direct handler guard | Export the users database to ascii |
| [`FORWARD/LATLONG`](forward--latlong.md) | No direct handler guard | Send latitude and longitude information to another cluster |
| [`FORWARD/OPERNAME`](forward--opername.md) | Direct administration guard | Cause node to send PC41 info frames Mods by Dirk Koopman G1TLH 12Dec98 |
| [`GET/KEPS`](get--keps.md) | Direct administration guard | Obtain the latest AMSAT Keplarian Elements from the web |
| [`HELP`](help.md) | No direct handler guard | The HELP Command |
| [`INIT`](init.md) | Direct administration guard | Re-initialise a link to an AK1A compatible node |
| [`JOIN`](join.md) | No direct handler guard | Join a chat or conference group |
| [`KILL`](kill.md) | Direct administration guard | Delete a message from the local system |
| [`LEAVE`](leave.md) | No direct handler guard | Leave a chat or conference group |
| [`LINKS`](links.md) | No direct handler guard | Show which nodes is physically connected |
| [`LOAD/ALIASES`](load--aliases.md) | Direct administration guard | Reload the command alias table |
| [`LOAD/BADIP`](load--badip.md) | Direct administration guard | Reload the bad IP address table |
| [`LOAD/BADMSG`](load--badmsg.md) | Direct administration guard | Reload the bad msg table |
| [`LOAD/BADWORDS`](load--badwords.md) | Direct administration guard | Reload the bad words table |
| [`LOAD/BANDS`](load--bands.md) | Direct administration guard | Reload the band limits table |
| [`LOAD/CMD_CACHE`](load--cmd-cache.md) | Direct administration guard | Reload the automatic command cache |
| [`LOAD/DB`](load--db.md) | Direct administration guard | Reload the DB list |
| [`LOAD/DXQSL`](load--dxqsl.md) | Direct administration guard | load the QSL file after changing it |
| [`LOAD/FORWARD`](load--forward.md) | Direct administration guard | Reload the msg forwarding routing table |
| [`LOAD/HOPS`](load--hops.md) | Direct administration guard | load the node hop count table after changing it |
| [`LOAD/KEPS`](load--keps.md) | Direct administration guard | Load new keps data |
| [`LOAD/MESSAGES`](load--messages.md) | Direct administration guard | Reload the system messages file |
| [`LOAD/PREFIXES`](load--prefixes.md) | Direct administration guard | Reload the prefix table |
| [`LOAD/QSL`](load--qsl.md) | Direct administration guard | load the QSL file after changing it |
| [`LOAD/SWOP`](load--swop.md) | Direct administration guard | reload the swop file |
| [`LOAD/USDB`](load--usdb.md) | Direct administration guard | reload the usdb file Be warned, if this is the full database the size of your image will increase by at least 20Mb and all activity will stop for several |
| [`MERGE`](merge.md) | Direct administration guard | Ask for the latest spots and WWV |
| [`MRTG`](mrtg.md) | No direct handler guard | This is a local command to generate the various statistics that can then be displayed on an MRTG plot Your mrtg binary must live in one of the standard places |
| [`MSG`](msg.md) | Direct administration guard | Alter various message parameters |
| [`NOSPAWN`](nospawn.md) | Direct administration guard | pretend that you are another user, useful for reseting those silly things that people insist on getting wrong like set/homenode et al |
| [`PC`](pc.md) | Direct administration guard | Send text (eg PC Protocol) to <call> |
| [`PING`](ping.md) | No direct handler guard | User level link check command |
| [`PRIVILEGE`](privilege.md) | No direct handler guard | check the privilege of the user is at least n |
| [`RCMD`](rcmd.md) | Direct administration guard | Send a command to another DX Cluster |
| [`READ`](read.md) | Direct administration guard | Read the next unread personal message addressed to you |
| [`REGISTER/ACCEPT`](register--accept.md) | Direct administration guard | register/accept.pl - Accept a DXSpider registration request SYSOP only. Usage: |
| [`REGISTER/REJECT`](register--reject.md) | Direct administration guard | register/reject.pl - Reject a DXSpider registration request SYSOP only. Usage: |
| [`REGISTER/REMOVE`](register--remove.md) | Direct administration guard | register/remove.pl - Remove DXSpider registration for a callsign family SYSOP only. Usage: |
| [`REGISTER/REQUEST`](register--request.md) | No direct handler guard | register/request.pl - Create a DXSpider registration request Normal user: register/request <email> <EN|ES> [ssid-list] |
| [`REGISTER/SHOW`](register--show.md) | Direct administration guard | register/show.pl - Show DXSpider registration requests/history SYSOP only. Usage: |
| [`REJECT/ANNOUNCE`](reject--announce.md) | No direct handler guard | Set a 'reject' filter line for announce |
| [`REJECT/RBN`](reject--rbn.md) | No direct handler guard | Set a 'reject' filter line for RBN spots |
| [`REJECT/ROUTE`](reject--route.md) | No direct handler guard | Set an 'reject' filter line for routing |
| [`REJECT/SPOTS`](reject--spots.md) | No direct handler guard | Reject DX spots that match one or more filter rules. |
| [`REJECT/WCY`](reject--wcy.md) | No direct handler guard | set a 'reject' WCY filter |
| [`REJECT/WWV`](reject--wwv.md) | No direct handler guard | set a 'reject' WWV filter |
| [`REPLY`](reply.md) | No direct handler guard | Reply (privately) to the last message that you have read |
| [`RINIT`](rinit.md) | Direct administration guard | reverse init a cluster connection |
| [`RUN`](run.md) | Direct administration guard | the run command run a script from the scripts directory |
| [`SAVE`](save.md) | Direct administration guard | Save command output to a file |
| [`SEND`](send.md) | Direct administration guard | Send a message to one or more callsigns |
| [`SEND_CONFIG`](send-config.md) | No direct handler guard | Broadcast PC92 C records |
| [`SET/ADDRESS`](set--address.md) | No direct handler guard | Record your postal address |
| [`SET/AGWENGINE`](set--agwengine.md) | Direct administration guard | Enable the AGW Engine |
| [`SET/AGWMONITOR`](set--agwmonitor.md) | Direct administration guard | Enable Monitoring on the AGW Engine |
| [`SET/ANNOUNCE`](set--announce.md) | Direct administration guard | Allow announce messages to come out on your terminal |
| [`SET/ANNTALK`](set--anntalk.md) | Direct administration guard | Allow talk like announce messages on your terminal |
| [`SET/ARCLUSTER`](set--arcluster.md) | Direct administration guard | Make the callsign an AR-Cluster node |
| [`SET/BADDX`](set--baddx.md) | Direct administration guard | Stop callsigns in a dx spot being propagated |
| [`SET/BADIP`](set--badip.md) | Direct administration guard | Stop logins and spots with this IP address |
| [`SET/BADNODE`](set--badnode.md) | Direct administration guard | Stop spots from this node being propagated |
| [`SET/BADSPOTTER`](set--badspotter.md) | Direct administration guard | Stop spots from this callsign being propagated |
| [`SET/BADWORD`](set--badword.md) | Direct administration guard | Stop things like this word being propagated |
| [`SET/BBS`](set--bbs.md) | Direct administration guard | Make the callsign a BBS |
| [`SET/BEEP`](set--beep.md) | No direct handler guard | Add a beep to DX and other messages on your terminal |
| [`SET/BELIEVE`](set--believe.md) | Direct administration guard | Add a believable node - used to filter nodes as being believable |
| [`SET/BUDDY`](set--buddy.md) | No direct handler guard | Add this call to my buddy list |
| [`SET/CCLUSTER`](set--ccluster.md) | Direct administration guard | Make the callsign an CC Cluster node |
| [`SET/CLX`](set--clx.md) | Direct administration guard | Make the callsign an CLX node |
| [`SET/DEBUG`](set--debug.md) | Direct administration guard | Add a debug level to the debug set |
| [`SET/DX`](set--dx.md) | Direct administration guard | Allow DX messages to come out on your terminal |
| [`SET/DXCQ`](set--dxcq.md) | Direct administration guard | Show CQ Zones on the end of DX announcements |
| [`SET/DXGRID`](set--dxgrid.md) | Direct administration guard | Allow QRA Grid Squares on the end of DX announcements |
| [`SET/DXITU`](set--dxitu.md) | Direct administration guard | Show ITU Zones on the end of DX announcements |
| [`SET/DXNET`](set--dxnet.md) | Direct administration guard | Make the callsign an DXNet node |
| [`SET/ECHO`](set--echo.md) | No direct handler guard | Make the cluster echo your input |
| [`SET/EMAIL`](set--email.md) | No direct handler guard | Set email address(es) and forward your personals |
| [`SET/EXTERNAL_IP`](set--external-ip.md) | Direct administration guard | my $new = find_external_ipaddr(); |
| [`SET/GTK`](set--gtk.md) | No direct handler guard | set the gtk flag |
| [`SET/HERE`](set--here.md) | Direct administration guard | Tell DXSpider that you are present at your terminal. |
| [`SET/HOMEBBS`](set--homebbs.md) | No direct handler guard | set the home mail bbs of the user remove leading and trailing spaces |
| [`SET/HOMENODE`](set--homenode.md) | No direct handler guard | Set your normal cluster callsign |
| [`SET/HOPS`](set--hops.md) | Direct administration guard | Set hop count |
| [`SET/ISOLATE`](set--isolate.md) | Direct administration guard | Isolate a node from the rest of the network |
| [`SET/LANGUAGE`](set--language.md) | No direct handler guard | Set the language you want to use |
| [`SET/LOCAL_NODE`](set--local-node.md) | No direct handler guard | Add node to the local_node group |
| [`SET/LOCATION`](set--location.md) | No direct handler guard | Set your latitude and longitude |
| [`SET/LOCKOUT`](set--lockout.md) | Direct administration guard | Stop a callsign connecting to the cluster |
| [`SET/LOGININFO`](set--logininfo.md) | No direct handler guard | Inform when a station logs in/out locally |
| [`SET/MAXCONNECT`](set--maxconnect.md) | Direct administration guard | Set max incoming connections for user/node |
| [`SET/NAME`](set--name.md) | No direct handler guard | Set your name |
| [`SET/NODE`](set--node.md) | Direct administration guard | Make the callsign an AK1A cluster |
| [`SET/OBSCOUNT`](set--obscount.md) | Direct administration guard | Set the 'pump-up' obscelence PING counter |
| [`SET/PAGE`](set--page.md) | No direct handler guard | Set the lines per page |
| [`SET/PASSPHRASE`](set--passphrase.md) | Direct administration guard | set a user's passphrase Syntax: set/passphrase <callsign> <password> |
| [`SET/PASSWORD`](set--password.md) | Direct administration guard | Change your own password interactively, or—at SYSOP privilege—set another user's password. |
| [`SET/PINGINTERVAL`](set--pinginterval.md) | Direct administration guard | Set ping time to neighbouring nodes |
| [`SET/PRIVILEGE`](set--privilege.md) | Direct administration guard | Set privilege level on a call |
| [`SET/PROMPT`](set--prompt.md) | No direct handler guard | Set your prompt to <string> |
| [`SET/QRA`](set--qra.md) | No direct handler guard | Set your QRA Grid locator |
| [`SET/QTH`](set--qth.md) | No direct handler guard | Set your QTH |
| [`SET/RBN`](set--rbn.md) | Direct administration guard | Mark this call as an RBN node |
| [`SET/REGISTER`](set--register.md) | Direct administration guard | Mark a user as registered |
| [`SET/ROUTEPC19`](set--routepc19.md) | Direct administration guard | set the want to send PC19 route flag |
| [`SET/SEEME`](set--seeme.md) | No direct handler guard | set the ve7cc output flag |
| [`SET/SEEMEE`](set--seemee.md) | No direct handler guard | set the RBN seeme flag |
| [`SET/SENDPC16`](set--sendpc16.md) | Direct administration guard | set the send PC16 flag |
| [`SET/SEND_DBG`](set--send-dbg.md) | Direct administration guard | send debug information to this connection |
| [`SET/SPIDER`](set--spider.md) | Direct administration guard | Make the callsign an DXSpider node |
| [`SET/STARTUP`](set--startup.md) | Direct administration guard | Create a user startup script |
| [`SET/SYS_LOCATION`](set--sys-location.md) | Direct administration guard | Set your cluster latitude and longitude |
| [`SET/SYS_QRA`](set--sys-qra.md) | Direct administration guard | Set your cluster QRA Grid locator |
| [`SET/TALK`](set--talk.md) | Direct administration guard | Allow TALK messages to come out on your terminal |
| [`SET/USDB`](set--usdb.md) | Direct administration guard | add/update a US DB callsign |
| [`SET/USER`](set--user.md) | Direct administration guard | Make the callsign a normal user |
| [`SET/USERVAR`](set--uservar.md) | Direct administration guard | set any variable in the User file This is a hack - use the UTMOST CAUTION!!!!!!!! set it (dates and silly things like that can come later) |
| [`SET/USSTATE`](set--usstate.md) | Direct administration guard | Allow US State info on the end of DX announcements |
| [`SET/VAR`](set--var.md) | Direct administration guard | set any variable Rape me! |
| [`SET/VE7CC`](set--ve7cc.md) | No direct handler guard | set the ve7cc output flag |
| [`SET/WANTPC16`](set--wantpc16.md) | Direct administration guard | set the want PC16 flag |
| [`SET/WANTPC9X`](set--wantpc9x.md) | Direct administration guard | set the wantPC9x flag |
| [`SET/WANTRBN`](set--wantrbn.md) | Direct administration guard | Choose which curated RBN/Skimmer categories are delivered to the user. |
| [`SET/WCY`](set--wcy.md) | Direct administration guard | Allow WCY messages to come out on your terminal |
| [`SET/WIDTH`](set--width.md) | No direct handler guard | Set terminal width for the live session and stored user profile. |
| [`SET/WWV`](set--wwv.md) | Direct administration guard | Allow WWV messages to come out on your terminal |
| [`SET/WX`](set--wx.md) | Direct administration guard | Allow WX messages to come out on your terminal |
| [`SHOW/425`](show--425.md) | No direct handler guard | Query the 425 Database server for a callsign from an idea by Leo,IZ5FSA and 425DxNews Group |
| [`SHOW/ANNOUNCE`](show--announce.md) | Direct administration guard | Show log of announces |
| [`SHOW/BADDX`](show--baddx.md) | Direct administration guard | Show all the bad dx calls in the system |
| [`SHOW/BADIP`](show--badip.md) | Direct administration guard | show (or find) list of bad dx nodes are we permitted? $DB::single = 1; |
| [`SHOW/BADNODE`](show--badnode.md) | Direct administration guard | Show all the bad nodes in the system |
| [`SHOW/BADSPOTTER`](show--badspotter.md) | Direct administration guard | Show all the bad spotters in the system |
| [`SHOW/BADWORD`](show--badword.md) | Direct administration guard | Show all the bad words in the system |
| [`SHOW/BANDS`](show--bands.md) | No direct handler guard | Show the list of bands and regions |
| [`SHOW/BUDDY`](show--buddy.md) | No direct handler guard | Show your list of buddies |
| [`SHOW/CHAT`](show--chat.md) | Direct administration guard | Show any chat or conferencing |
| [`SHOW/CLUSTER`](show--cluster.md) | No direct handler guard | show some statistics |
| [`SHOW/CMD_CACHE`](show--cmd-cache.md) | Direct administration guard | Show the real source path of commands |
| [`SHOW/CONFIGURATION`](show--configuration.md) | No direct handler guard | Show all the nodes and users visible |
| [`SHOW/CONNECT`](show--connect.md) | Direct administration guard | Show all the active connections |
| [`SHOW/CONTEST`](show--contest.md) | No direct handler guard | Show all the contests for a month |
| [`SHOW/DATA_STATS`](show--data-stats.md) | No direct handler guard | show the users on this cluster from the routing tables |
| [`SHOW/DATE`](show--date.md) | No direct handler guard | Show the local time |
| [`SHOW/DB0SDX`](show--db0sdx.md) | No direct handler guard | Show QSL infomation from DB0SDX database |
| [`SHOW/DEBUG`](show--debug.md) | Direct administration guard | Show what levels of debug information you are logging |
| [`SHOW/DEBUG_RING`](show--debug-ring.md) | No direct handler guard | Log the current values of the DXDebug dbgring butter |
| [`SHOW/DUP_ANN`](show--dup-ann.md) | No direct handler guard | show a list of all the outstanding announce dups for debugging really |
| [`SHOW/DUP_EPH`](show--dup-eph.md) | No direct handler guard | show a list of all the outstanding announce dups for debugging really |
| [`SHOW/DUP_SPOTS`](show--dup-spots.md) | No direct handler guard | show a list of all the outstanding spot dups for debugging really |
| [`SHOW/DUP_WCY`](show--dup-wcy.md) | No direct handler guard | show a list of all the outstanding wcy dups for debugging really |
| [`SHOW/DUP_WWV`](show--dup-wwv.md) | No direct handler guard | show a list of all the outstanding wwv dups for debugging really |
| [`SHOW/DX`](show--dx.md) | No direct handler guard | Search the spot database by band, frequency, callsign, age, spotter, country, zone, state, origin, IP address and other selectors. |
| [`SHOW/DXQSL`](show--dxqsl.md) | No direct handler guard | Show any QSL info gathered from spots |
| [`SHOW/DXSTATS`](show--dxstats.md) | No direct handler guard | Show the DX Statistics |
| [`SHOW/EXTERNAL_IP`](show--external-ip.md) | Direct administration guard | Source-present command; review implementation evidence. |
| [`SHOW/FILES`](show--files.md) | No direct handler guard | List the contents of a filearea |
| [`SHOW/FILTER`](show--filter.md) | No direct handler guard | Show the contents of all the filters you have set |
| [`SHOW/GRAYLINE`](show--grayline.md) | No direct handler guard | Show Civil dawn/dusk times |
| [`SHOW/GROUPS`](show--groups.md) | No direct handler guard | show recently used groups by Tommy SM3OSM |
| [`SHOW/HEADING`](show--heading.md) | No direct handler guard | show the heading and distance for each callsign or prefix entered AK1A-compatible output Iain Philipps, G0RDI 16-Dec-1998 prefixes ---> |
| [`SHOW/HFSTATS`](show--hfstats.md) | No direct handler guard | Show the HF DX Statistics |
| [`SHOW/HFTABLE`](show--hftable.md) | No direct handler guard | Show the HF DX Spotter Table |
| [`SHOW/HOPS`](show--hops.md) | No direct handler guard | Show the hop counts for a node |
| [`SHOW/IK3QAR`](show--ik3qar.md) | No direct handler guard | Obtain QSL info from IK3QAR database |
| [`SHOW/ISOLATE`](show--isolate.md) | No direct handler guard | Show list of ISOLATED nodes |
| [`SHOW/LOCKOUT`](show--lockout.md) | No direct handler guard | Show the list of locked out or excluded callsigns |
| [`SHOW/LOG`](show--log.md) | Direct administration guard | Show excerpts from the system log |
| [`SHOW/MOON`](show--moon.md) | No direct handler guard | Show Moon rise and set times |
| [`SHOW/MOTD`](show--motd.md) | No direct handler guard | Show your MOTD (the Message of the Day) |
| [`SHOW/MSG_STATUS`](show--msg-status.md) | Direct administration guard | show msgs system status |
| [`SHOW/MUF`](show--muf.md) | No direct handler guard | Show the likely propagation to a prefix |
| [`SHOW/NEWCONFIGURATION`](show--newconfiguration.md) | No direct handler guard | Show the cluster map |
| [`SHOW/NODE`](show--node.md) | No direct handler guard | Show the type and version number of nodes |
| [`SHOW/PREFIX`](show--prefix.md) | No direct handler guard | Interrogate the prefix database |
| [`SHOW/PROGRAM`](show--program.md) | Direct administration guard | Show the locations of all the included program modules |
| [`SHOW/QRA`](show--qra.md) | No direct handler guard | Show distance between QRA Grid locators |
| [`SHOW/QRZ`](show--qrz.md) | No direct handler guard | Show any callbook details on a callsign |
| [`SHOW/RBN`](show--rbn.md) | No direct handler guard | Show which connected users want RBN spots |
| [`SHOW/RCMD`](show--rcmd.md) | Direct administration guard | Show log of rcmds |
| [`SHOW/REGISTERED`](show--registered.md) | No direct handler guard | Show the registered users |
| [`SHOW/ROUTE`](show--route.md) | No direct handler guard | Show the route to the callsign |
| [`SHOW/SATELLITE`](show--satellite.md) | No direct handler guard | Show tracking data |
| [`SHOW/SEEME`](show--seeme.md) | No direct handler guard | show/registered show all registered users dbg("set/register line: $line"); |
| [`SHOW/SPOTSTATS`](show--spotstats.md) | No direct handler guard | Show the current Spot statistics |
| [`SHOW/STARTUP`](show--startup.md) | Direct administration guard | View a user startup script |
| [`SHOW/STATION`](show--station.md) | Direct administration guard | Show list of users in the system |
| [`SHOW/SUN`](show--sun.md) | No direct handler guard | Show sun rise and set times |
| [`SHOW/TALK`](show--talk.md) | Direct administration guard | print out the general log file for talks only print "f: $f list: ", join(',', @list), "\n"; ($who) = $f =~ /^(\w+)/o; |
| [`SHOW/TIME`](show--time.md) | No direct handler guard | Show the local time |
| [`SHOW/USDB`](show--usdb.md) | No direct handler guard | Show information held on the FCC Call database |
| [`SHOW/USERS`](show--users.md) | No direct handler guard | show the users on this cluster from the routing tables |
| [`SHOW/VAR`](show--var.md) | Direct administration guard | show any variable Rape me! print "\$f = $f\n"; |
| [`SHOW/VERSION`](show--version.md) | No direct handler guard | show the version number of the software + copyright info $DB::single=1; |
| [`SHOW/VHFSTATS`](show--vhfstats.md) | No direct handler guard | Show the VHF DX Statistics |
| [`SHOW/VHFTABLE`](show--vhftable.md) | No direct handler guard | Show the VHF DX Spotter Table |
| [`SHOW/WCY`](show--wcy.md) | No direct handler guard | Show last 10 WCY broadcasts |
| [`SHOW/WM7D`](show--wm7d.md) | No direct handler guard | Show callbook details on a US callsigns |
| [`SHOW/WWV`](show--wwv.md) | No direct handler guard | Show last 10 WWV broadcasts |
| [`SHOW/WX`](show--wx.md) | Direct administration guard | show wx data this appears to be a reasonable thing for users to do (thank you JE1SGH) return (1, $self->msg('e5')) if $self->priv < 9; |
| [`SHU`](shu.md) | No direct handler guard | Command to force people to type at least 'shut' to shutdown |
| [`SHUTDOWN`](shutdown.md) | No direct handler guard | Shutdown the cluster |
| [`SPOOF`](spoof.md) | Direct administration guard | Do a command as though you are another user |
| [`STAT/CHANNEL`](stat--channel.md) | Direct administration guard | Show the status of a channel on the cluster |
| [`STAT/DB`](stat--db.md) | Direct administration guard | Show the status of a database |
| [`STAT/MSG`](stat--msg.md) | Direct administration guard | Show the status of the message system |
| [`STAT/NODECONFIG`](stat--nodeconfig.md) | No direct handler guard | show who all the nodes are connected to |
| [`STAT/PC19LIST`](stat--pc19list.md) | No direct handler guard | list out the PC19s that are outstanding (for which PC16s have not been seen) |
| [`STAT/ROUTE`](stat--route.md) | No direct handler guard | show a Route thingy A general purpose Route get thingy, use stat/route_user or _node if you want a list of all that particular type of thingy otherwise this |
| [`STAT/ROUTE_NODE`](stat--route-node.md) | No direct handler guard | Show the data in a Route::Node object |
| [`STAT/ROUTE_USER`](stat--route-user.md) | No direct handler guard | Show the data in a Route::User object |
| [`STAT/USER`](stat--user.md) | No direct handler guard | Show the full status of a user |
| [`STAT/USERCONFIG`](stat--userconfig.md) | No direct handler guard | show who all the users are connected to |
| [`SYSOP`](sysop.md) | No direct handler guard | Regain your privileges if you login remotely |
| [`TALK`](talk.md) | No direct handler guard | Send a private talk message or enter interactive talk mode. |
| [`TESTBADIP`](testbadip.md) | Direct administration guard | set list of bad dx nodes are we permitted? |
| [`TYPE`](type.md) | No direct handler guard | Look at the contents of a file in one of the fileareas |
| [`UNCATCHUP`](uncatchup.md) | Direct administration guard | Unmark a message as sent |
| [`UNSET/AGWENGINE`](unset--agwengine.md) | Direct administration guard | Disable the AGW Engine |
| [`UNSET/AGWMONITOR`](unset--agwmonitor.md) | Direct administration guard | Disable Monitoring on the AGW Engine |
| [`UNSET/ANNOUNCE`](unset--announce.md) | Direct administration guard | Stop announce messages coming out on your terminal |
| [`UNSET/ANNTALK`](unset--anntalk.md) | Direct administration guard | Stop talk like announce messages on your terminal |
| [`UNSET/BADDX`](unset--baddx.md) | Direct administration guard | Propagate a dx spot with this callsign again |
| [`UNSET/BADNODE`](unset--badnode.md) | Direct administration guard | Allow spots from this node again |
| [`UNSET/BADSPOTTER`](unset--badspotter.md) | Direct administration guard | Allow spots from this callsign again |
| [`UNSET/BADWORD`](unset--badword.md) | Direct administration guard | Propagate things like this word again |
| [`UNSET/BEEP`](unset--beep.md) | No direct handler guard | Stop beeps for DX and other messages on your terminal |
| [`UNSET/BELIEVE`](unset--believe.md) | Direct administration guard | Add a believable node - used to filter nodes as being believable |
| [`UNSET/BUDDY`](unset--buddy.md) | No direct handler guard | Remove this call from my buddy list |
| [`UNSET/DEBUG`](unset--debug.md) | Direct administration guard | Remove a debug level from the debug set |
| [`UNSET/DX`](unset--dx.md) | Direct administration guard | Stop DX messages coming out on your terminal |
| [`UNSET/DXCQ`](unset--dxcq.md) | Direct administration guard | Stop CQ Zones on the end of DX announcements |
| [`UNSET/DXGRID`](unset--dxgrid.md) | Direct administration guard | Stop QRA Grid Squares on the end of DX announcements |
| [`UNSET/DXITU`](unset--dxitu.md) | Direct administration guard | Stop ITU Zones on the end of DX announcements |
| [`UNSET/ECHO`](unset--echo.md) | No direct handler guard | Stop the cluster echoing your input |
| [`UNSET/EMAIL`](unset--email.md) | No direct handler guard | Stop personal msgs being forwarded by email |
| [`UNSET/GTK`](unset--gtk.md) | No direct handler guard | unset the gtk flag |
| [`UNSET/HERE`](unset--here.md) | Direct administration guard | Tell DXSpider that you are absent from your terminal. |
| [`UNSET/HOPS`](unset--hops.md) | Direct administration guard | Unset hop count |
| [`UNSET/ISOLATE`](unset--isolate.md) | Direct administration guard | Stop Isolation of a node from the rest of the network |
| [`UNSET/LOCAL_NODE`](unset--local-node.md) | No direct handler guard | Remove node from the local_node group |
| [`UNSET/LOCKOUT`](unset--lockout.md) | Direct administration guard | Allow a callsign to connect to the cluster |
| [`UNSET/LOGININFO`](unset--logininfo.md) | No direct handler guard | No longer inform when a station logs in/out locally |
| [`UNSET/PASSPHRASE`](unset--passphrase.md) | Direct administration guard | unset a user's passphrase Syntax: unset/passphrase <callsign> ... |
| [`UNSET/PASSWORD`](unset--password.md) | Direct administration guard | Delete (remove) a user's password |
| [`UNSET/PRIVILEGE`](unset--privilege.md) | No direct handler guard | Remove any privilege for this session |
| [`UNSET/PROMPT`](unset--prompt.md) | No direct handler guard | Set your prompt back to default |
| [`UNSET/REGISTER`](unset--register.md) | Direct administration guard | Mark a user as not registered |
| [`UNSET/ROUTEPC19`](unset--routepc19.md) | Direct administration guard | set the don't want to send PC19 route flag |
| [`UNSET/SEEME`](unset--seeme.md) | No direct handler guard | unset the RBN seeme flag |
| [`UNSET/SENDPC16`](unset--sendpc16.md) | Direct administration guard | unset the send PC16 flag |
| [`UNSET/SEND_DBG`](unset--send-dbg.md) | Direct administration guard | send debug information to this connection |
| [`UNSET/STARTUP`](unset--startup.md) | Direct administration guard | Remove a user startup script |
| [`UNSET/TALK`](unset--talk.md) | Direct administration guard | Stop TALK messages coming out on your terminal |
| [`UNSET/USSTATE`](unset--usstate.md) | Direct administration guard | Stop US State info on the end of DX announcements |
| [`UNSET/VE7CC`](unset--ve7cc.md) | No direct handler guard | set the ve7cc output flag |
| [`UNSET/WANTPC16`](unset--wantpc16.md) | Direct administration guard | unset the want PC16 flag |
| [`UNSET/WANTPC9X`](unset--wantpc9x.md) | Direct administration guard | unset the wantpc9x flag |
| [`UNSET/WANTRBN`](unset--wantrbn.md) | Direct administration guard | Stop all RBN/Skimmer spots |
| [`UNSET/WCY`](unset--wcy.md) | Direct administration guard | Stop WCY messages coming out on your terminal |
| [`UNSET/WWV`](unset--wwv.md) | Direct administration guard | Stop WWV messages coming out on your terminal |
| [`UNSET/WX`](unset--wx.md) | Direct administration guard | Stop WX messages coming out on your terminal |
| [`UPTIME`](uptime.md) | No direct handler guard | do a tradiotional "uptime" clone |
| [`WCY`](wcy.md) | No direct handler guard | WCY command This can only be used if the appropriate flag is enabled. I would STRONGLY recommend that, unless your callsign is DK8LV, you |
| [`WHO`](who.md) | No direct handler guard | Show who is physically connected |
| [`WWV`](wwv.md) | No direct handler guard | WWV command This can only be used if the appropriate flag is enabled. I would STRONGLY recommend that you |
| [`WX`](wx.md) | No direct handler guard | Send a weather message to local users |