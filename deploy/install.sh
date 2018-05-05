#!/bin/sh

# install docker
apt-get install docker docker-compose
systemctl enable docker

# firewall setup
systemctl enable ufw
ufw allow ssh
ufw allow http
ufw allow https
ufw default deny
ufw enable
