#`django-suggestions` Suggestions

[![Build Status](https://travis-ci.org/dreidev/Suggestions.svg?branch=ReadMe)](https://travis-ci.org/dreidev/Suggestions)

[![Coverage Status](https://coveralls.io/repos/dreidev/Suggestions/badge.svg?branch=HEAD&service=github)](https://coveralls.io/github/dreidev/Suggestions?branch=HEAD)

`django-suggestions` is a suggestions application for Django-powered websites.

> Suggestions can be added to any model's page in your application and it can help a user to discover other related pages they might find interesting based on what other users have viewed.


##Example
Let's say you have a model called Blog and you would like to add the suggestions functionality to it so users can find related blog posts when viewing any other blog post.

Consider this scenario:

1. User1 visits blog post (a)
2. User1 visits blog post (b)
3. User2 visits blog post (b)

Now User2 will get a suggestion to visit blog post (a), this is due to the fact that some other user who visited (b) was interested in another blog post which is (a).


##Installation

Installation is available via `pip`

`$ pip install django-suggestions`

or via source on github

```
$ git clone https://github.com/dreidev/Suggestions.git
$ cd Suggestions
$ python setup.py install
```

Add 'suggestions' to your installed_apps in your `settings.py` file. It should look like the following. Note that you should add it after `django.contrib.auth`:

```python
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	...
	'suggestions',
	..
)
```

In your urls.py:

```python
urlpatterns = patterns('',
    ...
    url(r'^suggestions/', include('suggestions.urls')),
    ...
)
```


##Migrations for Django 1.7 and later

Migrate suggestions:
```
$ python manage.py migrate suggestions
```


##Setup

###Step 1


```python

```

###Step 2


```python

```

---
