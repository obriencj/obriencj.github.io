# Mess of a Makefile


PODMAN ?= $(shell which podman docker 2>/dev/null | head -n1)
PODMAN := $(PODMAN)

PORT ?= 8900


##@ Basic Targets

default:	help


help:	## Display this help  (default)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


html:  ## Regenerates static site
	podman run --rm --volume ./:/work \
          pelican-inelegant:latest \
	  -s developconf.py \
	  -e SITEURL="\"file://$(PWD)/output\""


develop:	## Launches web server that constantly regenerates site
	podman run --rm --volume ./:/work --network host \
          pelican-inelegant:latest -lr -p $(PORT) \
	  -s developconf.py \
	  -e SITEURL="\"https://localhost:$(PORT)\""


purge-cache:
	@git rm -rf content/photos/processed


photo-cache: clean purge-cache html
	@mkdir -p content/photos/processed
	@cp -ru output/photos/processed/* content/photos/processed/
	@git add content/photos/processed/**/*.*


##@ Cleanup

clean:	## Removes output dir
	@rm -rf ./output


.PHONY:	clean default help html devserver


# The end.
