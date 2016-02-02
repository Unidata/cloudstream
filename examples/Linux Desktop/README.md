# Linux Desktop Example

This example shows how to use `unidata/cloudstream` to generate a linux desktop environment which may be accessed via a web browser.  This example overrides the default screen geometry and replaces the default windows manager with the `LXDE` manager.

## Building the example

You will build this example as follows:

    $ docker build -t desktop -f Dockerfile.desktop .

## Running the example

You will run this example as follows:

    $ docker run -it -p 6080:6080 desktop

Once running, it will be accessed via a web browser.  Open the browser and enter the following address:

    [IP Address of the server where docker is running]:6080
