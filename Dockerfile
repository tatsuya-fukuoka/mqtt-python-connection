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
