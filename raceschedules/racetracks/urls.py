from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.RacetrackList.as_view(), name='list'),
    url(r'^new/$', views.RacetrackCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.RacetrackDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.RacetrackUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.RacetrackDelete.as_view(), name='delete'),
]
