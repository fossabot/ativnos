#!/bin/sh

APP_DIR=/var/app

update_vcs() {
    cd $APP_DIR || exit 1
    git pull
}

build_assets() {
    cd $APP_DIR || exit 1
    nodejs node_modules/gulp/bin/gulp.js build
}

migrate_databse() {
    cd $APP_DIR || exit 1
    docker-compose -f production.yml run django 'python manage.py migrate'
}

restart_service() {
    systemctl restart ativnos
}

update_vcs
build_assets
migrate_databse
restart_service