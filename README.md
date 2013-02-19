#Module 1 - Getting Started with Django

In this tutorial, we will create our first Django Application. It will be a blog creating on Django framework.

## Lesson 0 - Installing Django

To get started with Django, you need to install Django first. 

If you have `pip` installed you can simply run `pip install Django`. Luckily, this has already been done on the codelearn server, so you don't need to bother about the installation process. 

However, if you want to work on your local machine you can follow the [instuctions here](https://docs.djangoproject.com/en/1.4/intro/install/)

## Lesson 1 - Creating the Project

Once you have installed Django, *django-admin.py* will be added to your system path.

*django-admin.py* is Django’s command-line utility for administrative tasks.
It will be used to create Django projects, handle database operations, run development server and do several other tasks which we'll dive into later modules.

To create your first Django project, run the following command

``Terminal``

	~/$ django-admin.py startproject django_blog
	
This will create a folder *django_blog* with the following structure.


    django_blog	
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	└── manage.py
	
These files are:

- **The outer django_blog/** directory is just a container for your project. Its name doesn't matter to Django; you can rename it to anything you like. 
- **manage.py:** A command-line utility that lets you interact with this Django project in various ways. It is a thin wrapper around django-admin.py. So inside a Django project you run ``python manage.py <command>`` instead of ``django-admin.py <command>``.
- **The inner django_blog/** directory is the actual Python package for your project. Its name is the Python package name you'll use to import modules in your main app(e.g. ``from django_blog import mysite.settings``). What are modules, we will see shortly. 
- **__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
- **settings.py:** Django can import apps (what are apps, we will see later). This file contains the list of the apps. The file also contain paths to static directory & similar other configurations.
- **urls.py:** The file contains mapping of URLs to appropriate Django view (as usual, Django views are introduced later).
- **wsgi.py:** This will be used, once we want to deploy our application for production. For now, we'll ignore it.

As mentioned in point 1, lets rename **outer django_blog** directory to django-tutorial-blog-app to avoid confusion

``Terminal``

	~/$ mv django_blog django-tutorial-blog-app


Now, that our project is setup. We can test it by running a development server.

The Django development server is a built-in, lightweight Web server you can use while developing your site. It’s included with Django so you can develop your site rapidly, without having to deal with configuring your production server (e.g., Apache) until you’re ready for production

Get inside the Django project & start the server

``Terminal``

	~/$ cd django-tutorial-blog-app
	~/django-tutorial-blog-app$ python manage.py runserver
	
This will run a development server on port 8000, if you have Django installed on your PC. You can view the app at *http://localhost:8000*.  In our case, simply Reload the **App Output** tab.

If everything goes right, you'll see a **"Welcome to Django"** page, in pleasant, light-blue pastel. It worked!

> Command to exit the server should be included here 

## Lesson 2 - Hello World
In this module, we'll create our first Django Application that will show a **Hello World** message instead of Welcome to Django.

We will show **Hello World** by creating a static page. For that, we do not need to use any of the files generated above. 

To serve a simple static page from django, create a folder named static. Create a file named index.html inside the static folder.

``Terminal``

	~/django-tutorial-blog-app$ mkdir static
	~/django-tutorial-blog-app$ touch static/index.html

The directory structure now looks like,

    django-tutorial-blog-app
	├── django_blog
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   ├── wsgi.py
	├── static
	│   ├── index.html
	└── manage.py
	
Edit index.html and add the following html content to it

``static/index.html``

	<!DOCTYPE html>
	<html>
	Hello world!!
	</html>
	
Edit the *django-tutorial-blog-app/settings.py* file and add the static directory to **STATICFILES_DIRS** which is django's list of directories which it searches to serve static files. 
You need absolute path to the static directory to put inside **STATICFILES_DIRS**

``Terminal``
	
	~/django-tutorial-blog-app$ pwd

You will see something like */home/user_1/django-tutorial-blog-app*. The absolute path to the static directory will be */home/user_1/django-tutorial-blog-app/static*.
``pwd`` is a linux command that gets you the path of your current directory. 

``django-tutorial-blog-app/settings.py``

	# URL prefix for static files.
	# Example: "http://media.lawrence.com/static/"
	STATIC_URL = '/static/'

	# Additional locations of static files
	STATICFILES_DIRS = (
		# Put strings here, like "/home/html/static" or "C:/www/django/static".
		# Always use forward slashes, even on Windows.
		# Don't forget to use absolute paths, not relative paths.
		'/home/user_1/django-tutorial-blog-app/static',
	)

*Even if STATICFILES_DIRS contains a single location as shown above, don't forget to add a comma(,) at the end as shown.*
[**STATICFILES_DIRS** is python tuple datatype and the way to declare a tuple with a single element is to add a comma after it.]

You can test the settngs so far by running development server again.

``Terminal``

	~/django-tutorial-blog-app$ python manage.py runserver

Enter location *http://localhost:8000/static/index.html* in your PC to view the page. Here you can simply enter *static/index.html* in the input box inside **App Output** & hit 'Go' to view the output. 

Note that you are accessing the file by adding static/ in the url which tell django to serve static files.

> Dont forget to shut down your server by pressing __ once you are done

## Lesson 3 - Configure database

Django stores all the persistent information regarding the website, users and apps in a database.
Eg. the blogs that we will write will be stored in this database.
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

The line `url(r'^admin/', include(admin.site.urls))` tells django that any url starting with admin/ should be handled
by the admin.site module. [ A module is a python script which is also used by other scripts. ] 
`r'^admin/'` is a regular expression (a special kind of string) which matches any string with a specific pattern.
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

Lets create models for our blog application. Models are essentially database tables which every app
uses to save app-specific information. The blog application will require just one model- BlogPost.
Edit django_blog/blog/models.py and add the following code so that it looks like, 

	from django.db import models

	# Create your models here.
	class BlogPost(models.Model):
		title = models.CharField(max_length=500)
		post = models.TextField()
		posted_date = models.DateTimeField('date posted')

What we are telling django here, is that we want every BlogPost to have a title, a post and posted_date fields.
A title would be a bunch of character (CharField, limited to maximum size of 500). A Post would be bunch of text (TextField)and 
posted_date, (DateTimeField) a date and time field.

Update the database so that it is able to store BlogPost related information,

	python manage.py syncdb
	

## Lesson 5 - Write your first blog

To be able to write out first blog, we need to add the blog app to the list of installed apps.
Modify django_blog/settings.py and add blog to the list of INSTALLED_APPS

	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		# Uncomment the next line to enable the admin:
		'django.contrib.admin',
		# Uncomment the next line to enable admin documentation:
		# 'django.contrib.admindocs',
		**'blog',**
	)

	
