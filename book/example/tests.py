from django.test import TestCase
from .models import Book,Author

class BookTestCase(TestCase):
    def setUp(self):
        print("setUp")

    def test_manyToMany(self):
        print('testcase')
