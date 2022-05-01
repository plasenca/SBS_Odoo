FROM odoo:15.0

LABEL MAINTAINER DevfullScoopers <devfull@scoopers.com>
USER root

# Install nginx
RUN apt-get update && apt-get install -y nginx
RUN echo "Nginx Instalado"
# Install certbot
RUN apt-get update && apt-get install -y certbot
RUN echo "Certbot Instalado"
# Install certbot-nginx
RUN apt-get update && apt-get install -y python3-certbot-nginx
RUN echo "Certbot-Nginx Instalado"

# Reload nginx
RUN service nginx reload
RUN echo "Nginx Reiniciado"

# Generate SSL certificate
RUN certbot --nginx -d store.perusbs.com
