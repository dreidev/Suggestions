#`django-suggestions` Suggestions

[![Build Status](https://travis-ci.org/dreidev/Suggestions.svg?branch=ReadMe)](https://travis-ci.org/dreidev/Suggestions)

[![Coverage Status](https://coveralls.io/repos/dreidev/Suggestions/badge.svg?branch=HEAD&service=github)](https://coveralls.io/github/dreidev/Suggestions?branch=HEAD)

`django-suggestions` is a suggestions application for Django-powered websites.

> Suggestions can be added to any model's page in your application and it can help a user to discover other related pages they might find interesting based on what other users have viewed.


##Example
Let's say you have a model called Blog and you would like to add the suggestions functionality to it so users can find related blog posts when viewing any other blog post.

Consider this simple scenario:

1. User1 visits blog post (a)
2. User1 visits blog post (b)
..*The suggestions dictionary will be updated with an entry containing blog post (a) and blog post (b)
3. User2 visits blog post (b)

Now User2 will get a suggestion to visit blog post (a), this is due to the fact that some other user who visited (b) was interested in another blog post which is (a).

######The suggestions dictionary is the brain of this application; through self-learning it will be able to provide users with related similar interests to whatever they are viewing.

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
In `views.py` you need to first include the following imports

```python
from suggestions.views import update_suggestions_dictionary, get_suggestions
```

###Step 2
Continuing in `views.py`, you'll need to update the dictionary we talked about in the example above.

```python
update_suggestions_dictionary(request, self.object)
suggestions = get_suggestions(self.object)
```

However, `update_suggestions_dictionary` will only work with authenticated users.

* The `self.object` is for example the blog post object.
* You'll need to either add `suggestions` to the context dictionary or return it.

#####For `ClassBasedViews`:
You'll need to do this in the `DetailView` of say, model Blog, either in the `get` or `get_context_data` method.

#####For `FunctionBasedViews`:
Do this in the function responsible for rendering the template where you view the details of a certain Blog post.


###Step 3
To view the suggested objects in the intended html, say `blog_detail.html`, you can do the following:

```python
{% for suggestion in suggestions %}
	{{ suggestions.visited_before_object }}
{% endfor %}
```
The `visited_before_object` would be the suggested blog post and you can call any attribute you want from that object, for example:

```python
	{{ suggestions.visited_before_object.title }}
```
---
