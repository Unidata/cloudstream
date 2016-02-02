# CloudIDV Example

This example shows how to use `unidata/cloudstream` to create a kiosk-like IDV instance which is accessible via a web browser.

## Building the example

You will build this example as follows:

    $ docker build -t desktop -f Dockerfile.cloudidv .

## Running the example

You will run this example as follows:

    $ docker run -it -p 6080:6080 cloudidv

Once running, it will be accessed via a web browser.  Open the browser and enter the following address:

    [IP Address of the server where docker is running]:6080
