# coding=utf-8
from django.db import models
from altauth.models import PollingUser


class PollAlternatives(models.Model):
    president = models.CharField(max_length=500)


class Poll(models.Model):
    user = models.OneToOneField(PollingUser)
    choice = models.ForeignKey(PollAlternatives)


def create_def_choices():
    PollAlternatives.objects.get_or_create(president=u"Джордж Вашингтон")
    PollAlternatives.objects.get_or_create(president=u"Джон Адамс")
    PollAlternatives.objects.get_or_create(president=u"Томас Джефферсон")
    PollAlternatives.objects.get_or_create(president=u"Джеймс Медисон")
    PollAlternatives.objects.get_or_create(president=u"Джеймс Монро")