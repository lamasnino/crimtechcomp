# crypto crypto urls
# (my_project/my_project/urls.py

from django.conf.urls import include, url
from django.contrib import admin

from home import views
from encode import views
from decode import views
#from crypto import views

from home import urls as home_urls
from decode import urls as decode_urls
#from decode.views import *
#from encode.views import *
from encode import urls as encode_urls




urlpatterns = [
    # Examples:
    # url(r'^$', 'crypto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^decode/*', include(decode_urls)),
    url(r'^encode/*', include(encode_urls)),
    url(r'^/*',include(home_urls)),
    #url(r'^home/*', include(encode_urls)),
    #url(r'/*',views.home, name = 'home'),
    #url(r'^$', views.index, name = 'index'),
    #url(r'^.*',)#),
]

