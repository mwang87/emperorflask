#!/bin/bash
cd /server
gunicorn webserver:app -b 0.0.0.0:5000 --threads 4 --timeout 3600 
