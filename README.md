# MySandbox Project

## Intro
Work in progres<br>

I tried to do too many things at once so now I'm cleaning up, and removing redundant things
before I move forward.

## Installation:
### Manual
1. clone 
[mysandbox-backend-django](https://github.com/wdudek82/mysandbox)
from github: 
```
clone git@github.com:wdudek82/mysandbox.git && cd mysandbox
```
2. To force pipenv to create venv in project's root,
add to the ~/.bashrc or ~/.bash_profile:
```
export PIPENV_VENV_IN_PROJECT=1
```
3. Using system's/global pip install pipenv: 
```
sudo pip install pipenv
```  
4. Create virtual env, install project's dependencies,
and settings for proper env by typing
(type ```make``` in project's root for more information.): 
```
make [dev|prod]
```

### To make things work smoother
1. to auto-start virtual env configure [autoenv](https://github.com/kennethreitz/autoenv),
2. add to ~/.pip/pip.conf:<br>
```
[global]
format = columns
```

## Built with:
- Python 3.6
- Django 1.11.3
    - django-colorfield (color picker)
    - django-crispy-forms
    - django-debug-toolbar
    - django-rest-framework
    - django-rest-swagger
    - django-summernote (WYSIWYG editor)
    - grappelli
- Redis
- Celery
- Circus + Chaussette
- Nginx

### Other tools:
- virtualenv
- autoenv [docs](https://github.com/kennethreitz/autoenv)
- pipenv [docs](https://github.com/kennethreitz/pipenv)

### Relational DB:
- SQLite (in development)
- PostgreSQL (in production)

## Production Environment:


#### TODO:
- Makefile now can't really discern betwean prod and dev, and installs always all dependencies,
I must fix that
- User profiles
- avatar img: http://django-avatar.readthedocs.io/en/latest/
- Translations (PL/EN)
- create API
- sending messages between user profiles functionality
- contact form
- ...

#### Known issues
- for some reason colorfield is searching for jscolor in media dorectory, so after collectstatic it's folder must be copied
 from static to media root,
