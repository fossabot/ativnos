#!/bin/sh

APP_DIR=/var/app

npm_install(){
    cd $APP_DIR || exit
    npm install
}

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

# install npm for building static assets
apt-get install npm
npm_install
