#!/bin/bash

sudo snap install node --classic
find -name "*npm*" /var/lib/snapd/snaps
sudo apt-get install -y npm
cd ${WORKSPACE}/tnyML
sudo npm install
sudo npm install -g @angular/cli