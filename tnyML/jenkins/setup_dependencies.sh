#!/bin/bash

sudo snap install node --classic
sudo apt-get install -y npm
cd ${WORKSPACE}/tnyML
sudo npm install
sudo npm install -g @angular/cli