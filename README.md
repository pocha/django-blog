#Getting Started with Django

In this module, we will create our first Django Application that will display **Hello World**

## Lesson 0 - Installing Django

To get started with Django, you need to install Django first. 

If you have `pip` installed you can simply run `pip install Django`. Luckily, this has already been done on the codelearn server, so you don't need to bother about the installation process. 

However, if you want to work on your local machine you can follow the [instuctions here](https://docs.djangoproject.com/en/1.4/intro/install/)

## Lesson 1 - Creating the Project

Once you have installed Django, *django-admin.py* will be added to your system path.

*django-admin.py *is Django’s command-line utility for administrative tasks.
It will be used to create Django projects, handle database operations, run development server and do several other tasks which we'll dive into later modules.

To create your first Django project, goto the console and run

	django-admin.py startproject django_blog
	
This will create a folder *django_blog* with the following structure. Here, *django_blog* is the name of our project.

<del>A Django project is a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.</del>
> No useful information

    django_blog	
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	└── manage.py
	
These files are:

- **The outer django_blog/** directory is just a container for your project. Its name doesn't matter to Django; you can rename it to anything you like.	
- **manage.py:** A command-line utility that lets you interact with this Django project in various ways. It is a thin wrapper around django-admin.py. So inside a Django project you can run manage.py instead of django-admin.py.
- **The inner django_blog/** directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside it (e.g. import mysite.settings).
- **django_blog/__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
-  **django_blog/settings.py:** Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- **django_blog/urls.py:** It handles the URL declarations for the Django project. This will simply map URL patterns (simple regular expressions) to Python functions (your views).
- **django_blog/wsgi.py:** An entry-point for WSGI-compatible webservers to serve your project. This will be used, once we want to deploy our application for production. For now, we'll ignore it.

> Feb 7 - import word is kind of alien. What exactly import does needs explanation
> What is WSGI ?

Now, that our project is setup. We can test it by running a development server.

The Django development server is a built-in, lightweight Web server you can use while developing your site. It’s included with Django so you can develop your site rapidly, without having to deal with configuring your production server (e.g., Apache) until you’re ready for production

Run this command inside Django project

	python manage.py runserver
	
This will run a development server on port 8000. If you preview your app now you'll see a **"Welcome to Django"** page, in pleasant, light-blue pastel. It worked!

## Lesson 2 - Creating the app
In this module, we'll create our first Django Application that will show a **Hello World** message instead of Weclome to Django.

To create our application, we'll run this command inside our Django project in the console.
	cd django_blog
	python manage.py startapp blog

This will create a folder *blog* inside our project. The new file structure should look something like this.

    django_blog
	├── blog
	│   ├── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   ├── views.py
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	└── manage.py
	
Each Django application will consist of *models.py, tests.py and views.py*. For this module we'll only be dealing with *views.py* which shall be used to serve the content of our application.

To serve a simple static page from django, create a folder in djang_blog directory named static. Create a file named index.html inside
the static folder such that the directory structure now looks like,

    django_blog
	├── blog
	│   ├── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   ├── views.py
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	├── static
	│   ├── index.html
	└── manage.py
	
Edit index.html and add the following html content to it
	&lt!DOCTYPE html&gt
	&lthtml&gt
	Hello world!!
	&lt/html&gt
	
Edit the django_blog/django_blog/setting.py file and add the static directory to STATICFILES_DIRS which is 
django's list of directories which it searches to serve static files. Make sure that the STATIC_URL variable
in settings.py is set to '/static/'

	# URL prefix for static files.
	# Example: "http://media.lawrence.com/static/"
	STATIC_URL = '/static/'

	# Additional locations of static files
	STATICFILES_DIRS = (
		# Put strings here, like "/home/html/static" or "C:/www/django/static".
		# Always use forward slashes, even on Windows.
		# Don't forget to use absolute paths, not relative paths.
		'C:/workspace/django-blog/static',
	)

If STATICFILES_DIRS contains a single location as shown above, don't for to add a comma(,) at the end as shown.
[STATICFILES_DIRS is python tuple datatype and the way to declare a tuple with a single element is to add a comma after it.]

This shall be enough to tell our django project, to serve the static files from django_blog/static directory.

You can test the same by running development server again.

	python manage.py runserver

Enter location http://localhost:8000/static/index.html

That is it, preview your application and you shall see the **Hello World** message.
Note that you are accessing the file by adding static/ in the url which tell django to serve static files.

That's it for this module. We'll get into models and get started with blog views in the next module.

## Lesson 3 - Configure database

Django stores all the persistent information regarding the website, users and apps in a database.
So you need to configure the database details in the django_blog/settings.py file. For the purpose of 
this tutorial, we will use sqlite3 database which is a simple file-based database. Modify django_blog/settings.py and
add the details to DATABASES variable as shown below. 

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'C:/workspace/django-blog/django_blog.db',       # Or path to database file if using sqlite3.
			'USER': '',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}

Select ENGINE as django.db.backends.sqlite3. NAME should be the full path of the file which would be the actual
database. If it doesn't already exist django will create it for you. sqlite3 doesn't require user and password so 
you can leave that blank.
To update the database with relevant application information run the following command

	python manage.py syncdb

	
## Lesson 3 - Enable site admin interface

Django provides inbuilt admin interface for every django powered site. This interface can be
used to control application changes, add new users to the site, etc.
The admin interface is bundled as a django app (just like our blog app we created above). To enable it,
modify the django_blog/settings.py file and add django.contrib.admin to the list of installed apps by
simply uncommenting the corresponding line in INSTALLED_APPS as shown below

	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		# Uncomment the next line to enable the admin:
		**'django.contrib.admin',**
		# Uncomment the next line to enable admin documentation:
		# 'django.contrib.admindocs',
	)

Now you would want to access the admin interface with a specific URL. To tell django, which URL should take 
you to the admin page, you'll have to configure the django_blog/urls.py file. Uncomment the highlighted lines
in django_blog/urls.py

	from django.conf.urls import patterns, include, url

	# Uncomment the next two lines to enable the admin:
	**from django.contrib import admin**
	**admin.autodiscover()**

	urlpatterns = patterns('',
		# Examples:
		url(r'^$', 'blog.views.home'),
		# url(r'^$', 'django_blog.views.home', name='home'),
		# url(r'^django_blog/', include('django_blog.foo.urls')),

		# Uncomment the admin/doc line below to enable admin documentation:
		# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

		# Uncomment the next line to enable the admin:
		**url(r'^admin/', include(admin.site.urls)),**
	)

The line url(r'^admin/', include(admin.site.urls)) tells django that any url starting with admin/ should be handled
by the admin.site module. [ A module is a python script which is also used by other scripts. ] 
r'^admin/' is a regular expression (a special kind of string) which matches any string with a specific pattern.
In this case, it would match any string starting with 'admin/'.
To update the database with admin app related information, run
	
	python manage.py syncdb
	
You will be asked to create a superuser or admin account. Enter 'yes' and enter the username and password of your choice. 
You will need this to access the admin webpage.

	C:\workspace\django-blog>manage.py syncdb
	Creating tables ...
	Creating table auth_permission
	Creating table auth_group_permissions
	Creating table auth_group
	Creating table auth_user_user_permissions
	Creating table auth_user_groups
	Creating table auth_user
	Creating table django_content_type
	Creating table django_session
	Creating table django_site
	Creating table django_admin_log

	You just installed Django's auth system, which means you don't have any superuse
	rs defined.
	Would you like to create one now? (yes/no): yes
	Username (leave blank to use 'swapnil'):
	E-mail address: swapnil.st@gmail.com
	Password:
	Password (again):
	Superuser created successfully.
	Installing custom SQL ...
	Installing indexes ...
	Installed 0 object(s) from 0 fixture(s)

That's it. Your admin app should now be enabled. Run the development server
	
	python manage.py runserver

Try accessing it at http://localhost:8000/admin with username and password you just entered.

## Lesson 4 - Creating models


Write models
Sync database

Write URL

## Lesson 5 - Write first blog


## Lesson 2 - Writing views and configure urls

Views in django are functions that typically return the output you see for a specific URL.
All the relevant views for an app can reside in the apps's views.py file.
Each URL is typically handled by a specific view function.





