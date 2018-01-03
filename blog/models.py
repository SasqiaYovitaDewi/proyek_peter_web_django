from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')

class Bekonomi(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')

class Bsains(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')
