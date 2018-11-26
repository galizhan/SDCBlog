from django.contrib import admin

# Register your models here.
from Comment.models import Comment

admin.site.register(Comment)