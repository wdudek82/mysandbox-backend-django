# MySandbox Project


## Built with:
- Python 3.6
- Django 1.10.5
    - django-colorfield
    - django-debug-toolbar
    - django-rest-framework
    -django-rest-swagger
    - grappelli
- Redis
- Celery
- Circus + Chaussette
- Nginx

## Other tools:
- virtualenv
- virtualenvwrapper
- autoenv

## Relational DB:
- SQLite (in development)
- PostgreSQL (in production)


## Production Environment:

#### TODO:
- User profiles
- avatar img: http://django-avatar.readthedocs.io/en/latest/
- Translations (PL/EN)
- create API
- sending messages between user profiles functionality
- switch to Mezzanine :?
- contact form
- ...

#### Additional Info
- for some reason colorfield is searching for jscolor in media, so after collectstatic it's folder must be copied
 from static to media root,