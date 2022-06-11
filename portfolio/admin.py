from django.contrib import admin

# Register your models here.

from .models import Blog, Project

admin.site.register(Blog)

admin.site.register(Project)