We will writing our blogs using the admin interface so we need to allow our app to be 
accessible by the admin. In order to do this, create a new file admin.py in django-blog/blog directory.
Add the following code to the admin.py file.

	from blog.models import BlogPost
	from django.contrib import admin

	admin.site.register(BlogPost)

	
Update the database and run the development server,

	python manage.py syncdb
	python manage.py runsever
	
Access the admin site by visiting http://localhost:8000/admin/

Now you can see the Blog posts model in the Blog app on the admin page.
Click **+Add** besides it, to add a new blog. Enter the blog contents and save it.
You should be able to see the newly created blog post in the list of blogs.
But it says *BlogPost object*. That is not very helpful in distinguishing different posts.
Let's change that. 
Modify django-blog/blog/models.py file and add a function __unicode__ to our BlogPost model,

	class BlogPost(models.Model):
		title = models.CharField(max_length=500)
		post = models.TextField()
		posted_date = models.DateTimeField('date posted')
		
		def __unicode__(self):
			return self.title

This will let django print the title of the blog while representing a particular blog post.
Now, simply refresh the page (no need to restart the server), and you should be able to see the 
title of the blog in place of *BlogPost object*. Now you can add as many blog posts as you like.

## Lesson 6 - Writing views and configure urls

Now, we want our blogs to be read by others as well. In other words, we would want to
be able to access them using specific urls. In django, each URL is typically handled by a single
view function. Views in django are functions that return the output you see for a given URL.
All the relevant views for an app can reside in the app's views.py file.

Let's write the view functions which will display our blogs.
In django-blog/blog/views.py, add the following code,

	# Create your views here.
	from django.http import HttpResponse
	from blog.models import BlogPost
	from django.template import Context, loader

	def index(request):
		blogs = BlogPost.objects.all().order_by('-posted_date')
		t = loader.get_template('index.html')
		c = Context({
			'blogs' : blogs,
		})
		return HttpResponse(t.render(c))
		
The BlogPost.objects.all() function retrieves all the blog posts presents in the database. 
The order_by('-posted_date') function sorts the list of blogs according to the date the were posted 
with the most recent ones first. The loader.get_template function loads a template file named index.html.
We'll talk more about template files later. We pass some information to the template in the form of Context 
object for it to generate the actual html. Finally the view returns an HttpResponse object which contains 
the html rendered by the template.

The next step is to configure the url for which the index view would be called; similar to what we did 
for the admin app. Modify django-blog/django_blog/urls.py and add the highlighted line,

	urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'django_blog.views.home', name='home'),
		# url(r'^django_blog/', include('django_blog.foo.urls')),

		# Uncomment the admin/doc line below to enable admin documentation:
		# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

		# Uncomment the next line to enable the admin:
		url(r'^admin/', include(admin.site.urls)),
		**url(r'^django_blog/','blog.views.index'),**
	)

