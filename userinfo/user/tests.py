from django.test import TestCase

# Create your tests here.
from . import models


class UserTestCase(TestCase):
    def setUp(self):
        models.UserInfo.objects.create(username='joshua',nid=1)

    def test_queryset(self):
        w = models.UserInfo.objects.all()
        print(w, type(w))
