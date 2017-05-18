from django.db import models


class NodeHierarchy(models.Model):
    node_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    parent_id = models.IntegerField(null=True)
    input_code = models.CharField(max_length=20)
    node_order = models.IntegerField()


class TestCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    node_id = models.ForeignKey(NodeHierarchy)
    case_name = models.CharField(max_length=100)
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    path = models.CharField(max_length=200)
    method_choice = (
        (0, 'GET'),
        (1, 'POST'),
        (2, 'PUT'),
        (3, 'DELETE'),
    )
    method = models.IntegerField(choices=method_choice, default=0)
    version = models.CharField(max_length=40)


class Param(models.Model):
    param_id = models.AutoField(primary_key=True)
    param_name = models.CharField(max_length=40)
    case_id = models.ForeignKey(TestCase)
    value = models.CharField(max_length=200)
    type_choice = (
        (0, 'PARAM'),
        (1, 'PATH'),
    )
    type = models.IntegerField(choices=type_choice, default=0)
