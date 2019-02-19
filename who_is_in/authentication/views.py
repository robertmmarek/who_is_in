from django.db.utils import IntegrityError as IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.

def login_user(request):
    user = None
    response = HttpResponse('')
    isFormCorrect = set(['login', 'password']).issubset(request.POST.keys())
    if isFormCorrect:
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
    
    if user != None:
        response = HttpResponseRedirect(reverse('index'))
        login(request, user)
    else:
        response = HttpResponse('login incorrect')

    return response

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def register_user(request):
    isFormCorrect = set(['login', 'password']).issubset(request.POST.keys())
    isLoginUnique = True
    user = None
    response = HttpResponse('')

    if isFormCorrect:
        try:
            user = User.objects.create_user(request.POST['login'], password=request.POST['password'])
        except IntegrityError as e:
            isLoginUnique = False
        except Exception as e:
            print(e)

    if user != None:
        user.save()
    else:
        response = HttpResponse('incorrect registration')

    return response