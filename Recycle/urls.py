"""Recycle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from Recycle.view import instances, ceaseinstances, imageslist, imagescease,volumescease,volumeslist

schema_view = get_swagger_view(title="Recycle")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/$',schema_view),
    url (r'^instances/list$', instances.as_view ()),
    url (r'^instances/cease$', ceaseinstances.as_view ()),
    url (r'^images/list$', imageslist.as_view ()),
    url (r'^images/cease', imagescease.as_view ()),
    url (r'^volumes/list$', volumeslist.as_view ()),
    url (r'^volumes/cease', volumescease.as_view ())
    # path('qingcloud/', include('resouces.qingcloud.urls')),

]
