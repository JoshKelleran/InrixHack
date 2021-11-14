from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'mysite/index.html')

def login(request):
    return render(request, 'mysite/login.html')

def googleauth(request):
    return render(request, 'mysite/googleauth.html')

def calendar(request):
    return render(request,'mysite/calendar.html')
