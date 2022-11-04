from django.urls import re_path
from django.contrib import admin
from .import views

urlpatterns = [
    re_path(r'^$', views.home, name = 'home'),

    re_path(r'^iha_list/$', views.iha_list, name = "iha_list"),
    re_path(r'^createOrder/$', views.order_created, name = "order_create"),

    re_path(r'^(?P<id>\d+)/edit/$', views.iha_update, name = "iha_edit"),


    re_path(r'^(?P<id>\d+)/$', views.iha_detail, name = "iha_detail"),
    re_path(r'^detail/(?P<id>\d+)/$', views.order_detail, name = "order_detail"),

    re_path(r'^(?P<id>\d+)/delete/$', views.iha_delete, name = "iha_delete"),
    re_path(r'^(?P<id>\d+)/deleteOrder/$', views.order_delete, name = "order_delete"),

    re_path(r'^contact/$', views.contact, name = "contact"),

    re_path(r'^new_iha/$', views.new_iha, name = "new_iha"),
    re_path(r'^(?P<id>\d+)/like/$', views.like_update, name = "like"),
    re_path(r'^popular_iha/$', views.popular_iha, name = "popular_iha"),

]
