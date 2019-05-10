import jdPrice.views
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^login/$', jdPrice.views.my_login),
    re_path(r'^register/$', jdPrice.views.register),
    re_path(r'^logout/$', jdPrice.views.my_logout),
    re_path(r'^queryid/$', jdPrice.views.queryid),
    re_path(r'^multiqueryid/$', jdPrice.views.multiqueryid),
    re_path(r'^smquery/$', jdPrice.views.smquery),
    re_path(r'^check/$', jdPrice.views.check_username),
    # re_path(r'^index/$', jdPrice.views.index),
]
