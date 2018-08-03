from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    year = models.IntegerField(null=True)
    game = models.CharField(max_length=64, null=True)
    file = models.FileField()
    difficulty = models.IntegerField(null=True)
    docker_repo = models.CharField(max_length=256, null=True)
    vagrant_box = models.CharField(max_length=256, null=True)
    poc = models.TextField(null=True)
    references = models.CharField(max_length=256, null=True)


class CVE(models.Model):
    cveid = models.CharField(max_length=64, primary_key=True)
    desc = models.TextField()
    dtime = models.DateField(null=True)
    program = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    difficulty = models.IntegerField(null=True)
    docker_repo = models.CharField(max_length=256, null=True)
    vagrant_box = models.CharField(max_length=256, null=True)
    poc = models.TextField(null=True)
    references = models.CharField(max_length=256, null=True)


class RunningChallenge(models.Model):
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    cid = models.ForeignKey(Challenge, on_delete=models.PROTECT)


class RunningCve(models.Model):
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    cid = models.ForeignKey(CVE, on_delete=models.PROTECT)
