from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, "gen/home.html")
    


def car(request):
    return HttpResponse("car") 

def password(request):
    thepass = ''
    characters = list('abcdefghijklmnopqrstuvwxyz') 
    number= list('0123456789')
    length = int(request.GET.get('lengthPass',6))

    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()')) 
    if request.GET.get('number'):
        characters.extend(number)

    for i in range(length):
        thepass += random.choice(characters)

    return render(request, "gen/password.html",{"password":thepass})
