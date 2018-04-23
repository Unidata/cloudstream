#####
#
# Used to generate the 'unidata/cloudstream:centos7' docker container.
# Visit us on the web at https://www.unidata.ucar.edu
#
# Copyright Unidata 2015 - 2018
#
#####

FROM centos:7
MAINTAINER Ward Fisher <wfisher@ucar.edu> Michael James <mjames@ucar.edu>
ENV CLOUDSTREAM_VERSION development

###
# Update base docker image.
###

RUN yum -y update yum

###
# Development tools (optional)
###

RUN yum -y groupinstall development

###
# CloudStream dependencies
### 

RUN yum -y install \
  epel-release \
  glx-utils \
  mesa-dri-drivers \
  nano \
  net-tools \
  openssl \
  pexpect \
  sudo \
  wget \
  which \
  xterm \
  xdg-utils \
  xorg-x11-xinit \
  xorg-x11-server-Xvfb

###
# Refresh yum cache for EPEL
###

RUN yum -y update

###
# EPEL dependencies
###

RUN yum -y install fluxbox x11vnc

###
# Set up a non-root user account.
###

ENV CUSER stream
ENV CUSERPWORD "password.1234"

RUN useradd -ms /bin/bash ${CUSER}
#RUN adduser ${CUSER} sudo
RUN usermod -a -G wheel ${CUSER}
# There is no need for the password to be known, so
# randomize it for now.
RUN echo "${CUSER}:${CUSERPWORD}${RANDOM} " | chpasswd
RUN echo "${CUSER} ALL=NOPASSWD: ALL" >> /etc/sudoers

###
# Switch to the non-root user,
# configure system and environment.
###

USER ${CUSER}
ENV HOME /home/${CUSER}
WORKDIR ${HOME}

RUN mkdir ~/.vnc

###
# Create a .xinitrc file.
# The environmental variable APORT = 5901 by default but can be
# overridden when invoking 'docker run', e.g. docker run -e APORT=4435
###

RUN echo '/usr/bin/x11vnc -display :1 $SHARESTRING -autoport $APORT -repeat -forever &' > ~/.xinitrc.nopassword
RUN echo '/usr/bin/x11vnc -usepw -display :1 $SHARESTRING -autoport $APORT -repeat -forever &' > ~/.xinitrc.password

RUN echo "/usr/bin/startfluxbox" >> ~/.xinitrc.nopassword
RUN echo "/usr/bin/startfluxbox" >> ~/.xinitrc.password

###
# Configure fluxbox
###

RUN mkdir ~/.fluxbox/
RUN bash -c 'echo "xterm &" >> ~/.fluxbox/startup'
RUN echo "/usr/bin/fluxbox -log ~/.fluxbox/log" >> ~/.fluxbox/startup

###
# Expose Websocket port for VNC server.
###

ENV APORT 5901
ENV WPORT 6080

EXPOSE ${WPORT}

RUN git clone git://github.com/kanaka/noVNC
RUN cp /home/${CUSER}/noVNC/vnc_lite.html /home/${CUSER}/noVNC/index.html
RUN cd /home/${CUSER}/noVNC/utils && git clone https://github.com/kanaka/websockify

USER root
RUN wget https://downloads.rclone.org/rclone-current-linux-amd64.rpm && rpm -ivh rclone-current-linux-amd64.rpm
USER ${CUSER}

###
# We can parameterize screen dimensions with the following variables.
# e.g.
#    docker run -p 6080:6080 -e SIZEH=800 -e SIZEW=640 -e CDEPTH=8 \
#                       -it [docker image] bootstrap.sh
###

ENV SIZEW 1024
ENV SIZEH 768
ENV CDEPTH 24

###
# Set up an option to allow for sharing.
###

ENV SHARESTRING --noshared

###
# Copy over files
###

COPY start.sh ${HOME}/
COPY bootstrap.sh ${HOME}/
COPY README.md ${HOME}/
COPY COPYRIGHT_CLOUDSTREAM.md ${HOME}/
COPY RELEASE_NOTES.md ${HOME}/
COPY QUICKSTART.md ${HOME}/

RUN mv README.md CLOUDSTREAM_README.md
ADD examples ${HOME}/examples

###
# Create version file
###

ENV VERSION_FILE VERSION.md
RUN echo "CloudStream Version: "$CLOUDSTREAM_VERSION" $(date)" > $VERSION_FILE

###
# Housekeeping
###

USER root
RUN chown -R ${CUSER}:${CUSER} ${HOME}
USER ${CUSER}

###
# Run the bootstrap.sh script.
# This will set up/run the VNC environment,
# and execute the start.sh file if present.
###

CMD /home/${CUSER}/bootstrap.sh

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG IMAGE
ARG VCS_REF
ARG VCS_URL
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name=$IMAGE \
      org.label-schema.description="An image based on centos 7 containing AWIPS CAVE and an X_Window_System" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.schema-version="1.0"
