from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'gen/home.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    length=10

    thepassword=''
    for x in range(length):
        thepassword += random.choice(characters)



    return render(request,'gen/password.html',{'password':thepassword})

def about(request):
    return render(request, 'gen/about.html')
