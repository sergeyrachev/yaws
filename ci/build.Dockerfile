from ubuntu:latest

arg DEBIAN_FRONTEND=noninteractive

run apt update
run apt install -y python3 make python3-pip

add . /tmp/yaws
workdir /tmp/yaws

run pip install -r requirements.txt
cmd python3 src/__main__.py -d /tmp/resources

