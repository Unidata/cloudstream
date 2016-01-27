#!/bin/bash
##########
# This script is part of the unidata/cloudstream Docker image.
#
# It sets up a VNC session accessible via a webbrowser using noVNC and
# then executes start.sh, if available.
#
# Instructions for use are at https://github.com/Unidata/cloudstream.
#
# Copyright Unidata 2015 http://www.unidata.ucar.edu
##########

set -e

trap "echo TRAPed signal" HUP INT QUIT KILL TERM

###
# If HELP environmental variable is non-empty,
# cat the README file and exit.
#
# Start with checking for the CLOUDSTREAM readme, which is default.
# Then, assuming it will be named README[.md/.txt], cat other
# README file which might have been copied in. Finally, print
# out the version file.
#
###
if [ "x${HELP}" != "x" ]; then

    if [ -e "/home/${CUSER}/CLOUDSTREAM_README.md" ]; then
        cat "/home/${CUSER}/CLOUDSTREAM_README.md"
    fi
    echo ""

    if [ -e "/home/${CUSER}/README.md" ]; then
        cat "/home/${CUSER}/README.md"
    elif [ -e "/home/${CUSER}/README" ]; then
        cat "/home/${CUSER}/README"
    elif [ -e "/home/${CUSER}/README.txt" ]; then
        cat "/home/${CUSER}/README.txt"
    fi
    echo ""

    if [ "/home/${CUSER}/VERSION.md" ]; then
        cat "/home/${CUSER}/VERSION.md"
    fi

    exit
fi

###
# Print out the version file.
###
if [ "x${VERSION}" != "x" ]; then
    cat VERSION.md
    echo ""
    exit
fi


###
# Remove .x11 lock just in case there is one.
###
sudo rm -rf /tmp/.X1-lock

###
# Set up vnc to use a password if USEPASS is non-empty.
###

if [ "x${USEPASS}" == "x" ]; then
    cp /home/${CUSER}/.xinitrc.nopassword /home/${CUSER}/.xinitrc
else
    mkdir -p /home/${CUSER}/.vnc
    cp /home/${CUSER}/.xinitrc.password /home/${CUSER}/.xinitrc
    x11vnc -storepasswd "${USEPASS}" /home/${CUSER}/.vnc/passwd
fi

xinit -- /usr/bin/Xvfb :1 -screen 0 $SIZEW\x$SIZEH\x$CDEPTH &
sleep 5

export DISPLAY=localhost:1

##
# Invoke noVNC
##
cd /home/${CUSER}/noVNC/utils && openssl req -new -x509 -days 365 -nodes -out self.pem -keyout self.pem -batch
cd ~
/home/${CUSER}/noVNC/utils/launch.sh --vnc 127.0.0.1:5901 &

echo ""
echo ""
echo "================================"
cat VERSION.md
echo "================================"
echo ""
echo ""

if [ -f /home/${CUSER}/start.sh ]; then
    /home/${CUSER}/start.sh
fi

echo "Session Running. Press [Return] to exit."
read
