from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'gen/home.html',{'password':'qwertyuiop'})

def password(request):
    return render(request,'gen/password.html')

def about(request):
    return render(request, 'gen/about.html')
