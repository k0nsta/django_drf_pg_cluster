#!/bin/bash

set -e
set -u

# Only for demonstration purpose
if [ ! -f /code/apps/library/migrations/0001_initial.py ]; then
    python /code/manage.py collectstatic --noinput
    python /code/manage.py makemigrations
    python /code/manage.py migrate
    echo "Begin initial seeding of the database with fake data."
    python /code/manage.py gendata
    echo "Initial seeding of the database with fake data finished."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '${ADMIN_PWD}')" | python manage.py shell
    echo ""
fi

gunicorn --config=/code/conf/gunicorn.py conf.wsgi:app --chdir=/code

