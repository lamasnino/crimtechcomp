# encode views
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


    # function should iterate through string and add value of key's letter
    # to the value of the message's letter in the corresponding position
    
def encode(msg,k):
    # make a new encodedmsg
    encoded_msg=""
    msg=str(msg)
    k=str(k)
    i=0
    # how else would I specify that I take in strings?*
    # find numerical values of all letters in msg
    for i in msg[i]:
        l=0
        while l < len(k):
            for j in k:
                encoded_msg[i]=str(ord(msg[i])+ord(k[i]))
                l=l+1
            for h in k:
                encoded_msg[h]=str(ord(msg[h])+ord(k[-1]))
                l=l+1
    return encoded_msg
            
        ''' this is super super commented out (the other stuff is commented
            out because I'll need it later
    for j in k:
            encoded_msg[i]=ord(msg[i])+ord(k[i])
        for l in k:
            encoded_msg[l]=ord(msg[l])+ord(k[-1])'''






#aaaaaaaaaa 1111111111
#add abc then cba then abc c
#2344322344 
#bcddcbbcda
# make rest of views

def encode_view(request):
    if request.method == 'POST':
        context = {'encoding': None}
        msg,k = request.POST['msg'],request.POST['k']

        context['encoding'] = encode(msg,k)
        return render(request,'encoded.html', context = context)
    else:
        return render(request, 'index.html')
    
    
    #return HttResponse("<p>encoded_msg</p>")
  
