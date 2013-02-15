# Create your views here.
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render_to_response

def index(request):
	blogs = BlogPost.objects.all().order_by('-posted_date')
	return render_to_response('index.html', {'blogs': blogs})
	
def yearwise(request, year):
	blogs = BlogPost.objects.filter(posted_date__year=year).order_by('-posted_date')
	return render_to_response('index.html', {'blogs': blogs})

def monthwise(request, year, month):
	blogs = BlogPost.objects.filter(posted_date__year=year, posted_date__month=month).order_by('-posted_date')
	return render_to_response('index.html', {'blogs': blogs})

def datewise(request, year, month, date):
	blogs = BlogPost.objects.filter(posted_date__year=year, posted_date__month=month, posted_date__date=date).order_by('-posted_date')
	return render_to_response('index.html', {'blogs': blogs})
	
