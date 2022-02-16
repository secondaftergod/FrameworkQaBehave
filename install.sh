#!/bin/bash

FILE=venv/

if [ ! -d "$FILE" ]; then
    python3 -m venv venv
fi

source venv/bin/activate &&
pip install -U pip && pip install -r requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/*.feature
