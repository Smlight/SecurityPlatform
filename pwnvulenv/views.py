from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from pwnvulenv.models import Challenge, CVE, RunningChallenge, RunningCve
from pwnvulenv.serializers import UserSerializer, ChallengeSerializer, CveSerializer, RunningChallengeSerializer, \
    RunningCveSerializer


class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 50


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return super(UserViewSet, self).create(request,args,kwargs)


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    pagination_class = MyPageNumberPagination


class CveViewSet(viewsets.ModelViewSet):
    queryset = CVE.objects.all()
    serializer_class = CveSerializer
    pagination_class = MyPageNumberPagination


class RunningChallengeViewSet(viewsets.ModelViewSet):
    queryset = RunningChallenge.objects.all()
    serializer_class = RunningChallengeSerializer
    pagination_class = MyPageNumberPagination


class RunningCveViewSet(viewsets.ModelViewSet):
    queryset = RunningCve.objects.all()
    serializer_class = RunningCveSerializer
    pagination_class = MyPageNumberPagination
