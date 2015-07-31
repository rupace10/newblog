from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from . import models
from django.db.models import TextField

class EntryAdminh(MarkdownModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug": ("title",)}

	#to display markdown widget
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.posts, EntryAdminh)
admin.site.register(models.Tag)