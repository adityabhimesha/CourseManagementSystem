from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Teachers)
admin.site.register(models.Courses)
admin.site.register(models.Comments)
admin.site.register(models.Videos)
admin.site.register(models.Users_Extended)
