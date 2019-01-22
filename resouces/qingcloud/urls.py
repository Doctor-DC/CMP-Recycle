from django.conf.urls import url

from Recycle.view import InstancesList, CeaseInstances, ImagesList, ImagesCease,VolumesList,VolumesCease,SnapshotsList,SnapshotsCease
from Recycle.view import RdbsCease,RdbsList

urlpatterns = [
    url(r'^instances/list$',InstancesList.as_view()),
    url(r'^instances/cease$', CeaseInstances.as_view()),
    url(r'^images/list$', ImagesList.as_view()),
    url(r'^images/cease$', ImagesCease.as_view()),
    url (r'^volumes/list$', VolumesList.as_view ()),
    url (r'^volumes/cease$', VolumesCease.as_view ()),
    url (r'^snapshots/list$', SnapshotsList.as_view ()),
    url (r'^snapshots/cease$', SnapshotsCease.as_view ()),
    url (r'^rdbs/list$', RdbsList.as_view ()),
    url (r'^rdbs/cease$', RdbsCease.as_view ()),



]