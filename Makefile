ORG = unidata
IMAGE = cloudstream

all: ubuntu centos firefox desktop

ubuntu:
	docker build \
		-t $(ORG)/$(IMAGE):latest \
		-f Dockerfile.$(IMAGE) \
		--build-arg IMAGE=$(ORG)/$(IMAGE):latest \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg VCS_URL=`git config --get remote.origin.url` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		.

centos:
	docker build \
		-t $(ORG)/$(IMAGE):centos7 \
		-f Dockerfile.$(IMAGE).centos7 \
		--build-arg IMAGE=$(ORG)/$(IMAGE):centos7 \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg VCS_URL=`git config --get remote.origin.url` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
		.

firefox:
	docker build -t example/firefox:latest -f examples/Firefox/Dockerfile.firefox ./examples/Firefox/

desktop:
	docker build -t example/desktop:latest -f examples/Linux\ Desktop/Dockerfile.desktop examples/Linux\ Desktop/

.PHONY: ubuntu centos firefox desktop
