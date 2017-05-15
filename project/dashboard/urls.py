from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^server-list/$', views.server_list, name='server_list'),
]
