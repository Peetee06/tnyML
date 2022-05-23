#!/bin/bash

cd ${WORKSPACE}/tnyML
# run tests in headless chrome browser because vm does not have a gui
ng test --browsers ChromeHeadless