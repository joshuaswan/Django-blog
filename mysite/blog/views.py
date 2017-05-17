from django.template import loader,Context
from django.http import HttpResponse
from . import models

def archive(request):
    posts = models.BlogPost.objects.all()
    t = loader.get_template("archive.html")
    data = {'posts': posts}
    print(data)
    return HttpResponse(t.render(data))
