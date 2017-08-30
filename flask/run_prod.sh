#!/usr/bin/bash
gunicorn webserver:app -b 0.0.0.0:5000 --threads 4
