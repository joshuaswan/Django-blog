from django.template import loader,Context
from django.http import HttpResponse
from . import models

def archive(request):
    posts = models.BlogPost.objects.all()
    t = loader.get_template("archive.html")
    for post in posts:
        temp = [ post.title,post.timestamp,post.body]
        print(temp)
        data = {'posts': temp}
    print(data)
    return HttpResponse(t.render(data))
