# Commands with a direct administration guard

This list is generated from the current command handlers. Classification reflects direct guards visible in each handler; delegated authorization is called out on the command page.

| Command | Guide | Purpose |
|---|---|---|
| [`AGWRESTART`](../../reference/commands/agwrestart.md) | Direct administration guard | restart an agw connection |
| [`ANNOUNCE`](../../reference/commands/announce.md) | Direct administration guard | Send local, cluster-wide or SYSOP-only announcements. |
| [`CATCHUP`](../../reference/commands/catchup.md) | Direct administration guard | Mark a message as sent |
| [`CLEAR/CMD_CACHE`](../../reference/commands/clear--cmd-cache.md) | Direct administration guard | reset/reload the short name command cache you may need to do this if you remove files or the system gets confused about where it should be loading its cmd files |
| [`CLEAR/DUPEFILE`](../../reference/commands/clear--dupefile.md) | Direct administration guard | Clear out the dupefile completely |
| [`CONNECT`](../../reference/commands/connect.md) | Direct administration guard | Start a connection to another DX Cluster |
| [`CREATE/USER`](../../reference/commands/create--user.md) | Direct administration guard | Create this user from the User Database |
| [`DBCREATE`](../../reference/commands/dbcreate.md) | Direct administration guard | Create a database entry |
| [`DBEXPORT`](../../reference/commands/dbexport.md) | Direct administration guard | Export an AK1A data to a file |
| [`DBIMPORT`](../../reference/commands/dbimport.md) | Direct administration guard | Import AK1A data into a database |
| [`DBREMOVE`](../../reference/commands/dbremove.md) | Direct administration guard | Delete a database |
| [`DEBUG`](../../reference/commands/debug.md) | Direct administration guard | Set the cluster program into debug mode |
| [`DELETE/USDB`](../../reference/commands/delete--usdb.md) | Direct administration guard | Delete this user from the US State Database |
| [`DELETE/USER`](../../reference/commands/delete--user.md) | Direct administration guard | Delete this user from the User Database |
| [`DEMONSTRATE`](../../reference/commands/demonstrate.md) | Direct administration guard | Demonstrate a command to another user |
| [`DIRECTORY`](../../reference/commands/directory.md) | Direct administration guard | Browse DXSpider messages by ownership, age, sender, recipient, subject or message-number range. |
| [`DISCONNECT`](../../reference/commands/disconnect.md) | Direct administration guard | Disconnect user(s) or node(s) |
| [`DO`](../../reference/commands/do.md) | Direct administration guard | do anything Rape me! |
| [`DOWNLOAD`](../../reference/commands/download.md) | Direct administration guard | Download a file into local_data |
| [`DXQSL_EXPORT`](../../reference/commands/dxqsl-export.md) | Direct administration guard | Export SH/DXSQL information to a file |
| [`DXQSL_IMPORT`](../../reference/commands/dxqsl-import.md) | Direct administration guard | Import SH/DXSQL information from a file |
| [`EXPORT`](../../reference/commands/export.md) | Direct administration guard | Export a message to a file |
| [`FORWARD/OPERNAME`](../../reference/commands/forward--opername.md) | Direct administration guard | Cause node to send PC41 info frames Mods by Dirk Koopman G1TLH 12Dec98 |
| [`GET/KEPS`](../../reference/commands/get--keps.md) | Direct administration guard | Obtain the latest AMSAT Keplarian Elements from the web |
| [`INIT`](../../reference/commands/init.md) | Direct administration guard | Re-initialise a link to an AK1A compatible node |
| [`KILL`](../../reference/commands/kill.md) | Direct administration guard | Delete a message from the local system |
| [`LOAD/ALIASES`](../../reference/commands/load--aliases.md) | Direct administration guard | Reload the command alias table |
| [`LOAD/BADIP`](../../reference/commands/load--badip.md) | Direct administration guard | Reload the bad IP address table |
| [`LOAD/BADMSG`](../../reference/commands/load--badmsg.md) | Direct administration guard | Reload the bad msg table |
| [`LOAD/BADWORDS`](../../reference/commands/load--badwords.md) | Direct administration guard | Reload the bad words table |
| [`LOAD/BANDS`](../../reference/commands/load--bands.md) | Direct administration guard | Reload the band limits table |
| [`LOAD/CMD_CACHE`](../../reference/commands/load--cmd-cache.md) | Direct administration guard | Reload the automatic command cache |
| [`LOAD/DB`](../../reference/commands/load--db.md) | Direct administration guard | Reload the DB list |
| [`LOAD/DXQSL`](../../reference/commands/load--dxqsl.md) | Direct administration guard | load the QSL file after changing it |
| [`LOAD/FORWARD`](../../reference/commands/load--forward.md) | Direct administration guard | Reload the msg forwarding routing table |
| [`LOAD/HOPS`](../../reference/commands/load--hops.md) | Direct administration guard | load the node hop count table after changing it |
| [`LOAD/KEPS`](../../reference/commands/load--keps.md) | Direct administration guard | Load new keps data |
| [`LOAD/MESSAGES`](../../reference/commands/load--messages.md) | Direct administration guard | Reload the system messages file |
| [`LOAD/PREFIXES`](../../reference/commands/load--prefixes.md) | Direct administration guard | Reload the prefix table |
| [`LOAD/QSL`](../../reference/commands/load--qsl.md) | Direct administration guard | load the QSL file after changing it |
| [`LOAD/SWOP`](../../reference/commands/load--swop.md) | Direct administration guard | reload the swop file |
| [`LOAD/USDB`](../../reference/commands/load--usdb.md) | Direct administration guard | reload the usdb file Be warned, if this is the full database the size of your image will increase by at least 20Mb and all activity will stop for several |
| [`MERGE`](../../reference/commands/merge.md) | Direct administration guard | Ask for the latest spots and WWV |
| [`MSG`](../../reference/commands/msg.md) | Direct administration guard | Alter various message parameters |
| [`NOSPAWN`](../../reference/commands/nospawn.md) | Direct administration guard | pretend that you are another user, useful for reseting those silly things that people insist on getting wrong like set/homenode et al |
| [`PC`](../../reference/commands/pc.md) | Direct administration guard | Send text (eg PC Protocol) to <call> |
| [`RCMD`](../../reference/commands/rcmd.md) | Direct administration guard | Send a command to another DX Cluster |
| [`READ`](../../reference/commands/read.md) | Direct administration guard | Read the next unread personal message addressed to you |
| [`REGISTER/ACCEPT`](../../reference/commands/register--accept.md) | Direct administration guard | register/accept.pl - Accept a DXSpider registration request SYSOP only. Usage: |
| [`REGISTER/REJECT`](../../reference/commands/register--reject.md) | Direct administration guard | register/reject.pl - Reject a DXSpider registration request SYSOP only. Usage: |
| [`REGISTER/REMOVE`](../../reference/commands/register--remove.md) | Direct administration guard | register/remove.pl - Remove DXSpider registration for a callsign family SYSOP only. Usage: |
| [`REGISTER/SHOW`](../../reference/commands/register--show.md) | Direct administration guard | register/show.pl - Show DXSpider registration requests/history SYSOP only. Usage: |
| [`RINIT`](../../reference/commands/rinit.md) | Direct administration guard | reverse init a cluster connection |
| [`RUN`](../../reference/commands/run.md) | Direct administration guard | the run command run a script from the scripts directory |
| [`SAVE`](../../reference/commands/save.md) | Direct administration guard | Save command output to a file |
| [`SEND`](../../reference/commands/send.md) | Direct administration guard | Send a message to one or more callsigns |
| [`SET/AGWENGINE`](../../reference/commands/set--agwengine.md) | Direct administration guard | Enable the AGW Engine |
| [`SET/AGWMONITOR`](../../reference/commands/set--agwmonitor.md) | Direct administration guard | Enable Monitoring on the AGW Engine |
| [`SET/ANNOUNCE`](../../reference/commands/set--announce.md) | Direct administration guard | Allow announce messages to come out on your terminal |
| [`SET/ANNTALK`](../../reference/commands/set--anntalk.md) | Direct administration guard | Allow talk like announce messages on your terminal |
| [`SET/ARCLUSTER`](../../reference/commands/set--arcluster.md) | Direct administration guard | Make the callsign an AR-Cluster node |
| [`SET/BADDX`](../../reference/commands/set--baddx.md) | Direct administration guard | Stop callsigns in a dx spot being propagated |
| [`SET/BADIP`](../../reference/commands/set--badip.md) | Direct administration guard | Stop logins and spots with this IP address |
| [`SET/BADNODE`](../../reference/commands/set--badnode.md) | Direct administration guard | Stop spots from this node being propagated |
| [`SET/BADSPOTTER`](../../reference/commands/set--badspotter.md) | Direct administration guard | Stop spots from this callsign being propagated |
| [`SET/BADWORD`](../../reference/commands/set--badword.md) | Direct administration guard | Stop things like this word being propagated |
| [`SET/BBS`](../../reference/commands/set--bbs.md) | Direct administration guard | Make the callsign a BBS |
| [`SET/BELIEVE`](../../reference/commands/set--believe.md) | Direct administration guard | Add a believable node - used to filter nodes as being believable |
| [`SET/CCLUSTER`](../../reference/commands/set--ccluster.md) | Direct administration guard | Make the callsign an CC Cluster node |
| [`SET/CLX`](../../reference/commands/set--clx.md) | Direct administration guard | Make the callsign an CLX node |
| [`SET/DEBUG`](../../reference/commands/set--debug.md) | Direct administration guard | Add a debug level to the debug set |
| [`SET/DX`](../../reference/commands/set--dx.md) | Direct administration guard | Allow DX messages to come out on your terminal |
| [`SET/DXCQ`](../../reference/commands/set--dxcq.md) | Direct administration guard | Show CQ Zones on the end of DX announcements |
| [`SET/DXGRID`](../../reference/commands/set--dxgrid.md) | Direct administration guard | Allow QRA Grid Squares on the end of DX announcements |
| [`SET/DXITU`](../../reference/commands/set--dxitu.md) | Direct administration guard | Show ITU Zones on the end of DX announcements |
| [`SET/DXNET`](../../reference/commands/set--dxnet.md) | Direct administration guard | Make the callsign an DXNet node |
| [`SET/EXTERNAL_IP`](../../reference/commands/set--external-ip.md) | Direct administration guard | my $new = find_external_ipaddr(); |
| [`SET/HERE`](../../reference/commands/set--here.md) | Direct administration guard | Tell DXSpider that you are present at your terminal. |
| [`SET/HOPS`](../../reference/commands/set--hops.md) | Direct administration guard | Set hop count |
| [`SET/ISOLATE`](../../reference/commands/set--isolate.md) | Direct administration guard | Isolate a node from the rest of the network |
| [`SET/LOCKOUT`](../../reference/commands/set--lockout.md) | Direct administration guard | Stop a callsign connecting to the cluster |
| [`SET/MAXCONNECT`](../../reference/commands/set--maxconnect.md) | Direct administration guard | Set max incoming connections for user/node |
| [`SET/NODE`](../../reference/commands/set--node.md) | Direct administration guard | Make the callsign an AK1A cluster |
| [`SET/OBSCOUNT`](../../reference/commands/set--obscount.md) | Direct administration guard | Set the 'pump-up' obscelence PING counter |
| [`SET/PASSPHRASE`](../../reference/commands/set--passphrase.md) | Direct administration guard | set a user's passphrase Syntax: set/passphrase <callsign> <password> |
| [`SET/PASSWORD`](../../reference/commands/set--password.md) | Direct administration guard | Change your own password interactively, or—at SYSOP privilege—set another user's password. |
| [`SET/PINGINTERVAL`](../../reference/commands/set--pinginterval.md) | Direct administration guard | Set ping time to neighbouring nodes |
| [`SET/PRIVILEGE`](../../reference/commands/set--privilege.md) | Direct administration guard | Set privilege level on a call |
| [`SET/RBN`](../../reference/commands/set--rbn.md) | Direct administration guard | Mark this call as an RBN node |
| [`SET/REGISTER`](../../reference/commands/set--register.md) | Direct administration guard | Mark a user as registered |
| [`SET/ROUTEPC19`](../../reference/commands/set--routepc19.md) | Direct administration guard | set the want to send PC19 route flag |
| [`SET/SENDPC16`](../../reference/commands/set--sendpc16.md) | Direct administration guard | set the send PC16 flag |
| [`SET/SEND_DBG`](../../reference/commands/set--send-dbg.md) | Direct administration guard | send debug information to this connection |
| [`SET/SPIDER`](../../reference/commands/set--spider.md) | Direct administration guard | Make the callsign an DXSpider node |
| [`SET/STARTUP`](../../reference/commands/set--startup.md) | Direct administration guard | Create a user startup script |
| [`SET/SYS_LOCATION`](../../reference/commands/set--sys-location.md) | Direct administration guard | Set your cluster latitude and longitude |
| [`SET/SYS_QRA`](../../reference/commands/set--sys-qra.md) | Direct administration guard | Set your cluster QRA Grid locator |
| [`SET/TALK`](../../reference/commands/set--talk.md) | Direct administration guard | Allow TALK messages to come out on your terminal |
| [`SET/USDB`](../../reference/commands/set--usdb.md) | Direct administration guard | add/update a US DB callsign |
| [`SET/USER`](../../reference/commands/set--user.md) | Direct administration guard | Make the callsign a normal user |
| [`SET/USERVAR`](../../reference/commands/set--uservar.md) | Direct administration guard | set any variable in the User file This is a hack - use the UTMOST CAUTION!!!!!!!! set it (dates and silly things like that can come later) |
| [`SET/USSTATE`](../../reference/commands/set--usstate.md) | Direct administration guard | Allow US State info on the end of DX announcements |
| [`SET/VAR`](../../reference/commands/set--var.md) | Direct administration guard | set any variable Rape me! |
| [`SET/WANTPC16`](../../reference/commands/set--wantpc16.md) | Direct administration guard | set the want PC16 flag |
| [`SET/WANTPC9X`](../../reference/commands/set--wantpc9x.md) | Direct administration guard | set the wantPC9x flag |
| [`SET/WANTRBN`](../../reference/commands/set--wantrbn.md) | Direct administration guard | Choose which curated RBN/Skimmer categories are delivered to the user. |
| [`SET/WCY`](../../reference/commands/set--wcy.md) | Direct administration guard | Allow WCY messages to come out on your terminal |
| [`SET/WWV`](../../reference/commands/set--wwv.md) | Direct administration guard | Allow WWV messages to come out on your terminal |
| [`SET/WX`](../../reference/commands/set--wx.md) | Direct administration guard | Allow WX messages to come out on your terminal |
| [`SHOW/ANNOUNCE`](../../reference/commands/show--announce.md) | Direct administration guard | Show log of announces |
| [`SHOW/BADDX`](../../reference/commands/show--baddx.md) | Direct administration guard | Show all the bad dx calls in the system |
| [`SHOW/BADIP`](../../reference/commands/show--badip.md) | Direct administration guard | show (or find) list of bad dx nodes are we permitted? $DB::single = 1; |
| [`SHOW/BADNODE`](../../reference/commands/show--badnode.md) | Direct administration guard | Show all the bad nodes in the system |
| [`SHOW/BADSPOTTER`](../../reference/commands/show--badspotter.md) | Direct administration guard | Show all the bad spotters in the system |
| [`SHOW/BADWORD`](../../reference/commands/show--badword.md) | Direct administration guard | Show all the bad words in the system |
| [`SHOW/CHAT`](../../reference/commands/show--chat.md) | Direct administration guard | Show any chat or conferencing |
| [`SHOW/CMD_CACHE`](../../reference/commands/show--cmd-cache.md) | Direct administration guard | Show the real source path of commands |
| [`SHOW/CONNECT`](../../reference/commands/show--connect.md) | Direct administration guard | Show all the active connections |
| [`SHOW/DEBUG`](../../reference/commands/show--debug.md) | Direct administration guard | Show what levels of debug information you are logging |
| [`SHOW/EXTERNAL_IP`](../../reference/commands/show--external-ip.md) | Direct administration guard | Source-present command; review implementation evidence. |
| [`SHOW/LOG`](../../reference/commands/show--log.md) | Direct administration guard | Show excerpts from the system log |
| [`SHOW/MSG_STATUS`](../../reference/commands/show--msg-status.md) | Direct administration guard | show msgs system status |
| [`SHOW/PROGRAM`](../../reference/commands/show--program.md) | Direct administration guard | Show the locations of all the included program modules |
| [`SHOW/RCMD`](../../reference/commands/show--rcmd.md) | Direct administration guard | Show log of rcmds |
| [`SHOW/STARTUP`](../../reference/commands/show--startup.md) | Direct administration guard | View a user startup script |
| [`SHOW/STATION`](../../reference/commands/show--station.md) | Direct administration guard | Show list of users in the system |
| [`SHOW/TALK`](../../reference/commands/show--talk.md) | Direct administration guard | print out the general log file for talks only print "f: $f list: ", join(',', @list), "\n"; ($who) = $f =~ /^(\w+)/o; |
| [`SHOW/VAR`](../../reference/commands/show--var.md) | Direct administration guard | show any variable Rape me! print "\$f = $f\n"; |
| [`SHOW/WX`](../../reference/commands/show--wx.md) | Direct administration guard | show wx data this appears to be a reasonable thing for users to do (thank you JE1SGH) return (1, $self->msg('e5')) if $self->priv < 9; |
| [`SPOOF`](../../reference/commands/spoof.md) | Direct administration guard | Do a command as though you are another user |
| [`STAT/CHANNEL`](../../reference/commands/stat--channel.md) | Direct administration guard | Show the status of a channel on the cluster |
| [`STAT/DB`](../../reference/commands/stat--db.md) | Direct administration guard | Show the status of a database |
| [`STAT/MSG`](../../reference/commands/stat--msg.md) | Direct administration guard | Show the status of the message system |
| [`TESTBADIP`](../../reference/commands/testbadip.md) | Direct administration guard | set list of bad dx nodes are we permitted? |
| [`UNCATCHUP`](../../reference/commands/uncatchup.md) | Direct administration guard | Unmark a message as sent |
| [`UNSET/AGWENGINE`](../../reference/commands/unset--agwengine.md) | Direct administration guard | Disable the AGW Engine |
| [`UNSET/AGWMONITOR`](../../reference/commands/unset--agwmonitor.md) | Direct administration guard | Disable Monitoring on the AGW Engine |
| [`UNSET/ANNOUNCE`](../../reference/commands/unset--announce.md) | Direct administration guard | Stop announce messages coming out on your terminal |
| [`UNSET/ANNTALK`](../../reference/commands/unset--anntalk.md) | Direct administration guard | Stop talk like announce messages on your terminal |
| [`UNSET/BADDX`](../../reference/commands/unset--baddx.md) | Direct administration guard | Propagate a dx spot with this callsign again |
| [`UNSET/BADNODE`](../../reference/commands/unset--badnode.md) | Direct administration guard | Allow spots from this node again |
| [`UNSET/BADSPOTTER`](../../reference/commands/unset--badspotter.md) | Direct administration guard | Allow spots from this callsign again |
| [`UNSET/BADWORD`](../../reference/commands/unset--badword.md) | Direct administration guard | Propagate things like this word again |
| [`UNSET/BELIEVE`](../../reference/commands/unset--believe.md) | Direct administration guard | Add a believable node - used to filter nodes as being believable |
| [`UNSET/DEBUG`](../../reference/commands/unset--debug.md) | Direct administration guard | Remove a debug level from the debug set |
| [`UNSET/DX`](../../reference/commands/unset--dx.md) | Direct administration guard | Stop DX messages coming out on your terminal |
| [`UNSET/DXCQ`](../../reference/commands/unset--dxcq.md) | Direct administration guard | Stop CQ Zones on the end of DX announcements |
| [`UNSET/DXGRID`](../../reference/commands/unset--dxgrid.md) | Direct administration guard | Stop QRA Grid Squares on the end of DX announcements |
| [`UNSET/DXITU`](../../reference/commands/unset--dxitu.md) | Direct administration guard | Stop ITU Zones on the end of DX announcements |
| [`UNSET/HERE`](../../reference/commands/unset--here.md) | Direct administration guard | Tell DXSpider that you are absent from your terminal. |
| [`UNSET/HOPS`](../../reference/commands/unset--hops.md) | Direct administration guard | Unset hop count |
| [`UNSET/ISOLATE`](../../reference/commands/unset--isolate.md) | Direct administration guard | Stop Isolation of a node from the rest of the network |
| [`UNSET/LOCKOUT`](../../reference/commands/unset--lockout.md) | Direct administration guard | Allow a callsign to connect to the cluster |
| [`UNSET/PASSPHRASE`](../../reference/commands/unset--passphrase.md) | Direct administration guard | unset a user's passphrase Syntax: unset/passphrase <callsign> ... |
| [`UNSET/PASSWORD`](../../reference/commands/unset--password.md) | Direct administration guard | Delete (remove) a user's password |
| [`UNSET/REGISTER`](../../reference/commands/unset--register.md) | Direct administration guard | Mark a user as not registered |
| [`UNSET/ROUTEPC19`](../../reference/commands/unset--routepc19.md) | Direct administration guard | set the don't want to send PC19 route flag |
| [`UNSET/SENDPC16`](../../reference/commands/unset--sendpc16.md) | Direct administration guard | unset the send PC16 flag |
| [`UNSET/SEND_DBG`](../../reference/commands/unset--send-dbg.md) | Direct administration guard | send debug information to this connection |
| [`UNSET/STARTUP`](../../reference/commands/unset--startup.md) | Direct administration guard | Remove a user startup script |
| [`UNSET/TALK`](../../reference/commands/unset--talk.md) | Direct administration guard | Stop TALK messages coming out on your terminal |
| [`UNSET/USSTATE`](../../reference/commands/unset--usstate.md) | Direct administration guard | Stop US State info on the end of DX announcements |
| [`UNSET/WANTPC16`](../../reference/commands/unset--wantpc16.md) | Direct administration guard | unset the want PC16 flag |
| [`UNSET/WANTPC9X`](../../reference/commands/unset--wantpc9x.md) | Direct administration guard | unset the wantpc9x flag |
| [`UNSET/WANTRBN`](../../reference/commands/unset--wantrbn.md) | Direct administration guard | Stop all RBN/Skimmer spots |
| [`UNSET/WCY`](../../reference/commands/unset--wcy.md) | Direct administration guard | Stop WCY messages coming out on your terminal |
| [`UNSET/WWV`](../../reference/commands/unset--wwv.md) | Direct administration guard | Stop WWV messages coming out on your terminal |
| [`UNSET/WX`](../../reference/commands/unset--wx.md) | Direct administration guard | Stop WX messages coming out on your terminal |