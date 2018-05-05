#!/bin/sh

update_vcs() {
    cd /var/app || exit 1
    git pull
}

update_vcs