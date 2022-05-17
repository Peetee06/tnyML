#!/bin/bash

# create venv
python -m venv ${VENV_NAME}
# activate venv
source ${VENV_BIN_PATH}activate
# FIXME: for debugging
which python
# install dependencies
#${VENV_BIN_PATH}pip install ${WORKSPACE}/flask/server/ --cache-dir ${WORKSPACE}/.pipcache/
${VENV_BIN_PATH}python install ${WORKSPACE}/flask/server/setup.py
