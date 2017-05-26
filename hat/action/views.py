import time

import re
from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import simplejson
from maintain import models
from urllib import request, error


def runPost(param):
    pass


@csrf_exempt
def runTestCases(request):
    execute = request.GET.get('execute')
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
        if one['method'] == 0:
            # GET方法
            print(runGet(models.TestCase(**one), execute))
        elif one['method'] == 1:
            # POST方法
            runPost(models.TestCase(**one))
    return HttpResponse('ok')


def runGet(testCase, execute):
    if execute == '':
        execute = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(testCase)
    print("in the run ")
    start_time = time.time()
    url = testCase.getUrl()
    print(url)
    temp = request.Request(url)
    try:
        response = request.urlopen(temp)
    except error.HTTPError:
        result = models.Result(case_id=testCase, case_name=testCase.getName(), case_path=testCase.getPath(),
                               case_method=testCase.getMethod(), case_data=testCase.getJsonData(),
                               host_port=testCase.getHostPort(),
                               version=testCase.getVersion(), expect_result=testCase.getExpect(),
                               real_result="HTTPError", test_result=False, execute_time=time.time() - start_time,
                               execute=execute)
        result.save()
        return False
    except error.URLError:
        result = models.Result(case_id=testCase, case_name=testCase.getName(), case_path=testCase.getPath(),
                               case_method=testCase.getMethod(), case_data=testCase.getJsonData(),
                               host_port=testCase.getHostPort(),
                               version=testCase.getVersion(), expect_result=testCase.getExpect(),
                               real_result="URLError", test_result=False, execute_time=time.time() - start_time,
                               execute=execute)
        result.save()
        return False
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
    result = models.Result(case_id=testCase, case_name=testCase.getName(), case_path=testCase.getPath(),
                           case_method=testCase.getMethod(), case_data=testCase.getJsonData(),
                           host_port=testCase.getHostPort(),
                           version=testCase.getVersion(), expect_result=testCase.getExpect(),
                           real_result=str(real), test_result=test_result, execute_time=execute_time,
                           execute=execute)
    result.save()
    print(response.read())
    return test_result


def execute(request):
    results = models.Result.objects.all().values("execute").distinct()
    results = list(results)
    print(simplejson.dumps(results))
    return HttpResponse(simplejson.dumps(results))