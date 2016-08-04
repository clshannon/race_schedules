from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ActivityList.as_view(), name='list'),
    url(r'^new/$', views.ActivityCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ActivityDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ActivityUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ActivityDelete.as_view(), name='delete'),
]
