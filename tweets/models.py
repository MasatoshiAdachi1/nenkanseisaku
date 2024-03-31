from django.db import models

class Tweet(models.Model):
    item = models.CharField(max_length=200)