# Dockerfile for gitcd.io Website
# Version 0.0.1
FROM php:7.1.1-apache

MAINTAINER Claudio Walser <claudio.walser@srf.ch>

COPY output/ /var/www/html/