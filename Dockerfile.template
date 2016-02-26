#####
# Copyright Unidata 2016 All Rights Reserved
#
# This is a template docker configuration file (dockerfile) provided
# by Unidata in support of the Unidata CloudStream docker container.
# It is intended to illustrate how to easily build a project on top
# of Unidata's Application-Streaming technology stack.  To use this
# template, you will make a copy to your project and change those
# variables which need changing according to the following documentation.
# You would then use `Docker` to build your application streaming project
# as follows:
#
#   $ docker build -t [desired tag name] -f [Dockerfile.template name] .
#
# Once built, you would run it as follows:
#
#   $ docker run -it -p 6080:6080 [tag name]
#
# The application will then be available via a browser at the
# IP address of the machine from which it was invoked, on port 6080, e.g.:
#
#   http://[IP address]:6080
#
# For detailed usage guidelines, please see the project documentation at:
#
#  * https://github.com/Unidata/cloudstream
#
# Copyright Unidata 2015 - 2016
#####

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The following variables must be left as they are for the system to work
# properly, please do not change them. They are related to the underlying
# Ubuntu linux image upon which `unidata/cloudstream` is based.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Specify that this image inherits from the `unidata/cloudstream` image.
FROM unidata/cloudstream:1.1.0

# Tell Docker that we will be working as `root`.  Note that we can switch back to the
# default user specified by `${CUSER}` where need be. This value is inherited from
# `unidata/cloudstream`.
USER root

# Tell the Ubuntu package manager that we are running in a non-interactive mode.
ENV DEBIAN_FRONTEND noninteractive

# Update the package manager information and update any installed packages.
RUN apt-get update && apt-get -y upgrade

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# End non-user-configurable options.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

###############################################################################
# Begin user-configurable options.
###############################################################################

MAINTAINER FirstName LastName <email.address@domain.name>

####
# APPLICATION_NAME - Name of the application.
#
# This name is used for the documentation and for convenience.  It does
# not have to be congruent with the Docker image name.
#
# Syntax:
#    ENV APPLICATION_NAME [application name]
####

# ENV APPLICATION_NAME [application name]

####
# APPLICATION_VERSION - Version of the application.
#
# If you intend to build a versioned docker image, you can set
# this variable to the desired version.  When running your image,
# you may then pass it a non-empty VERSION variable and the version
# of both your application and the underlying unidata/cloudstream image will be printed.
#
# Syntax:
#   ENV APPLICATION_VERSION [desired version]
#
####

# ENV APPLICATION_VERSION [desired version]

####
# Package management
#
# unidata/cloudstream uses a Ubuntu-based environment.  Ubuntu linux uses the
# `apt-get` tool for managing packages from the official repositories.  If
# there are specific utilities or programs or libraries which must be installed
# for your package to work, install them here
#
# Example:
#    RUN apt-get install -y libcurl4-openssl-dev wget emacs git nano
####

# RUN apt-get install -y [space-delimited list of package names]

###
# NOTE: If you intend to build your own application from source, you will
# *at minimum* require the Ubuntu development tools as listed below.
# You will also need to install any other libraries or utilities your program
# will need to be compiled.
###

# RUN apt-get install -y ubuntu-dev-tools libtool autoconf automake

####
# Revert to non-root admin user.
#
# The unidata/cloudstream image provides a default non-root user (who has full
# sudo privileges.  This useraccount is captured in the ${CUSER} environmental
# variable. In order to preserve environmental variables, we need to
# switch over to this user now.
####

USER ${CUSER}

####
# Display Options
#
# CloudStream uses a VNC remote desktop server, coupled with the VNC/Websockets
# interface `noVNC`, to provide visualization via a web browser.  When a
# unidata/cloudstream-derived image runs, it uses the following default
# environmental variables to define the screen properties:
#
# - SIZEW: Width of display, default 1024
# - SIZEH: Height of display, default 768
# - CDEPTH: Color depth of display, default 24
#
# These defaults may be overridden here.  They may also be modified at runtime by
# passing these values as environmental variables at runtime.
####

# ENV SIZEW 1024
# ENV SIZEH 768
# ENV CDEPTH 24

####
# Custom Environmental Variables
#
# If your program or project depends on specific environmental variables,
# you can set default values below, similar to how `SIZEW`, `SIZEH` and
# `CDEPTH` are specified above.  These default values can be overridden
# at runtime.
#
# Syntax:
#    ENV [Variable Name] [Variable Value]
####

# ENV [Variable Name] [Variable Value]

####
# Advanced Docker Image customization
#
# The application streaming image can be highly customized using standard
# Docker functionality.  The following space is a good place to add any custom
# functionality which is not captured in this template.
#
# Examples of advanced usage include:
#
# * Compiling a program manually for use by the image.
# * Manipulating the filesystem and/or filesystem contents.
# * Checking the values of particular options and performing actions based on
#   their value.
# * Change the default window manager.
# * Override other default properties of the `unidata/cloudstream` image.
#
# See the files in the `examples/` directory for more examples of advanced
# usage.
####

####
# Application README file
#
# When the "HELP" environment variable is non-empty at runtime, any
# unidata/cloudstream derived image will print out the help file associated
# with unidata/cloudstream.  If there exists one of the following files,
# it will *also* be printed out:
#
# * README
# * README.txt
# * README.md
#
# This will allow you to add a help file or other documentation to your
# Docker image.
#
# You would view this helpfile at runtime as follows:
#
#    $ docker run -it -e HELP=YES [docker image name]
####

# COPY README ${HOME}/
# COPY README.txt ${HOME}/
# COPY README.md ${HOME}/

####
# Custom Bash Init Script
#
# By default, unidata/cloudidv and derivatives run a script when the image is
# invoked, `bootstrap.sh`.  `bootstrap.sh` is responsible for setting various
# underlying environmental variables and running the VNC server.  It also
# performs some actions depending on the environmental variables specified
# at runtime.
#
# If the file `start.sh` exists in the Docker image, `bootstrap.sh` will run
# this shell script once the environment has been configured.
#
# Example uses for `start.sh` include automatically running a specific program,
# checking out a project from a subversion or git repository, or anything else
# which can normally be achieved via a bash shell script.
#
# In order to work, `start.sh` must be copied to the default directory ${HOME},
# which maps to /home/${CUSER}/.
#
# If no `start.sh` is present, your application will automatically run a
# standard X11 desktop session using the `fluxbox` windows manager.
####

# COPY start.sh ${HOME}/

####
# End Advanced Docker Image customization
####

###############################################################################
# End user-configurable options.
###############################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Do not change anything below this line.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

####
# Append application name and version to the version file.
#
# This copies the application-specific name and version to the
# cloudstream version file.  When queried, this allows Docker
# to print out the version of your Docker image as well as the
# version of the underlying unidata/cloudstream image.
#
# It is safe to leave it alone.
####

RUN echo "${APPLICATION_NAME} Version: \"${APPLICATION_VERSION}\"\t$(date)" >> $VERSION_FILE

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# End File
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
