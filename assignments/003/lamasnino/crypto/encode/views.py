# encode views
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


    # function should iterate through string and add value of key's letter
    # to the value of the message's letter in the corresponding position
    
def encode(msg,key):
    key_count = 0
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    length_key=len(key)
    result =""
    switch = True
    for symbol in msg:
        if switch == True: # go forwards and toggle at mod key_length == 0, when you reach the end of the key
            key_character = key[key_count]
            if symbol.isalpha():
                encoded_number = alphabet.index(symbol)+alphabet.index(key_character)+1
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
                encoded_number = alphabet.index(symbol)+alphabet.index(key_character)+1
                result = result +alphabet[encoded_number%26]
            else:
                result = result + str(symbol)
            new_key = new_key-1
            key_count = key_count+1
            key_count = key_count%length_key
            if key_count%length_key == 0:
                    switch = not switch
    return result

def encode_view(request):
    #return HttpResponse('Hello, world! From encode_view')
    # if 'message' in request.POST and 'key' in request.POST:
    #     result = encode('message','key')
    #     context = {
    #     'message_input': request.POST['message'],
    #     'key_input': request.POST['key'],
    #     'result': result
    #     }
    #     return render(request,'encoder.html',context = context)
    # else:
    #     return render(request,'encoded.html')

    if 'message' in request.POST and 'key' in request.POST:
        msg = request.POST['message']
        key = request.POST['key']
        result = encode(msg,key)
        context = {
        'message_input': request.POST['message'],
        'key_input': request.POST['key'],
        'result': result
        }
        return render(request,'my_template.html',context = context)
    else:
        return render(request,'encoded.html')






    # title = 'My Title'
    # if request.method == 'POST':
    #     context = {'template_title': title,'encoded_message':None}
    #     msg,key = request.POST['msg'],request.POST['key']
    #     context['encoded_message'] = encode(msg,key)
    #     return render(request,'encoded.html',context = context)
    # else:
    #     return render(request,'encoded.html')







    #return render(request,'encoded.html', context = context)
    #else:
        #return render(request, 'index.html')
#def index(request):
    #return render(request, "index.html",context ={"index":None})



def index(request):
    return HttpResponse('Hello, world! From encode index')

def home(request):
    return HttpResponse('Hello, world! Home from encode')
#aaaaaaaaaa 1111111111
#add abc then cba then abc c
#2344322344 
#bcddcbbcda
# make rest of views


        
        
        #return HttResponse("<p>encoded_msg</p>")
      
