#!/bin/bash

# install python
sudo apt-get install -y python3.9
# create venv
python -m venv ${VENV_NAME}
# activate venv
source ${VENV_BIN_PATH}activate
# install wheel
${VENV_BIN_PATH}pip install wheel
# install dependencies
${VENV_BIN_PATH}pip install ${WORKSPACE}/flask/server/ --cache-dir ${WORKSPACE}/.pipcache/
