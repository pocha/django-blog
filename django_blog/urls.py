from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^django_blog/', include('django_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^django_blog/','blog.views.index'),
	 url(r'^django_blog/(?P<year>\d+)/$', 'blog.views.yearwise'),
	 url(r'^django_blog/(?P<year>\d+)/(?P<month>\d+)/$', 'blog.views.monthwise'),
	 url(r'^django_blog/(?P<year>\d+)/(?P<month>\d+)/(?P<date>\d+)/$', 'blog.views.datewise'),	 
)
