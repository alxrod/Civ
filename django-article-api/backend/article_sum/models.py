from django.db import models
import random

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=120)
	summary = models.TextField()
	complete = models.TextField()
	url = models.TextField()
	category = models.IntegerField(default = 0)
	hn_rank = models.IntegerField(default=0)

	def _str_(self):
		return self.title
