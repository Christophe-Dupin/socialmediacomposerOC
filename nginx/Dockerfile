# The first stage
# Build React static files
FROM node:13.12.0-alpine as build

# set work directory
WORKDIR /usr/src/app

ADD ./frontend/package.json ./
ADD ./frontend/package-lock.json ./
RUN npm ci --silent
ADD ./frontend/ ./
RUN npm run build

FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/src/app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
