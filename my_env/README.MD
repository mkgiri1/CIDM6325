## Blog App using Django

---
**Notes**

* Install Django
* Create and Configure a Django project
* Create a Django application
* Design models and generate model migrations
* Create an administration site for our models
* Working with QuerySets and managers
* Build views, templates, and URLs
* Add pagination to list views
* Use Django’s class-based views

**Installed Apps**
INSTALLED_APPS is a setting which tells Django which applications are active for site.

**Extending Application**
* Adding Comments System – https://djangocentral.com/creating-comments-system-with-django/
* Adding Pagination to the Index page – https://djangocentral.com/adding-pagination-with-django/
* Integrating PostgreSQL with Django – https://djangocentral.com/using-postgresql-with-django/

***Migrations***
* `python manage.py makemigrations blog`
* `python manage.py migrate`

**gmail and smtp** [App Passwords](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637344913016438884-914897482&rd=1).

**Settings**

The settings file needs to be adjusted to use Postgres.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': '*****',
    }
}
```

## Enhancements of Blog with Advanced Features e.g
* Email
* Comments
* Tags and metadata
* Recommendations
* Custom template tags and filters
* Sitemap and syndication (both useful for SEO)
* Full-text search in Postgres (will be difficult to do on desktop)


