#!/bin/bash

source myenv/bin/activate && \
pip install -r requirements.txt && \
echo 'yes' | ./manage.py collectstatic && \
./manage.py migrate

