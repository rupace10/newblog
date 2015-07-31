from django.db import models
from django_markdown.models import MarkdownField

body = MarkdownField()

# Create your models here.

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class posts(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
