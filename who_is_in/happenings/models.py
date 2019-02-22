from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=128)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    observed_hashtags = models.ManyToManyField(Hashtag)

class Happening(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_happenings')
    max_participants = models.IntegerField()
    participants = models.ManyToManyField(Profile)
    hashtags = models.ManyToManyField(Hashtag)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=2048, default='')

    def add_user(self, user):
        self.participants.add(user)
        self.participants.save()