from django import forms
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    food_name = models.CharField(max_length=500)
    ingredient = models.TextField()
    recipe = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.food_name


class Comment(models.Model):
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.author+' '+self.text

