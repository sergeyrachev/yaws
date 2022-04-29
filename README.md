# yaws
Yet Another Web Service

How to run:

You need Docker install on host.
Then do `make image` to build Docker image;
And `YAWS_RESOURCE_DIR=$PWD/tmp make run` where YAWS_RESOURCE_DIR is a full path to CSV resource directory. 
The command mount resource directoy to container and launch it in interactive mode with terminal to handle Ctrl-C;
Swagger UI is available at http://172.17.0.2:8080/v1/ui/. IP address may differ as it depends on Docker network. 

Known trade-offs, limitations or growing-points:

- not strongly typed object members in API: timezone should be restricted by format specification; park type may be enum rather than string
- response paging depends on data size
- JWT/OAuth2 Auth
- Memory consumption: read csv to local memory may cause troubles
- CSV updates logic: trigger reload or use external indexed storage to get data from
- Remote CSV storage(like S3) may cause response delays
- JSON object schemas may be refactored to reflect customer domain model rather than storage one.
