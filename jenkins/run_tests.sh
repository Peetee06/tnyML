#!/bin/bash

source ${VENV_BIN_PATH}activate
# FIXME: for debugging
${VENV_BIN_PATH}pytest ${WORKSPACE}/flask/server/test --junitxml=${WORKSPACE}/test-reports/output.xml
