FROM node:12.4.0

# RUN apt-get update && apt-get -y install cron

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . /app

CMD /bin/bash
