from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^v1/', include('raceschedules.api.v1.urls', namespace='v1')),
)
