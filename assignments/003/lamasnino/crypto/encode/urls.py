# crypto encode urls
# (my_project/my_app/urls.py
from django.conf.urls import url
from encode.views import *

urlpatterns = [
    url(r'^.*', encode_view),
]

# make random test function

'''def encode(x, y, f): #<-- this is just a function
  f = f.strip().lower()
  if f == 'add':
    return x + y
  elif f == 'subtract':
    return x - y
  elif f == 'multiply':
    return x * y
  elif f == 'divide':
    return x / y
  elif f == 'power':
    return x ** y
  else
    return None

# make rest of views

def encode_view():'''
