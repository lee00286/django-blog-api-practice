# practice-log

Blog API with Django Rest Framework

---

Date Links

* [2020-12-23](#2020-12-23-wed)
* [2020-12-31](#2020-12-31-thu)

---

## 2020-12-23 Wed

### [Bookmark App] Start a Project

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

Update `mysite/settings.py`

* Add IP adress of `ALLOWED_HOSTS` 
* Add DIRS of `TEMPLATES`
* Modify `TIME_ZONE`
* Create `STATICFILES_DIRS` for directory of static files
* Create `MEDIA_URL` and `MEDIA_ROOT` for upload functionality

**Keep secret key secret**

Update `mysite/settings.py`

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

### [Bookmark App] Start bookmark app

```
$ python3 manage.py startapp bookmark
```

## 2020-12-31 Thu

### [Bookmark App] Develop database tables

**Create bookmark table**

Update `bookmark/models.py`

Table columns:

* title: CharField
* url: URLField

**Display bookmark table**

Update `bookmmark/admin.py`

Display `id`, `title`, and `url` on admin page

**Migration**

```
$ python3 manage.py makemigrations bookmark
$ python3 manage.py migrate
```

### [Bookmark App] URLconf

Update `mysite/urls.py` and `bookmark/views.py`

* Add urls of bookmark list and detail view
* Import ListView and DetailView to use generic view

### [Bookmark App] Develop template file

Show bookmark list using a template files

* `bookmark_list.html`
* `bookmark_detail.html`

### [Blog App] URL configuration plan

| URL Pattern | View | Template |
| :-----------: | :------------: | :------------: |
| /blog/ | PostLV(ListView) | post_all.html |
| /blog/post/ | PostLV(ListView) | post_all.html |
| /blog/post/django-example/ | PostDV(DetailView) | post_detail.html |
| /blog/archive/ | PostAV(ArchiveIndexView) | post_archive.html |
| /blog/archive/2019/ | PostYAV(YearArchiveIndexView) | post_archive_year.html |
| /blog/archive/2019/nov/ | PostMAV(MonthArchiveIndexView) | post_archive_month.html |
| /blog/archive/2019/nov/10/ | PostDAV(DayYearArchiveIndexView) | post_archive_day.html |
| /blog/archive/today/ | PostTAV(TodayArchiveIndexView) | post_archive_day.html |
| /admin/ |  |  |

### [Blog App] Start blog app

```
$ python3 manage.py startapp blog
```

Update `mysite/settings.py` and `blog/models.py`

* Add blog in `INSTALLED_APPS` of `mysite/settings.py`
* Update columns of table Post in `blog/models.py`

**Migration**

```
$ python3 manage.py makemigrations blog
$ python3 manage.py migrate
```
