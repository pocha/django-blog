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
	
