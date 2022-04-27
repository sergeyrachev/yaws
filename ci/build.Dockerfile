from alpine:latest as build-env
run apk install maven jq python make

add . /tmp/yaws
workdir /tmp/yaws

run make prereq

from build-env as build

add . /tmp/yaws
workdir /tmp/yaws

run make generate
run make service