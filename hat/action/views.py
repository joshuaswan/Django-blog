import time

import re
from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from maintain import models
from urllib import request


def runPost(param):
    pass


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
        # one = models.TestCase.objects.get(case_id=one['case_id'])
        if one['method'] == 0:
            # GET方法
            print(runGet(models.TestCase(**one)))
        elif one['method'] == 1:
            # POST方法
            runPost(models.TestCase(**one))
    return HttpResponse('ok')


def runGet(testCase):
    print(testCase)
    print("in the run ")
    start_time = time.time()
    url = testCase.getUrl()
    print(url)
    temp = request.Request(url)
    response = request.urlopen(temp)
    stop_time = time.time()
    execute_time = stop_time - start_time
    print(testCase.getExpect())
    expect = testCase.getExpect()
    real = response.read()
    pattern = re.compile(expect)
    match = re.search(pattern, str(real))
    if match:
        test_result = True
    else:
        test_result = False
    result = models.Result(case_id=testCase, case_name=testCase.getName(), expect_result=testCase.getExpect(),
                           real_result=str(real), test_result=test_result, execute_time=execute_time,
                           execute="1")
    result.save()
    print(response.read())
    return test_result
