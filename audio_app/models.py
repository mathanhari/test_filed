from django.db import models
from django.contrib.auth.models import User

class SongModel(models.Model):
    name = models.CharField(max_length=100)
    Song = models.FileField(upload_to='Song/')
    Duration = models.PositiveIntegerField()
    UploadeDate = models.DateTimeField()

    def __str__(self):
        return self.name

class PodcastModel(models.Model):
    name = models.CharField(max_length=100)
    Podcast = models.FileField(upload_to='Podcast/')
    Duration = models.PositiveIntegerField()
    UploadeDate = models.DateTimeField()
    Host = models.CharField(max_length=100)
    Participants = models.ManyToManyField(User, related_name='Participants')

    def __str__(self):
        return self.name


class AudiobookModel(models.Model):
    Title = models.CharField(max_length=100)
    Audiobook = models.FileField(upload_to='Audiobook/')
    Auther = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration = models.PositiveIntegerField()
    UploadeDate = models.DateTimeField()

    def __str__(self):
        return self.Title