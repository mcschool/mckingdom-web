FROM node:10.13

WORKDIR /app
ADD . /app
RUN pwd
RUN ls -la

ARG BUILD_ENV=local
ENV BUILD_ENV ${BUILD_ENV}

RUN npm i npm@latest -g
RUN npm audit fix
RUN npm install
RUN npm run build
RUN pwd
RUN ls -la

ENV HOST 0.0.0.0
ENV NODE_ENV=production
EXPOSE 3000

CMD ["npm", "run", "start"]
