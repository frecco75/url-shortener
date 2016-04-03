# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<token>\w{6})$', views.read, name='url_redirection'),
    url(r'^add$', views.add, name='url_add'),
    url('^.*$', views.go_to_home, name='go_to_home'),
]
