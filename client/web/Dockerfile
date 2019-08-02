FROM node:10.13

WORKDIR /app
ADD . /app

#ARG BUILD_ENV=local
#ENV BUILD_ENV ${BUILD_ENV}

RUN npm i npm@latest -g
RUN npm i
RUN npm run build
ENV HOST 0.0.0.0
EXPOSE 3000

CMD ["npm", "run", "start"]
