from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'runTestCases', views.runTestCases, name='runTestCases'),
]