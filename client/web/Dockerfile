FROM node:10.14.2-alpine

WORKDIR /app
ADD . /app

ARG BUILD_ENV=local
ENV BUILD_ENV ${BUILD_ENV}

RUN npm i npm@latest -g
RUN npm install
RUN npm run build
RUN pwd
RUN ls -la

ENV HOST 0.0.0.0
EXPOSE 3000

CMD ["npm", "run", "start"]
