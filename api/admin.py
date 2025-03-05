from django.contrib import admin
from .models import Project, UserRole, Comment

admin.site.register(Project)
admin.site.register(UserRole)
admin.site.register(Comment)