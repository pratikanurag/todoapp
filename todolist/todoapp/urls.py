from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^details/(?P<id>\w{0,50})/$',views.details),
    url(r'^add',views.add,name='add'),
]