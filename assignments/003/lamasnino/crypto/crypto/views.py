from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, world! Home from the legit home page I just set up')

        #return render(request,'home.html')
