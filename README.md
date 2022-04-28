# yaws
Yet Another Web Service

Known trade-offs, limitations or growing-points:

- not strongly typed object members in API: timezone should be restricted by format specification; park type may be enum rather than string
- response paging depends on data size
- JWT/OAuth2 Auth
- Memory consumption: read csv to local memory may cause troubles
- CSV updates logic: trigger reload or use external indexed storage to get data from
- Remote CSV storage(like S3) may cause response delays
- JSON object schemas may be refactored to reflect customer domain model rather than storage one.
