# decode views

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# make random test function

def decode(msg, k): #<-- this is just a function
  
  return decoded_msg

# make rest of views

  
def decode_view(request):
    if request.method == 'POST':
        context = {'decoding': None}
        msg,k = request.POST['msg'],request.POST['k']

        context['decoding'] = decode(msg,k)
        return render(request,'decoded.html', context = context)
    else:
        return render(request, 'index.html')
    

