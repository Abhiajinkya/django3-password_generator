from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'gen/home.html',{'password':'qwertyuiop'})

def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')

def about(request):
    return render(request, 'gen/about.html')
