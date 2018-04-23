# crypto decode urls
# (my_project/my_app/urls.py
from django.conf.urls import url
from decode.views import *


urlpatterns = [
    url(r'^.*', decode_view),
    #url(r'^.*',index,name = 'index')
]
