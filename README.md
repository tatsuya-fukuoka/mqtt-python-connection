# mqtt-python-connection
## 1. Git clone
```bash
git clone https://github.com/tatsuya-fukuoka/mqtt-python-connection.git
```
## 2. Building the Docker environment where mqtt works
```bash
docker build -t mqtt-test:v1.0.0 .
```
Dockerhub: https://hub.docker.com/repository/docker/tatsuya060504/mqtt-test/general
```bash
docker run -it --name=mqtt-test -v /home/tatsu/mqtt-test:/home -p 1883:1883 mqtt-test:v1.0.0 /bin/bash
```
