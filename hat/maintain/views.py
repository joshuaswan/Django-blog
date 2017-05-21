# -*-coding:utf-8-*-
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from maintain import models


def createTestCase(request):
    models.NodeHierarchy.objects.create(name='test', details='test', input_code='test', node_order=1)

    return HttpResponse("createTestCase")


def getTestCase(request):
    print(request)
    testCases = models.TestCase.objects.all()
    print(testCases.__dict__)
    print(serializers.serialize("json", testCases))
    return HttpResponse(serializers.serialize("json", testCases))

    return HttpResponse("get test case")


def getAllTestCase(request):
    node = models.NodeHierarchy.objects.all()

    return HttpResponse("get all test case")


@csrf_exempt
def createNode(request):
    node = request.body
    # print(node)
    jsonData = json.loads(node.decode('utf-8'))
    print(models.NodeHierarchy(**jsonData).__dict__)
    models.NodeHierarchy(**jsonData).save()
    # models.NodeHierarchy.objects.create(nodeHierarchy)
    return HttpResponse('ok')


def getVersion(request):
    print(request)
    versions = models.Version.objects.all()
    print(versions.__dict__)
    print(serializers.serialize("json", versions))
    return HttpResponse(serializers.serialize("json", versions))


@csrf_exempt
def saveVersion(request):
    versions = request.body
    print(versions)
    jsonData = json.loads(versions.decode('utf-8'))
    print(jsonData)
    models.Version.objects.all().delete()
    for one in jsonData:
        print(one)
        models.Version(**one).save()
    return HttpResponse('ok')


def getHostPort(request):
    print(request)
    hostPorts = models.HostPort.objects.all()
    print(hostPorts.__dict__)
    print(serializers.serialize("json", hostPorts))
    return HttpResponse(serializers.serialize("json", hostPorts))


@csrf_exempt
def saveHostPort(request):
    hostPorts = request.body
    print(hostPorts)
    jsonData = json.loads(hostPorts.decode('utf-8'))
    print(jsonData)
    models.HostPort.objects.all().delete()
    for one in jsonData:
        print(one)
        models.HostPort(**one).save()
    return HttpResponse('ok')


@csrf_exempt
def saveTestCase(request):
    testCases = request.body
    print(testCases)
    jsonData = json.loads(testCases.decode('utf-8'))
    print(jsonData)
    models.TestCase.objects.all().delete()
    for one in jsonData:
        print(one)
        version = one["version"]
        print(version)
        version = models.Version(**version)
        one['version'] = version
        one['node_id'] = models.NodeHierarchy.objects.get(node_id=1)
        models.TestCase(**one).save()
    return HttpResponse('ok')
