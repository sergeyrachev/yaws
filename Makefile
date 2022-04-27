prereq:
	mkdir -p tmp/bin/openapitools
	curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh > tmp/bin/openapitools/openapi-generator-cli
	chmod u+x tmp/bin/openapitools/openapi-generator-cli
	export PATH=$PATH:tmp/bin/openapitools

generate:
	openapi-generator-cli generate -g python-flask -i ./api/ -o src/gen
