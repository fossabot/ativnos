#!/bin/sh

update_vcs() {
    cd /var/app || exit 1
    git pull
}

build_assets() {
    cd /var/app || exit 1
    nodejs node_modules/gulp/bin/gulp.js build
}

update_vcs
build_assets