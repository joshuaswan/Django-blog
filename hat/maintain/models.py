from django.db import models

class Node_Hierarchy(models.Model):
    node_id = models.IntegerField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    parent_id = models.IntegerField(max_length=10)
    input_code = models.CharField(max_length=20)
    node_order = models.IntegerField(max_length=4)

class Test_Case(models.Model):
    case_id = models.IntegerField(primary_key=True,max_length=10)
    node_id = models.ForeignKey(Node_Hierarchy)
    case_name = models.CharField(max_length=100)
    host = models.CharField(max_length=50)
    port = models.IntegerField(max_length=10)
    path = models.CharField(max_length=200)

class Param(models.Model):
    param_id = models.IntegerField(primary_key=True,max_length=10)
    param_name = models.CharField(max_length=40)
    case_id = models.ForeignKey(Test_Case)
