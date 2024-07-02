#FROM python:3.11-slim
FROM ubuntu:22.04 AS builder-image
#
#RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
RUN apt-get update && apt-get install --no-install-recommends -y python3.11 python3.11-dev python3.11-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

#RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y update && apt-get -y install make

#RUN apt clean && apt update && apt upgrade -y && apt install -y -f
#RUN apt install -y build-essential wget unzip cmake gcc

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python3 /app/python-flask/aplicacion/app.py runserver