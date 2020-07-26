#!/usr/bin/env sh
SYNERGY=17525

yum install -y glibc.i686 libstdc++.i686 steamcmd
useradd -m steam
su - steam
mkdir ~/Steam && cd ~/Steam
steamcmd +login anonymous +force_install_dir ../synergy +app_update ${SYNERGY} +quit
ls -lAh
ls -lAh ../synergy