This will tell django to call the index view for all the urls starting with django_blog/.

Next, we need to write the template file which will be returned by the index view and tell django where to find it.
A template file is just an html file, the contents of which are generated dynamically. 
It can contain python-like code with special syntax which helps in generating the actual html content.

Create a directory **/django-blog/templates** and add it to the list of django's template directories.

	TEMPLATE_DIRS = (
		# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
		# Always use forward slashes, even on Windows.
		# Don't forget to use absolute paths, not relative paths.
		'C:/workspace/django-blog/templates',
	)

Modify TEMPLATE_DIRS in django-blog/django_blog/settings.py as shown with the appropriate path for
templates directory. (Don't forget to add the comma.)
This allows django to search for template files in the templates directory.
Create a template file index.html in django-blog/templates directory with the following contents.

	{% if blogs %}
		{% for blog in blogs %}
			<p>
				<h2>{{blog.title}}</h2>
				Date: {{blog.posted_date}}<br/>
				<p>
				{{blog.post}}
				</p>
				==================================
			</p>
		{% endfor %}
	{% else %}
		<p>No blogs to show</p>
	{% endif %}

As you can see, the file contains python-like statement. Within the template we have access to
all the variables which were passed to us by the view as Context object through the render function.
As we did in the index function,
	
	t = loader.get_template('index.html')
		c = Context({
			'blogs' : blogs,
		})
		return HttpResponse(t.render(c))
		
Here we see that we pass a single variable blogs to the template's context, which we access within the
templates `{% if %}` statement. We iterate over the list of blogs to render each blog in an html paragraph.
Individual fields of a blog are accessed by "." operator. eg. `blog.post`

Start the server,
	
	python manage.py runserver
	
and checkout all the blogs you've written so far by accessing http://localhost:8000/django_blog/

## Lesson 7 - Writing more views and simplifying urls

Django provides few shortcut functions to simplify writing of views. Instead of using the loader.get_template 
function, creating a separate Context object and rendering the template, you can use a shortcut 
function- `render_to_response`. Modify the index view as shown below.

	from django.http import HttpResponse
	from blog.models import BlogPost
	from django.shortcuts import render_to_response

	def index(request):
		blogs = BlogPost.objects.all().order_by('-posted_date')
		return render_to_response('index.html', {'blogs': blogs})
		
This works exactly as before with less code to write.

We can add few more views to access the blogs as publised yearwise, monthwise and datewise.
Let's do that. Add the following views to django-blog/blog/views.py.

	def yearwise(request, year):
		blogs = BlogPost.objects.filter(posted_date__year=year).order_by('-posted_date')
		return render_to_response('index.html', {'blogs': blogs})

	def monthwise(request, year, month):
		blogs = BlogPost.objects.filter(posted_date__year=year, posted_date__month=month).order_by('-posted_date')
		return render_to_response('index.html', {'blogs': blogs})

	def datewise(request, year, month, date):
		blogs = BlogPost.objects.filter(posted_date__year=year, posted_date__month=month, posted_date__date=date).order_by('-posted_date')
		return render_to_response('index.html', {'blogs': blogs})
	

The function BlogPost.objects.filter retrives only those blogs from the database for which 
the filter criterion matches. In function yearwise, we filter only those blogs whose year in posted_date matches
the year variable as provided by the user. We'll see how the user can provide the year parameter through url, later.
Similarly, the monthwise and datewise views return the blogs further filtered by month and date, respectively.
Now lets configure the urls throught which we will access these views. Modify the django-blog/django_blog/urls.py
and add the following lines to it.

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^django_blog/','blog.views.index'),
	url(r'^django_blog/(?P<year>\d+)/$', 'blog.views.yearwise'),
	url(r'^django_blog/(?P<year>\d+)/(?P<month>\d+)/$', 'blog.views.monthwise'),
	url(r'^django_blog/(?P<year>\d+)/(?P<month>\d+)/(?P<date>\d+)/$', 'blog.views.datewise'),	 
	

Here we are using a bunch of regular expressions to call appropriate function for specific urls.
Eg. In regular expression **r'^django_blog/(?P<year>\d+)/$'**, the special characters, *^* and *$* signify the start and 
end of the string respectively. **\d+** matches one or more sequence of numbers. The expression **?P<year>** just tells
django to pass this particular matched sequence (\d+) while calling the corresponding view function.
Hence, a call to url like *http://localhost:8000/django_blog/2013* would match this particular regular expression
and the view blog.views.yearwise will be called and passed a year parameter. The same is true for other two views. 

You app is now completely ready. Happy blogging!!



