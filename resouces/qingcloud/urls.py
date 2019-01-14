from django.conf.urls import url

from Recycle.view import instances, ceaseinstances, imageslist, imagescease,volumeslist,volumescease,snapshotslist,snapshotscease
from Recycle.view import rdbscease,rdbslist

urlpatterns = [
    url(r'^instances/list$',instances.as_view()),
    url(r'^instances/cease$',ceaseinstances.as_view()),
    url(r'^images/list$',imageslist.as_view()),
    url(r'^images/cease$',imagescease.as_view()),
    url (r'^volumes/list$', volumeslist.as_view ()),
    url (r'^volumes/cease$', volumescease.as_view ()),
    url (r'^snapshots/list$', snapshotslist.as_view ()),
    url (r'^snapshots/cease$', snapshotscease.as_view ()),
    url (r'^rdbs/list$', rdbslist.as_view ()),
    url (r'^rdbs/cease$', rdbscease.as_view ()),



]