from django.contrib.auth.models import User
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from pwnvulenv.models import Challenge, CVE, RunningChallenge, RunningCve
from pwnvulenv.serializers import UserSerializer, ChallengeSerializer, CveSerializer, RunningChallengeSerializer, \
    RunningCveSerializer
import json
import re
import time
from django.db.models import Q
import os
from django.views.decorators.csrf import ensure_csrf_cookie

class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 50


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    pagination_class = MyPageNumberPagination


class CveViewSet(viewsets.ModelViewSet):
    queryset = CVE.objects.all().order_by('cveid')
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


@ensure_csrf_cookie
def userlogin(request):
    res = {}
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            # request.session['user'] = username
            res['status'] = 'ok'
            if user is None:
                raise Exception('Authenticate Failed')
        except Exception as e:
            res['status'] = str(e)
    else:
        res['status'] = 'Method Error'
    return JsonResponse(res)


def userlogout(request):
    res = {}
    logout(request)
    res['status'] = 'ok'
    return JsonResponse(res)


def getuserinfo(request):
    res = {}
    if request.method == 'GET':
            if request.user.is_authenticated:
                res['user'] = request.user.username
                res['status'] = 'ok'
            else:
                res['status'] = 'Not Authenticated'
    else:
        res['status'] = 'Method Error'
    return JsonResponse(res)

def dodeply(request):
    res = {}
    username = request.user.username
    try:
        os.system('useradd -m {}'.format(username))
        os.system('echo {}\n{}\n | passwd {}'.format(username,username,username))
        os.system('usermod -a -G docker {}'.format(username))
    except Exception as e:
        print(e)
    res['hostname'] = '127.0.0.1'
    res['port'] = 22
    res['status'] = 'ok'
    return JsonResponse(res)