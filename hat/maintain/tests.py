from django.test import TestCase
from . import models

class ModelsTestCase(TestCase):
    def setUp(self):
        pass

    def test_create(self):
        # print('test_create')
        models.NodeHierarchy.objects.create(name='test', details='test', input_code='test',node_order=1)
        node = models.NodeHierarchy.objects.get(name='test')
        print(node.__dict__)
        # print(dir(node))
