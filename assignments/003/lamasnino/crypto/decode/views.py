# decode views

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# make random test function

def decode(msg, key): 
  key_count = 0
  alphabet ='abcdefghijklmnopqrstuvwxyz'
  length_key=len(key)
  result =""
  switch = True
  for symbol in msg:
      if switch == True: # go forwards and toggle at mod key_length == 0, when you reach the end of the key
          key_character = key[key_count]
          if symbol.isalpha():
              encoded_number = alphabet.index(symbol) - alphabet.index(key_character) -1 
              result = result +alphabet[encoded_number%26]
          else:
              result = result + str(symbol)
          key_count = key_count+1
          key_count = key_count%length_key
          if key_count%length_key == 0:
              switch = not switch
              new_key = -1
      else:
          key_character = key[new_key]
          if symbol.isalpha():
              encoded_number = alphabet.index(symbol) - alphabet.index(key_character) -1 
              result = result +alphabet[encoded_number%26]
          else:
              result = result + str(symbol)
          new_key = new_key-1
          key_count = key_count+1
          key_count = key_count%length_key
          if key_count%length_key == 0:
              switch = not switch 
  return result


  # key_count = 0
  # alphabet ='abcdefghijklmnopqrstuvwxyz'
  # length_key=len(key)
  # result =""
  # switch = True
  # for symbol in msg:
  #   if switch == True: # go forwards and toggle at mod key_length == 0, when you reach the end of the key
  #     key_character = key[key_count]
  #     if symbol.isalpha():
  #       encoded_number = alphabet.index(symbol) - alphabet.index(key_character) -1 
  #       result = result +alphabet[encoded_number%26]
  #     else:
  #       result = result + str(symbol)
  #       key_count = key_count+1
  #       key_count = key_count%length_key
  #       if key_count%length_key == 0:
  #         switch = not switch
  #         new_key = -1
  #   else:
  #     key_character = key[new_key]
  #     if symbol.isalpha():
  #       encoded_number = alphabet.index(symbol) - alphabet.index(key_character) -1 
  #       result = result +alphabet[encoded_number%26]
  #     else:
  #       result = result + str(symbol)
  #     new_key = new_key-1
  #     key_count = key_count+1
  #     key_count = key_count%length_key
  #     if key_count%length_key == 0:
  #       switch = not switch
  # return result






#def index(request):
  #return render(request, "index.html",context ={"index":None})

def index(request):
  return HttpResponse('Hello, world! From index')

def home(request):
  return render(request,'home.html')
    #return HttpResponse('Hello, world! Home from decode')

    
def decode_view(request):
  if 'message' in request.POST and 'key' in request.POST:
    msg = request.POST['message']
    key = request.POST['key']
    result = decode(msg,key)
    context = {
    'message_input': request.POST['message'],
    'key_input': request.POST['key'],
    'result': result
    }
    return render(request,'my_template.html',context = context)
  else:
    return render(request,'decoded.html')
  # title = 'My Title'
  # if request.method == 'POST':
  #   context = {'template_title': title,'decoded_message':None}
  #   msg,key = request.POST['msg'],request.POST['key']
  #   context['decoded_message'] = decode(msg,key)
  #   return render(request,'decoded.html',context = context)
  # else:
  #   return render(request,'home.html')










  '''
  if request.method == 'POST':
    context = {'decoding': None}
    msg,k = request.POST['msg'],request.POST['k']

    context['decoding'] = decode(msg,k)
    return render(request,'decoded.html', context = context)
  else:
    return render(request, 'home.html')
      '''

