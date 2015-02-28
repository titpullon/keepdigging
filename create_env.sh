#!/bin/bash

# creates .env for project

if [ -d ".env" ]; then
	rm -rf .env
fi

virtualenv .env

.env/bin/easy_install --upgrade virtualenv
.env/bin/easy_install pip

.env/bin/pip install -r requirements.txt
