#!/bin/bash

# create venv
python -m venv ${VENV_NAME}
# activate venv
source ${VENV_BIN_PATH}activate
# install dependencies
${VENV_BIN_PATH}pip install ${WORKSPACE}/flask/server/ --cache-dir ${WORKSPACE}/.pipcache/
