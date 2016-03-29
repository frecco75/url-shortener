# url-shortener
A URL shortener written in Python, using Django.


### Prerequisites ###
Install Django
```
pip install Django==1.9.4
```

Install pytz
```
pip install pytz
```

### Installation ###

Install the database
```
python manage.py makemigrations
python manage.py migrate
```

### Running ###
```
python manage.py runserver
```
The web application will be accessible at http://127.0.0.1:8000/.
