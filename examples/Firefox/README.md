# Firefox Example

This example shows how to use `unidata/cloudstream` to create a container which will run the "Firefox" web browser on launch.

## Building the example

You will build this example as follows:

    $ docker build -t desktop -f Dockerfile.firefox .

## Running the example

You will run this example as follows:

    $ docker run -it -p 6080:6080 firefox

Once running, it will be accessed via a web browser.  Open the browser and enter the following address:

    [IP Address of the server where docker is running]:6080
