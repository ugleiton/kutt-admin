#!/bin/bash
python manage.py collectstatic --noinput
gunicorn core.wsgi -b 0.0.0.0:8000 --workers=2 --timeout=600 --log-level=debug --log-file=/var/log/gunicorn/gunicorn.log
