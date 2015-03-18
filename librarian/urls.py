
from django.conf.urls import patterns, include, url
from django.contrib import admin
from librarian import views

urlpatterns=patterns('',
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
url(r'^first/$', views.first),
url(r'^index/$', views.index, name='index'),
url(r'^logout/$', views.logout_view, name='logout'),
)