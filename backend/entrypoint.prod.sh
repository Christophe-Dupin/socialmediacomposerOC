#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

python3 manage.py makemigrations
python manage.py migrate
python3 manage.py collectstatic --noinput
exec "$@"
