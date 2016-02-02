CloudStream
===========

* [Travis-CI Dashboard](https://travis-ci.org/Unidata/cloudstream):  <IMG SRC="https://travis-ci.org/Unidata/cloudstream.svg?branch=master"/>

Table of contents
-----------------

* [Introduction](#introduction)
* [Requirements](#requirements)
* [CloudStream Runtime Options](#options)
    * [Information Options](#infooptions)
    * [Security Options](#secoptions)
    * [Display Options](#displayoptions)
* [Using CloudStream](#usage)
* [Using Cloudstream for custom software](#custom)
* [Other Resources](#refs)
* [Examples](#examples)

Introduction <A NAME="introduction"></A>
------------

***CloudStream*** is a Docker-based framework/container for Application Streaming. Application Streaming describes the process by which software is run on a remote server but is accessed on a device as though it were running locally.  CloudStream provides a Linux Desktop environment, which is then accessible through a standard web browser.  

CloudStream allows you to build a Docker image which contains specific software and may be run on a remote server, or a local system, and then access it using your web browser.  CloudStream images are sandboxed from each other, allowing for multiple CloudStream-enabled programs to run concurrently, without resource conflicts.

Requirements <A NAME="requirements"></A>
------------

CloudStream is a **Docker** image, which other images may be built on.  As a result, using CloudStream requires a local Docker installation.  Instructions for installing Docker may be found [here](https://docs.docker.com/).

Runtime Options <A NAME="options"></A>
---------------

**CloudStream** has several options built-in, enumerated below.  Additional custom options may be added for use in a CloudStream-based image.

CloudStream options are handled using environmental variables.  The syntax for this is described below.



#### View the unidata/cloudstream version information:

    $ docker run -it -e VERSION=TRUE unidata/cloudidv
    CloudStream Version: "1.0.0 - development"	Thu Jan 28 21:23:27 UTC 2016

#### Run unidata/cloudstream with custom display geometry, password protected, accessible on port 6080:

    $ docker run -it -p 6080:6080 -e USEPASS=password1234 -e SIZEW=800 -e SIZEH=600 -CDEPTH=16 unidata/cloudidv

### Information Options <A NAME="infooptions"></A>

Option | Note
-------|------
HELP   | Displays the CloudStream help file, plus any custom `README`, `README.txt` or `README.md` file copied over by a dependent image.
VERSION | Displays the CloudStream version, plus any custom version specified by a dependent image.  See `Dockerfile.template` for the syntax used to specify this.

### Security Options <A NAME="secoptions"></A>
Option | Note
-------|-----
USEPASS | Specifies a password to be used for the session.  `Default: no password`.

### Display Options <A NAME="displayoptions"></A>

Option | Note
-------|-----
SIZEW | The width of the display provided by CloudStream. `Default: 1024`
SIZEH | The height of the display provided by CloudStream. `Default: 768`
CDEPTH | The color depth of the display provided by CloudStream. `Default: 24`

### Docker-specific Options

> You will notice in all of our examples, we consistently pass the `-it` option to Docker. This tells Docker to run as an `interactive shell`, and is required for `unidata/cloudstream` to work properly.

In addition to the CloudStream options outlined above, you will need to expose port `6080` using the Docker flags `-p` or `-P`.  The `-p` option allows you to specify a specific port mapping, e.g. `-p 6081:6080` would result in a running docker image accessible on port `6081`.  The `-P` option specifies a dynamic port mapping, where Docker will find an available port.  You would then need to use `docker ps` to determine what port was selected.  This would work as follows:

    $ docker run -it -P  unidata/cloudstream
    $ docker ps
    CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                     NAMES
    47de1934777f        unidata/cloudstream   "/bin/sh -c /home/${C"   52 seconds ago      Up 51 seconds       0.0.0.0:32768->6080/tcp   big_pare

In this example, we see that we would connect to the `unidata/cloudstream`-based image by opening a web browser and going to `[Server IP Address]:32768`.


Usage <A NAME="usage"></A>
-----


Using CloudStream for custom software <A NAME="custom"></A>
-------------------------------------


Other Resources <A NAME="refs">
---------------

For more information on Docker syntax and using CloudStream as a basis for other application-streaming applications, see the following resources:

* Unidata CloudIDV:  [https://github.com/Unidata/cloudidv](https://github.com/Unidata/cloudidv)
* Dockerfile Syntax: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder)

Examples <A NAME="examples"></A>
--------
