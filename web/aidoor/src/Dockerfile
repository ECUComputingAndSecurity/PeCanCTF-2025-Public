FROM debian:12.10

# Updating and installing services
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install php php-fpm  nginx supervisor net-tools php-sqlite3 sqlite3
# Copying config files
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/supervisord.conf /etc/supervisord.conf

WORKDIR /app
COPY ./www /app

# Make sure the database is writable 
RUN chown www-data:www-data database.db
RUN chown www-data:www-data /app

EXPOSE 5000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]