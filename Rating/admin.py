from django.contrib import admin

# Register your models here.
from Rating.models import RatingList, RatingSum

admin.site.register(RatingList)
admin.site.register(RatingSum)