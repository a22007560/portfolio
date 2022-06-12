from django.contrib import admin

# Register your models here.

from .models import Blog, Project, Cadeira

admin.site.register(Blog)

admin.site.register(Project)

admin.site.register(Cadeira)
