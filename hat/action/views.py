from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from maintain import models
from urllib import request


@csrf_exempt
def runTestCases(request):
    testCases = request.body
    print(testCases)
    jsonData = json.loads(testCases.decode('utf-8'))
    print(jsonData)
    for one in jsonData:
        print(one)
        version = one["version"]
        print(version)
        version = models.Version(**version)
        one['version'] = version
        host_port = one["host_port"]
        print(host_port)
        host_port = models.HostPort(**host_port)
        one['host_port'] = host_port
        one['node_id'] = models.NodeHierarchy.objects.get(node_id=1)
        runTestCase(models.TestCase(**one))
    return HttpResponse('ok')


def runTestCase(testCase):
    print(testCase)
    print("in the run ")
    url = testCase.getUrl()
    print(url)
    temp = request.Request(url)
    response = request.urlopen(temp)
    print(response.read())
    return True