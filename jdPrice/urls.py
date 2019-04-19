import jdPrice.views
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^login/$', jdPrice.views.login),
    re_path(r'^register/$', jdPrice.views.register),
    re_path(r'^queryid/$', jdPrice.views.queryid),
    re_path(r'^multiqueryid/$', jdPrice.views.multiqueryid),
    re_path(r'^smquery/$', jdPrice.views.smquery),
]
