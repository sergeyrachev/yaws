generate:
	mkdir -p gen
	touch gen/.keep

image:
	docker build -f ci/build.Dockerfile

service: generate
	python -m build

distribution: service
	python -m twine upload --repository testpypi dist/*