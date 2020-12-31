# practice-log

Blog API with Django Rest Framework

---

Date Links

* [2020-12-23](#2020-12-23-wed)
* [2020-12-31](#2020-12-31-thu)

---

## 2020-12-23 Wed

### Start a Project

**Create and setup virtual environment**

```
$ virtualenv venv
$ pip3 install --upgrade setuptools pip
$ pip3 install -r requirements.txt
```

**Packages to install**

```
$ pip3 freeze > requriements.txt
$ pip3 install -r requirements.txt
```

**Create and setup a project**

```
$ django-admin startproject mysite
$ mv mysite blog
```

Update `settings.py`

* Add IP adress of `ALLOWED_HOSTS` 
* Add DIRS of `TEMPLATES`
* Modify `TIME_ZONE`
* Create `STATICFILES_DIRS` for directory of static files
* Create `MEDIA_URL` and `MEDIA_ROOT` for upload functionality

```
@mysite/settings.py
ALLOWED_HOSTS = ['192.168.56.101', 'localhost', '127.0.0.1']
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
TIME_ZONE = 'Asia/Seoul'
...
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = [os.path.join(BASE_DIR, 'media')]
```

**Keep secret key secret**

Update `settings.py`

```
@mysite/settings.py
from dotenv import load_dotenv
load_dotenv()
```

**Migration**

```
$ python3 manage.py migrate
```

**Create superuser**

```
$ python3 manage.py createsuperuser
```

### Start bookmark app

```
$ python3 manage.py startapp bookmark
```

## 2020-12-31 Thu

### Develop database tables

**Create bookmark table**

Use `bookmmark/models.py`

Table columns:

* title: CharField
* url: URLField

**Display bookmark table**

Use `bookmmark/admin.py`

Display `id`, `title`, and `url` on admin page

**Migration**

```
$ python3 manage.py makemigrations bookmark
$ python3 manage.py migrate
```
