#!/bin/bash

### BEGIN INIT INFO
# Provides:          RelayBot
# Required-Start:    $remote_fs $syslog $named $network $time
# Required-Stop:     $remote_fs $syslog $named $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: MuMaLab Relay Bot
# Description:       MuMaLab Relay Bot IRC<->Flowdock
### END INIT INFO

su - severin -c "/home/severin/mumalab/RelayBot/run.sh $1"
