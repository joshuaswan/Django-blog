# -*-coding:utf-8-*-
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def createNode(request):
    node = request.body
    print(node)
    jsonData = json.loads(node.decode('utf-8'))
    print(models.NodeHierarchy(jsonData).__dict__)
    # nodeH.save()
    # models.NodeHierarchy.objects.create(nodeHierarchy)
    return HttpResponse('ok')
