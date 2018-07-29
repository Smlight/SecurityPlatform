from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    year = models.IntegerField()
    game = models.CharField(max_length=64)
    file = models.FileField()
    docker_repo = models.CharField(max_length=256)
    vagrant_box = models.CharField(max_length=256)
    poc = models.TextField()
    references = models.CharField(max_length=256)


class CVE(models.Model):
    cveid = models.CharField(max_length=64)
    desc = models.TextField()
    dtime = models.DateField()
    program = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    docker_repo = models.CharField(max_length=256)
    vagrant_box = models.CharField(max_length=256)
    poc = models.TextField()
    references = models.CharField(max_length=256)


class RunningChallenge(models.Model):
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    cid = models.ForeignKey(Challenge, on_delete=models.PROTECT)


class RunningCve(models.Model):
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    cid = models.ForeignKey(CVE, on_delete=models.PROTECT)
