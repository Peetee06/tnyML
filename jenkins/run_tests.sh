#!/bin/bash

source ${VENV_BIN_PATH}activate
# FIXME: for debugging
${VENV_BIN_PATH}pytest ${WORKSPACE}/flask/server/test --junitxml=./test_xml_reports/output.xml
