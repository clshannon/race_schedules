from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.EventList.as_view(), name='list'),
    url(r'^new/$', views.EventCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.EventDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.EventUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='delete'),
]
