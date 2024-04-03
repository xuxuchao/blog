from django.contrib import admin

# Register your models here.

from . import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','summary','add_timestamp','update_timestamp')

admin.site.register(models.DocumentContent,BlogPostAdmin)