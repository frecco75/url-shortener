[![Codacy Badge](https://api.codacy.com/project/badge/grade/629f959d74f54dec8a8ed8a203f1569a)](https://www.codacy.com/app/fabien-recco/url-shortener)

# url-shortener
A URL shortener written in Python, using Django.


## Prerequisites ##
Install Django
```
pip install Django==1.9.4
```

Install pytz
```
pip install pytz
```

## Installation ##

Create the database
```
python manage.py migrate
```

## Running ##
```
python manage.py runserver
```
The web application will be accessible at http://127.0.0.1:8000/.
