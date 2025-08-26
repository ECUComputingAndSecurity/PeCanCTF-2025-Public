FROM node:20-alpine as build

WORKDIR /app
COPY package*.json .
RUN npm install

COPY . .
ARG VITE_BACKEND_URL=https://full-stack-reconnaissance-2.chals.pecanplus.org
RUN npm run build

FROM node:20-alpine

WORKDIR /app
RUN npm install -g serve

COPY --from=build /app/dist ./dist

EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
