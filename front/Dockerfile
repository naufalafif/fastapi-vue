FROM node:alpine as builder
WORKDIR '/app'

COPY package*.json ./
RUN yarn install
COPY . .
RUN yarn build:prod

FROM nginx
EXPOSE 80
COPY --from=builder /app/dist /usr/share/nginx/html/

RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]