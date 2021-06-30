from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "summary", "complete", "url", "category", "hn_rank")

# Register your models here.
admin.site.register(Article, ArticleAdmin)



