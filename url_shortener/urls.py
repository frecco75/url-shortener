# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<token>\w{6})$', views.read),
    url(r'^add$', views.add),
    url('^.*$', views.redirect_to_home),
]
