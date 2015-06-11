#!/bin/bash

if [ -z "$REPORTS_DIR" ]; then
    REPORTS_DIR='reports'
fi

# dir does not exist
if [ ! -d "$REPORTS_DIR" ]; then
    mkdir ${REPORTS_DIR}
fi

PYTHON_FILES=$(find . -name "*.py" \
    -not -path "*migrations/*" \
    -not -path "*deprecated/*" \
    -not -path "./venv/*" \
    -print)

# flake8 check against python files
echo "flake8 checking started..."
flake8 --config=./conf/flake8.conf ltsapi > ./${REPORTS_DIR}/flake8.log 2> /dev/null
echo "flake8 checking completed"