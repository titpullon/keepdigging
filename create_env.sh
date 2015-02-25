#!/bin/bash

# creates .env for project

if [ -d ".env" ]; then
	rm -rf .env
fi

virtualenv .env
.env/bin/pip install -r requirements.txt
