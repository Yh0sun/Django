from django import forms
from django.db import models
from django.utils import timezone


# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.post.id)+' '+self.text


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('title은 2글자 이상이여야 합니다.')


class Post(models.Model):
    # 변수 추가할 때는 python migrations 해야함
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[min_length_2_validator])
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # test = models.TextField()

    def __str__(self):
        return str(self.id) + ' ' + self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
