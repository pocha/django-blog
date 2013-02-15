from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=500)
	post = models.TextField()
	posted_date = models.DateTimeField('date posted')
	
	def __unicode__(self):
		return self.title
	