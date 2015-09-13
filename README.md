#`django-suggestions` Suggestions

[![Build Status](https://travis-ci.org/dreidev/Suggestions.svg?branch=ReadMe)](https://travis-ci.org/dreidev/Suggestions)

[![Coverage Status](https://coveralls.io/repos/dreidev/Suggestions/badge.svg?branch=HEAD&service=github)](https://coveralls.io/github/dreidev/Suggestions?branch=HEAD)

`django-suggestions` is a suggestions application for Django-powered websites.

> Suggestions can be added to any model's page in your application > and it can help users to discover other related pages they might > find interesting based on what other users have viewed.


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
In your models.py add the field comments to the model for which comments should be added (e.g. Blog) and the appropriate imports as shown below

```python
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

class Blog(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=256)
	body = models.TextField()
	comments = GenericRelation(Comment)
```

###Step 2
In your template (e.g. blog-detail.html) add the following template tags where object is the instance of blog.

```python
{% load comments_tags %}  # Loading the template tag
{% get_comments object request.user %}  # Include all the comments belonging to a certain object
{% comment_form object request.user %}  # Include the form for adding comments
{% get_comment_count object %}  # Include the number of comments on a certain object
```
The last template tag `{% get_comment_count object %}` is already included in `{% get_comments %}`, however you could include it seperately anywhere you want.

---
