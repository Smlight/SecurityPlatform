from django.contrib.auth.models import User
from rest_framework import serializers
from pwnvulenv.models import Challenge, CVE, RunningChallenge, RunningCve
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_superuser', 'is_active')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)



class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'desc', 'year', 'game', 'file', 'difficulty', 'docker_repo', 'vagrant_box', 'poc',
                  'references')


class CveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CVE
        fields = ('cveid', 'desc', 'dtime', 'program', 'version', 'difficulty', 'docker_repo', 'vagrant_box', 'poc',
                  'references')


class RunningChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningChallenge
        fields = ('uid', 'cid')


class RunningCveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCve
        fields = ('uid', 'cid')
