# from django.shortcuts import render
from django.views import generic
# from .models import posts
from . import models

# Create your views here.

class BlogIndex(generic.ListView):
	queryset = models.posts.objects.published()
	template_name = "home.html"
	paginate_by = 3