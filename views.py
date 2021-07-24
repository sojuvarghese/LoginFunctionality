from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request, 'index.html') 
    
def login(request):
    if request.method == 'POST':
        ema = request.POST['email']
        data=User.objects.get(email=ema)
        if data.email == ema:      
            auth.login(request,request.user)
            return HttpResponseRedirect('/index/')


        else:
            return HttpResponseRedirect('/login/')


    else:        
        return render(request, 'login.html') 

def registration(request):
    if request.method == 'POST':
        u = request.POST['username']
        ema = request.POST['email']
        p = request.POST['password1']
        cp = request.POST['password2']

        if p == cp:
            if User.objects.filter(username=u).exists():
                return HttpResponseRedirect('/registration')
            elif User.objects.filter(username=u).exists():
                return HttpResponseRedirect('/registration')
            else:
                sav = User.objects.create_user(username = u, email = ema, password = p)
                sav.save()
                return HttpResponseRedirect('/login/')
    else:
        return render(request, 'registration.html')