FROM odoo:15.0

LABEL MAINTAINER DevFullScoopers <projects@devfullscoopers.com>
USER root

RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install beautifulsoup4

