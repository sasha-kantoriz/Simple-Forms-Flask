FROM node:18-alpine as frontend

WORKDIR /app
ADD . /app

RUN npm install

FROM python:3-alpine3.10
RUN apk update && apk add build-base gcc musl-dev
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
COPY --from=frontend /app/static /app/static

