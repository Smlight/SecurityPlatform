from django.contrib.auth.models import User
from rest_framework import serializers
from pwnvulenv.models import Challenge, CVE, RunningChallenge, RunningCve


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser', 'is_active')


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields = ('title', 'desc', 'year', 'game', 'file', 'docker_repo', 'vagrant_box', 'poc', 'references')


class CveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CVE
        fields = ('cveid', 'desc', 'dtime', 'program', 'version', 'docker_repo', 'vagrant_box', 'poc', 'references')


class RunningChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningChallenge
        fields = ('uid', 'cid')


class RunningCveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCve
        fields = ('uid', 'cid')

