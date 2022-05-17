#!/bin/bash

source ${VENV_BIN_PATH}activate
# FIXME: for debugging
which python
which pytest
pytest ${WORKSPACE}/flask/server/test --junitxml=./test_xml_report/output.xml
