"""SecurityPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from rest_framework import routers
from pwnvulenv import views as pwnviews
from xterm_django import views as xtermviews
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', pwnviews.UserViewSet)
router.register(r'challenges', pwnviews.ChallengeViewSet)
router.register(r'cves', pwnviews.CveViewSet)
router.register(r'runningchallenges', pwnviews.RunningChallengeViewSet)
router.register(r'runningcves', pwnviews.RunningCveViewSet)

urlpatterns = [
    url(r'^webssh$', xtermviews.ssh_with_websocket, name='xtermwebssh'),

    url(r'^userlogin/', pwnviews.user_login),
    url(r'^userlogout/', pwnviews.user_logout),
    url(r'^getuserinfo/', pwnviews.getuserinfo),
    url(r'^deploy/', pwnviews.do_deploy),
    url(r'^search/', pwnviews.do_search),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    # url(r'.*', TemplateView.as_view(template_name="index.html")),
    url(r'.*', pwnviews.first_call),
]
