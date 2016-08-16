from django.conf.urls import *

urlpatterns = [
    url(r'', include('raceschedules.api.v1.urls', namespace='default')),
    url(r'^v1/', include('raceschedules.api.v1.urls', namespace='v1')),
]
