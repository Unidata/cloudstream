CloudStream Quickstart Guide
============================

This Quickstart guide provides the bare-minimum steps needed to get started with the Unidata **CloudStream** application-streaming framework.  This guide assumes that the user is familiar with **Git/GitHub**, **Docker** and **Linux** and wants to jump right in to using **CloudStream**.

> These examples assume the user is working in **OSX** or **Linux**.  Users in **Windows** should be able to use the same commands when using the *Docker Quickstart Terminal*.

Configure and Build your project
----------

1. Clone the **CloudStream** project from GitHub.

    ````.bash
    $ git clone http://github.com/Unidata/cloudstream
    ````

2. Copy the **CloudStream** `Dockerfile.template` into your project directory.
3. Rename `Dockerfile.template` to `Dockerfile.[project name]` or simply `Dockerfile`.
4. Edit `Dockerfile` and uncomment/set the following variables:

    * `MAINTAINER` - Your name and email address.
    * `APPLICATION_NAME` - The name of your docker project.
    * `APPLICATION_VERSION` - A string with your docker project version.  This can be numeric or a string.

5. If needed, uncomment the following line and define any additional packages to be installed using the `Ubuntu` package manager `apt-get`, e.g.:

    ````.bash
    # RUN apt-get install -y ubuntu-dev-tools libtool autoconf automake
    ````

6. Review the following sections in `Dockerfile`, editing each as is appropriate for your project:

    * `Advanced Docker Image customization`
    * `Custom Bash Init Script`
    * `Application README file`

7. Build your **Docker** project.

    ````.bash
    $ docker build -t [project name] -f Dockerfile .
    ````

8. Run your **Docker** project.

    ````.bash
    $ docker run -it -p 6080:6080 [project name]
    ````

9. Connect to your **Docker** project with a web browser, using the **IP** address of the server where your project is running and port `6080`, e.g.

    ````.bash
    http://192.168.99.100:6080
    ````

Additional Resources
--------------------

For a full list of options inherited from the **CloudStream** project, as well as advanced use cases, see the [CloudStream GitHub project page](https://github.com/Unidata/cloudstream#options).
