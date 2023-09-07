FROM nginx:1.23.4-alpine

WORKDIR /var/www/app

ADD app.conf /etc/nginx/conf.d/default.conf
RUN mkdir /var/www/app/staticfiles