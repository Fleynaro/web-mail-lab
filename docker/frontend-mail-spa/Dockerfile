# build stage
FROM node:lts-alpine as build-stage

WORKDIR /app

COPY ./spa/package*.json ./
RUN npm install

COPY ./spa ./
RUN npm run build



# production stage
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./docker/frontend-mail-spa/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]



# useful
# https://ru.vuejs.org/v2/cookbook/dockerize-vuejs-app.html