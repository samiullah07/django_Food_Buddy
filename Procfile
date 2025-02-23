web: gunicorn FastFood.wsgi:application --bind 0.0.0.0:$PORT
web: gunicorn FastFood.wsgi:application --workers 4
web: python manage.py migrate && gunicorn FastFood.wsgi:application