from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . import models

def createTestCase(request):
    models.NodeHierarchy.objects.create(name='test', details='test', input_code='test', node_order=1)

    return HttpResponse("createTestCase")

def getTestCase(request):
    # node = models.NodeHierarchy.objects.get()

    return HttpResponse("get test case")

def getAllTestCase(request):
    node = models.NodeHierarchy.objects.all()

    return HttpResponse("get all test case")