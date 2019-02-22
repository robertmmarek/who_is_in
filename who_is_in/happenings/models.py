from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    observed_hashtags = models.ManyToManyField(Hashtag)

class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=128)

class Happening(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_happenings')
    max_participants = models.IntegerField()
    participants = models.ManyToManyField(Profile)
    hashtags = models.ManyToManyField(Hashtag)
    date = models.DateTimeField()
    description = models.CharField(max_length=2048)

    def add_user(self, user):
        self.participants.add(user)
        self.participants.save()