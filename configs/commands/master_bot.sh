#!/bin/sh

python manage.py makemigrations
python manage.py migrate --noinput

python ./run_bot.py