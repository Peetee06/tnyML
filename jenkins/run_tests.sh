#!/bin/bash

source ${VENV_BIN_PATH}activate
pytest ${WORKSPACE}/flask/server/test --junitxml=./test_xml_report/output.xml
