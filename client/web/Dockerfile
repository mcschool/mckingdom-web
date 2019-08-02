FROM node:10.14.2-alpine

WORKDIR /app
ADD . /app

ARG BUILD_ENV=local
ENV BUILD_ENV ${BUILD_ENV}

RUN pwd && ls -la
RUN npm i npm@latest -g && npm i -g cross-env && npm i && npm i express
RUN pwd && ls -la ./node_modules
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD ["npm", "run", "start"]
