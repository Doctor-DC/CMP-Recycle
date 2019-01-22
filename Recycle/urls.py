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

from unrelated_test.detail_view import InstanceDetail
from Recycle.view import InstancesList, CeaseInstances, ImagesList, ImagesCease, VolumesCease, VolumesList, SnapshotsList, \
    SnapshotsCease, RdbsList, RdbsCease

schema_view = get_swagger_view(title="Recycle")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/$', schema_view),
    url(r'^instances/list$', InstancesList.as_view()),
    # url (r'^instances/detail$', instance_detail.as_view ()),
    url(r'^instances/cease$', CeaseInstances.as_view()),
    url(r'^images/list$', ImagesList.as_view()),
    url(r'^images/cease', ImagesCease.as_view()),
    url(r'^volumes/list$', VolumesList.as_view()),
    url(r'^volumes/cease', VolumesCease.as_view()),
    url(r'^snapshots/list$', SnapshotsList.as_view()),
    url(r'^snapshots/cease$', SnapshotsCease.as_view()),
    url(r'^rdbs/list$', RdbsList.as_view()),
    url(r'^rdbs/cease$', RdbsCease.as_view()),
    # path('qingcloud/', include('resouces.qingcloud.urls')),

]
