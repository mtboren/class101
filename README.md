## class101
Simple python django application tutorial leading to deploying on Openshift

This demo is written for working from a RHEL7 client, python 2.7.x and eventually the openshift client. You can also do this on a Mac, and for the not-so-faint-of heart on a Windows machine.  At no time will you need to be a superuser.  You can also start developing with a free account at pythonanywhere.com


### Prework for Week #1

Nice to have (but not required):

* Create a public Github repo, e.g. class101
* Create your ssh keys, e.g. id_rsa_git and id_rsa_git.pub
* Add your public key to Git (Settings -> SSH and GPG keys)
* Add this stanza to your ~/.ssh/config

```
Host github.com
User <your github user>
IdentityFile ~/.ssh/id_rsa_git
ForwardX11 no
```

* Test your github ssh keys

```
ssh -T git@github.com
You've successfully authenticated, but GitHub does not provide shell access.
```

### Notes on python
Python is space sensitive.  To make your life easier, and to follow recommended style

* Don't use tabs
* Indent 4 spaces
* To facilate this add this line to your `~/.vimrc`:

```
set ai et ts=4 sw=4 sts=4 nu ru

# Or, put this one line here 
set modeline
# and add a line to each file as shown here

```


### Week #1
What will be covered:

* discussion on modern web development - no cgi-bin, no raw sql queries, but frameworks (ror, django, cakephp, catalyst, node/express, java?)
* MVC, SOC, DRY, uncoupling, ORM
* Why PaaS (Openshift, Heroku)
* Examples of current customers: nodejs (new development), php (brought in legacy app), others

```
>>> from dashboard.models import BuildConfig as BC
>>> from datetime import date, timedelta
>>>
>>> t = date.today()
>>> t
datetime.date(2017, 5, 8)
>>>
>>> y = t - timedelta(days=1)
>>> y
datetime.date(2017, 5, 7)
>>>
>>> BC.objects.filter(last_seen__lt=y).count()
0
>>> BC.objects.filter(last_seen__gt=y).count()
150

```

```
oc login
oc get pods

NAME                       READY     STATUS    RESTARTS   AGE
parse-image-data-1-grbi1   1/1       Running   0          3d
postgresql-1-e72f2         1/1       Running   0          3d
project.celery-1-1p7u7     1/1       Running   0          3d
redis-1-3504l              1/1       Running   0          3d
```



#### Getting started
* setup python on RHEL7 (on windows or free pythonanywhere account left to the user)
* Reference: https://docs.djangoproject.com/en/1.11/intro/tutorial01/

```
# This is an example - use your git, not mine, your username, etc., etc.
git clone git@github.com:johnedstone/class101.git
cd class101
git config user.name "johnedstone"
git config user.email "johnedstone@gmail.com"
git config push.default simple

virtualenv ~/.virtualenvs/class101
source ~/.virtualenvs/class101/bin/activate
pip install pip --proxy <ip:ort> --upgrade
deactivate

source ~/.virtualenvs/class101/bin/activate
pip install --proxy <ip:port>  django
pip freeze

# https://docs.djangoproject.com/en/1.11/intro/tutorial01/
django-admin startproject project

echo '# Using python 2.7.5' > project/requirements.txt
echo 'Django==1.11.1' >> project/requirements.txt

cd project
python manage.py runserver
# Log into to your server from elsewhere with ssh -x -C -L 8000:127.0.0.1:8000
# and then request from browser http://127.0.0.1:8000

# Alternative, edit project/project/settings and set ALLOWED_HOST = ['*']
python manage.py runserver 0.0.0.0:8000
# request from browser http://fqdn:8000

git branch -a
git remote -v
git status
git add .
git commit -m 'my first commit'
# git commit -am 'my first commit'
git push origin master
# git push
```


### Week #2

* backup and remove db.sqlite3 and add to .gitignore
* talk about port 8000 for those on a shared server
* lets look at the `project/project/settings`:
    * database
    * other stuff
* let's look at project/project/urls.py -- done in Week #1
* And ...

```
    cd project
    python manage.py makemigrations
    python manage.py makemigrations
    python manage.py migrate

    # Create 3 superusers
    python manage.py createsuperuser
    python manage.py createsuperuser
    python manage.py createsuperuser
    python manage.py runserver

    # Browse to /admin
    # And then let's look at the uncoupling - done in Week #1

    vim project/project/urls.py
    python manage.py runserver

    # Other cool stuff
    python manage.py dbshell
    sqlite> select * from auth_user;
    1|pbkdf2_sha256$36000$qwnljNIWs1TU$qhtnEkYC4JiElD6y7L6/lkGw+j3B7dpWW2Pm1Ak0DKs=||1|||a@b.com|1|1|2017-05-08 14:50:42.269990|boo
    sqlite> .quit

    python manage.py shell
    >>> from django.conf import settings
    >>> settings.ALLOWED_HOSTS
    ['*']
    >>>
    >>> from django.contrib.auth.models import User as U
    >>> u = U.objects.objects.all()
    >>> u = U.objects.all()
    >>> for ea in u:
    ...     ea.email
    ...     print('Email: {}'.format(ea.email))
    ...
         u'a@b.com'
         Email: a@b.com
    >>>

```

* Yet to plan
    * Talk about requests - hello world
    * Start an app
    * Create a view
    * Do some templating  stuff


##### vim: ai et ts=4 sts=4 sw=4 nu ru
