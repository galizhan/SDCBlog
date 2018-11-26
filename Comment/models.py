from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('Post.Post', on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    text = models.TextField()
