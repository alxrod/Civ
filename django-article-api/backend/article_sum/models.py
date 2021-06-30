from django.db import models
import random

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=120)
	summary = models.TextField()
	complete = models.TextField()
	url = models.TextField()
	category = models.IntegerField(default = random.randint(1, 10))

	def _str_(self):
		return self.title
