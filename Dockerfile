FROM odoo:15.0

LABEL MAINTAINER DevfullScoopers <devfull@scoopers.com>
USER root

RUN sudo apt-get install nginx -y
