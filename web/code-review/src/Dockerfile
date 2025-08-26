FROM node:23.11.0-alpine

WORKDIR /app
COPY . /app

RUN npm i

ENV NODE_ENV="production"

EXPOSE 3000

CMD ["npm", "run", "deploy"]
