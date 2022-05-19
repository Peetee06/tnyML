#!/bin/bash

# create venv
python3 -m venv ${VENV_NAME}
# activate venv
source "${VENV_BIN_PATH}activate"
# install dependencies
"${VENV_BIN_PATH}pip" install -r "${WORKSPACE}/flask/server/requirements.txt"
