from django.contrib import admin
from recipe.models import Recipe, Comment

admin.site.register(Recipe)
admin.site.register(Comment)