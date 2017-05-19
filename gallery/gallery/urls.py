"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django.views.static
from django.conf.urls import url, include
from django.contrib import admin

from . import settings
from photo.models import Item, Photo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}
        ),
    # url(r'^$', include('simple.direct_to_template'),
    #     kwargs={
    #         'template': 'index.html',
    #         'extra_context': {'item_list': lambda: Item.objects.all()}
    #     },
    #     name='index'
    #     ),
    url(r'^items/$', include('list_detail.object_list'),
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'items_list.html',
            'allow_empty': True
        },
        name='item_list'
        ),
    url(r'^items/(?P<object_id>\d+)/$', include('list_detail.object_detail'),
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'items_detail.html'
        },
        name='item_detail'
        ),
    url(r'^photos/(?P<object_id>\d+)/$', include('list_detail.object_detail'),
        kwargs={
            'queryset': Photo.objects.all(),
            'template_name': 'photos_detail.html'
        },
        name='photo_detail'
        ),
]
