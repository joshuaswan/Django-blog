from django.shortcuts import render
import json

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from maintain import models
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def getResult(request):
    hostPort = request.GET.get('searchHostPort')
    version = request.GET.get('searchVersion')
    if hostPort == "0" and version == "0":
        results = models.Result.objects.all()
    elif hostPort == "0":
        results = models.Result.objects.filter(version=models.Version.objects.get(id=int(version)))
    elif version == "0":
        results = models.Result.objects.filter(host_port=models.HostPort.objects.get(id=int(hostPort)))
    else:
        results = models.Result.objects.filter(host_port=models.HostPort.objects.get(id=int(hostPort)),
                                                   version=models.Version.objects.get(id=int(version)))
    # results = models.Result.objects.all()
    print(results.__dict__)
    print(serializers.serialize("json", results))
    return HttpResponse(serializers.serialize("json", results))
