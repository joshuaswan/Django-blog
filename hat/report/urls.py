from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'getResult/$', views.getResult, name='getResult'),
]