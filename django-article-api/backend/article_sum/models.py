from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=120)
	summary = models.TextField()
	complete = models.TextField()
	url = models.TextField()

	def _str_(self):
		return self.title
