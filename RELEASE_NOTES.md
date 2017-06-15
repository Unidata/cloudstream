CloudStream Release Notes
========================

These are the release notes regarding CloudStream, the Unidata application-streaming technology stack.

See the project GitHub and DockerHub pages for more information:

* [https://github.com/Unidata/cloudstream](https://github.com/Unidata/cloudstream)
* [https://hub.docker.com/r/unidata/cloudstream/](https://hub.docker.com/r/unidata/cloudstream)

## 1.3.0 - June 15, 2017

* Enabled `noVNC`-provided shared clipboard.
* Taking advantage of nicer interface provided by `noVNC`.
* Updated to Ubuntu Xenial 16.04

## 1.2.0 - June 21, 2016

* Added a new option, `SHARED`, which allows for multiple connections to the same instance. **Off** by default.
* Added a new option, `SSLONLY`, which disables unencrypted http connections. **Off** by default.
* Added a `COPYRIGHT` environmental variable; when true, the CloudStream copyright file will be printed to standard output. Additionally, if the environmental variable `COPYRIGHT_FILE` has been set in a downstream image, the file referenced will be sent to standard output as well.
* `bootstrap.sh` no longer assumes a downstream image will use `README.[txt/md]`; instead, downstream projects must now specify a specific `README` file using the environmental variable `README_FILE`
* Added a quickstart guide, `QUICKSTART.md`, for users already familiar with Docker.

## 1.1.0 - February 17, 2016

* Added a `COPYRIGHT` file to the project.

## 1.0.0 - February 5, 2016

* Added documentation in the form of `README.md`.
* Added a template file, `Dockerfile.template`, that can be used as a basis for creating a CloudStream-based docker image.
* Added an initial set of basic examples to CloudStream in the `examples/` directory.
* Added Release Notes to CloudStream project.
