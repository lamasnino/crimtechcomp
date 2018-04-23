from django.conf.urls import url
from home.views import *

urlpatterns = [
    url(r'^.*', home_view),
    #url(r'^.*',include(crypto.views.home))
    #url(r'^.*',index,name = 'index')
]