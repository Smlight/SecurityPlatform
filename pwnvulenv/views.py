from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from pwnvulenv.models import Challenge, CVE, RunningChallenge, RunningCve
from pwnvulenv.serializers import UserSerializer, ChallengeSerializer, CveSerializer, RunningChallengeSerializer, \
    RunningCveSerializer
import json, re, random
import time, os
import paramiko

DEFAULT_PAGE_SIZE = 50


class MyPageNumberPagination(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 100


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all().order_by('id')
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
def first_call(request):
    return render(request, 'index.html')


def user_login(request):
    res = {}
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            res['status'] = 'ok'
        except Exception as e:
            res['status'] = str(e)
    else:
        res['status'] = 'Method Error'
    return JsonResponse(res)


def user_logout(request):
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


# TODO 修改为密钥文件登录
HOSTS = {'192.168.17.131': '654321', }  # docker宿主机的地址和root密码


def connect(host):
    """this is use the paramiko connect the host, return conn"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username='root', password=HOSTS[host], allow_agent=True)
        return ssh
    except Exception as e:
        print(e)
        return None


def exec_commands(conn, cmd):
    """this is use the conn to excute the cmd and return the results of excute the command"""
    stdin, stdout, stderr = conn.exec_command(cmd)
    results = stdout.read()
    # print(stderr.read())
    return results


def do_deploy(request):
    res = {}
    if request.method == 'POST':
        try:
            # TODO 均衡分配任务
            host = random.choice(list(HOSTS))
            client = connect(host)
            username = request.user.username
            server = {'host': host, 'port': '22'}
            if 'cveid' in request.POST:
                cid = request.POST.get('cveid')
                cve = CVE.objects.get(cveid=cid)  # 不存在时触发异常
                RunningCve(uid=request.user, cid=cve).save()
                exec_commands(client, 'useradd -m {}'.format(username))
                exec_commands(client, 'echo {}\n{}\n | passwd {}'.format(username, username, username))
                if cve.use_docker:
                    exec_commands(client, 'usermod -a -G docker {}'.format(username))
                    server['cmd'] = 'docker run -it {} /bin/bash'.format(cve.docker_repo)
                else:
                    pass
            elif 'id' in request.POST:
                cid = request.POST.get('id')
                cha = Challenge.objects.get(id=cid)  # 不存在时触发异常
                exec_commands(client, 'useradd -m {}'.format(username))
                exec_commands(client, 'echo {}\n{}\n | passwd {}'.format(username, username, username))
                if cha.use_docker:
                    exec_commands(client, 'usermod -a -G docker {}'.format(username))
                    server['cmd'] = 'docker run -it {} /bin/bash'.format(cha.docker_repo)
                else:
                    pass
            else:
                raise Exception('Missing Id Data')
            res['status'] = 'ok'
            res['server'] = server
        except Exception as e:
            res['status'] = str(e)
    else:
        res['status'] = 'Method Error'
    return JsonResponse(res)


def do_search(request):
    res = {}
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        try:
            if keyword == '':
                raise Exception('Missing Keyword Data')
            # TODO 性能优化
            need_cha = request.POST.get('challenges', False)
            if need_cha:
                cha_list = Challenge.objects.filter(Q(title__icontains=keyword)
                                                    | Q(desc__icontains=keyword)
                                                    | Q(year__icontains=keyword)
                                                    | Q(game__icontains=keyword)
                                                    | Q(docker_repo__icontains=keyword)
                                                    | Q(vagrant_box__icontains=keyword)
                                                    | Q(poc__icontains=keyword)
                                                    | Q(references__icontains=keyword)).distinct()[:DEFAULT_PAGE_SIZE]
                res['CHAlist'] = [ChallengeSerializer(x).data for x in cha_list]
            need_cve = request.POST.get('cves', False)
            if need_cve:
                cve_list = CVE.objects.filter(Q(cveid__icontains=keyword)
                                              | Q(desc__icontains=keyword)
                                              | Q(component__icontains=keyword)
                                              | Q(version__icontains=keyword)
                                              | Q(severity__icontains=keyword)
                                              | Q(docker_repo__icontains=keyword)
                                              | Q(vagrant_box__icontains=keyword)
                                              | Q(poc__icontains=keyword)
                                              | Q(references__icontains=keyword)).distinct()[:DEFAULT_PAGE_SIZE]
                res['CVElist'] = [CveSerializer(x).data for x in cve_list]
            res['status'] = 'ok'
        except Exception as e:
            res['status'] = str(e)
    else:
        res['status'] = 'Method Error'
    return JsonResponse(res)
