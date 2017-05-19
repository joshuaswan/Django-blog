from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'getTestCase', views.getTestCase, name='getTestCase'),
    url(r'createTestCase', views.createTestCase, name='getTestCase'),
    url(r'getAllTestCase', views.getAllTestCase, name='getAllTestCase'),
    url(r'createNode', views.createNode, name='createNode'),
]