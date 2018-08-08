# coding=utf-8
# 此文件
from django.conf.urls import url

from apps.goods import views

urlpatterns = [
    url(r'^index$', views.index, name="index"),

]