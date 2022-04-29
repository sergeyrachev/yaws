image:
	docker build -t yaws:latest -f ci/build.Dockerfile .

run:
	docker run --rm -ti -v$(YAWS_RESOURCE_DIR):/tmp/resources yaws:latest
