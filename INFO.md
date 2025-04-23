# my-nemo-invent1

## See also

Github usnistgov/NEMO
[https://github.com/usnistgov/NEMO]

## 01 Create Django project - Initial commit

```
$ git clone https://github.com/common1/my-nemo-invent1.git
$ cd my-nemo-invent1
$ python3 -m venv venv
$ source venv/bin/acivate
$ pip install django
$ pip freeze > requirements.txt
$ django-admin startproject invent .
$ python manage.py migrate
$ python manage.py createsuperuser
Usename: ubuntuuser
Email: ubuntuuser@ubuntuserver.com
Password: ubuntuuser
```

## 02 Create MYIVT app + install - Part 1

```
$ python manage.py startapp MYIVT
 File: settings.py
 INSTALLED_APPS = [
    ...
    'MYIVT',
]

Install mptt
[https://django-mptt.readthedocs.io/en/latest/install.html]

$ pip install django-mptt
$ pip freeze requirements.txt
```

