FROM node:18-alpine as frontend

WORKDIR /app
ADD package*.json webpack.config.js /app/
RUN npm install
ADD assets/ /app/assets/
RUN npm run bundle

FROM python:3-alpine3.10
RUN apk update && apk add build-base gcc musl-dev
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
COPY --from=frontend /app/static /app/static

