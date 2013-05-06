<h3>Get these tools</h3>
```
$ pip install virtualenv
$ pip install virtualenvwrapper
```

<h3>Set up virtual env</h3>
```
$ mkvirtualenv bounce
$ pip install django
```

<h3>Get the source code</h3>
```
$ git clone git@github.com:ryangallen/bounce.git
$ cd bounce
```

<h3>Setup the db</h3>
```
$ manage.py syncdb     #make sure to setup an admin user
```

<h3>Run it</h3>
```
$ manage.py runserver
```
<hr>
<p>Built using the tutorial at https://tutsplus.com/course/django-unchained/. Special thanks to <a href="https://github.com/croach">Christopher Roach</a> for making the tutorial and helping me out personally.</p>
