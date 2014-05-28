from django.db import models
from django.contrib.auth.models import User


class PollAlternatives(models.Model):
    president = models.CharField(max_length=500)


class Poll(models.Model):
    user = models.OneToOneField(User)
    choice = models.ForeignKey(PollAlternatives)