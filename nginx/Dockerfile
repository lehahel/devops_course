FROM nginx:latest

EXPOSE 80

RUN rm -rf /sites-available && run -rf /sites-enabled

COPY sites-available /etc/nginx
COPY sites-enabled /etc/nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
