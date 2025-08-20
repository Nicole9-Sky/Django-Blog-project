#!/bin/bash

# Navigate to project directory
cd /home/Rupert/Django-Blog-project

# Activate virtual environment
source venv/Scripts/activate

# Start Gunicorn with 3 workers
exec gunicorn simpleblog.wsgi:application \
  --workers 3 \
  --bind 0.0.0.0:8000 \
  --log-file -
