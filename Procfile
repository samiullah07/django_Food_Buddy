web: python manage.py migrate && gunicorn FastFood.wsgi:application --bind 0.0.0.0:$PORT --access-logfile=- --error-logfile=- 
