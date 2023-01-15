FROM python:3-alpine3.10
RUN apk update && apk add build-base gcc musl-dev
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
