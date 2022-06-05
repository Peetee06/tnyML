#!/bin/bash

source ${VENV_BIN_PATH}activate
${VENV_BIN_PATH}pip install -e ${WORKSPACE}/flask/server
${VENV_BIN_PATH}pytest ${WORKSPACE}/flask/server/test --junitxml=${WORKSPACE}/test-reports/output.xml
