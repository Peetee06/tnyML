#!/bin/bash

# create venv
python3 -m venv ${VENV_NAME}
# activate venv
source "${VENV_BIN_PATH}activate"
# install wheel
"${VENV_BIN_PATH}pip" install wheel
# install dependencies
"${VENV_BIN_PATH}pip" install "${WORKSPACE}/flask/server/"
