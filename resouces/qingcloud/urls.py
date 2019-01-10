from django.conf.urls import url

from Recycle.view import instances, ceaseinstances, imageslist, imagescease

urlpatterns = [
    url(r'^instances/list$',instances.as_view()),
    url(r'^instances/cease$',ceaseinstances.as_view()),
    url(r'^images/list$',imageslist.as_view()),
    url(r'^images/cease',imagescease.as_view())

]