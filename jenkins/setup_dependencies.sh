#!/bin/bash

# create venv
python -m venv ${VENV_NAME}
# activate venv
source ${VENV_BIN_PATH}activate
# install dependencies
${VENV_BIN_PATH}pip install -r ${WORKSPACE}/flask/server/requirements.txt --cache-dir ${WORKSPACE}/.pipcache/
echo pip install successfull
