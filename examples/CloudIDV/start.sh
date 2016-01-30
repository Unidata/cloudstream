#!/bin/bash

###
# This script does several things:
#
# 1. Starts up the X session in a virtual framebuffer; password
#    use is dictated by value of USEPASS environmental variable.
# 2. Launches the IDV, using the VFB as the display.
#
# This is necessary to do here; if we put the xinit command
# in the Dockerfile, it would not run if we invoke this script
# from the 'docker run' command.  If we put the IDV in .xinitrc,
# then it would cause problems for those downstream images that
# don't want to automatically run the IDV.
#
# Therefore, we must run a command that starts xinit and then
# runs the IDV.  Other images will need to do something similar.
#
# This has the added benefit of killing the image when the IDV exits.
###

~/IDV/runIDV
