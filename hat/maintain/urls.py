from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'createNode', views.createNode, name='createNode'),
    url(r'getVersion', views.getVersion, name='getVersion'),
    url(r'saveVersion', views.saveVersion, name='saveVersion'),
    url(r'getHostPort', views.getHostPort, name='getHostPort'),
    url(r'saveHostPort', views.saveHostPort, name='saveHostPort'),
    url(r'getTestCase', views.getTestCase, name='getTestCase'),
    url(r'saveTestCase', views.saveTestCase, name='saveTestCase'),
]