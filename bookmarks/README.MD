## Bookmark App using Django

---

* There are a number of pre-built CBVs for authentication that we should use for [user authentication in Django](https://docs.djangoproject.com/en/3.1/topics/auth/).

* Updating conda itself with `conda update conda`
* Initial ***miniconda*** virtual environment : `conda create -n your_env python=x.x.x`
* Activating virtual environments : `conda activate your_env`
* once active, use `pip install` as normal
* upgrade a pip package this way: `pip install package_name --upgrade`

**Extending the User Model**

* Use of the default User object and [extension through a related Profile](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model)
* Extension of the [User model via in inheritance](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model).


**Social Authentication**

Using `social-auth-app-django`.  However, `django-allauth` is also common and popular. 

Social-auth is very capable and the services provided by it [are now fairly commodity](https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends).

For a fresh install, perhaps not specifying a version is best: `pip install social-auth-app-django`

***NOTE*** please note the `hosts` entry mentioned in Chapter 4. 
Using named hosts, it is necessary to indicate to Django what IPs or hosts it is permitted to operate on:

`ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']`

When we are in DEBUG mode, all traffic is allowed, but when we deploy, it will be a different matter.

***HTTPS Required***

Setting up [RunServerPlus]() for an extended development experience.

**Social Backends**

Authentication examples using Facebook, Twitter, and Google are included.
