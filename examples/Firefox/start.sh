#!/bin/bash
#
# This script is part of the CloudStream "FireFox" example.
# All that it does is launch firefox when the container starts.
# It then uses the xdotool utility to set the browser to "kiosk"
# mode.

set -x

firefox http://github.com/Unidata/cloudstream#cloudstream &
sleep 3
echo "Entering Kiosk Mode"
xdotool key F11
