from django.db import models


class RatingList(models.Model):
    username = models.CharField(max_length=150)
    sum = models.IntegerField()
    post = models.ForeignKey('Post.Post', on_delete=models.CASCADE)


class RatingSum(models.Model):
    post = models.OneToOneField('Post.Post', on_delete=models.CASCADE)
    amount = models.IntegerField()
    voted_amount = models.IntegerField()
