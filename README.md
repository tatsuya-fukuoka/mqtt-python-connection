# mqtt-python-connection
Blog: https://chantastu.hatenablog.com/entry/2023/02/25/095248
## 1. Git clone
```bash
git clone https://github.com/tatsuya-fukuoka/mqtt-python-connection.git
```
## 2. Building the Docker environment where mqtt works
Dockerfile
```txt
FROM ubuntu:20.04
USER root

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt-get update
RUN apt-get -y install pip
RUN apt-get -y install libgl1-mesa-dev && apt-get -y install libglib2.0-0
RUN apt-get -y install mosquitto-clients && apt-get -y install mosquitto
RUN apt-get -y install systemctl

RUN pip install -U pip
RUN pip install paho-mqtt
```
build
```bash
docker build -t mqtt-test:v1.0.0 .
```
Dockerhub: https://hub.docker.com/repository/docker/tatsuya060504/mqtt-test/general
```bash
docker run -it --name=mqtt-test -v /home/tatsu/mqtt-test:/home -p 1883:1883 mqtt-test:v1.0.0 /bin/bash
```
## 3.JSON format
http://www.steves-internet-guide.com/send-json-data-mqtt-python/
