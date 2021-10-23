## Bookmark App using Django

---
**Notes**

* Updating conda itself with `conda update conda`
* Initial ***miniconda*** virtual environment : `conda create -n your_env python=x.x.x`
* Activating virtual environments : `conda activate your_env`
* once active, use `pip install` as normal
* upgrading a pip package : `pip install package_name --upgrade`
* There are a number of pre-built CBVs for authentication that we should use for [user authentication in Django](https://docs.djangoproject.com/en/3.1/topics/auth/).

**Extending the User Model**

* Use of the default User object and [extension through a related Profile](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model)
* Extension of the [User model via in inheritance](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model).


**Social Authentication**

Using `social-auth-app-django`.  However, `django-allauth` is also common and popular. 

Social-auth is very capable [python-social-auth](https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends).

For a fresh install, perhaps not specifying a version is best: `pip install social-auth-app-django`

***named hosts***

We Must indicate to Django what IPs or hosts it is permitted to operate on:

`ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']`

When we are in DEBUG mode, all traffic is allowed.

***HTTPS Required***

Setting up [RunServerPlus]() for an extended development experience.

**Social Backends**

Authentication examples using Facebook, Twitter, and Google are included.

## Images & bookmarking

---
**Notes**

* models with many-to-many relationships -> Django ORM handles [many-to-many relationships](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/)
* jQuery with Django - to build a JavaScript bookmarklet to share images from other websites into our site
* image thumbnails - Using the easy-thumbnails library -> [Easy thumbnails](https://easy-thumbnails.readthedocs.io/en/latest/) 
* AJAX views with jQuery - pagination to the image list view -> [infinite scroll](https://www.seoclarity.net/blog/pagination-vs-infinite-scroll)
* command to run app with RunServerPlus : `python manage.py runserver_plus --cert-file cert.crt`
* django provides an ability to detect whether a POST (or any HTTP request) was made with [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest) using the [`is_ajax`](https://docs.djangoproject.com/en/3.1/ref/csrf/) method, we simplify this with a [Python Decorator](https://www.python.org/dev/peps/pep-0318/)


## Tracking & Following

---
**Notes**

* Follow system using many-to-many relationships with an intermediary model.
* Activity stream using generic relations
* Django signals – signal receiver function to denormalize related object counts
* Install and configure Redis, Python bindings for Redis
**Usefull Commands**
* Installing WSL : `wsl –install`
* Installing Redis Python Bindings : `pip install redis`
* Installing Reedis `sudo apt-get install redis-server`
