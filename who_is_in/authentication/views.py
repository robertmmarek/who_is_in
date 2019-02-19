from django.db.utils import IntegrityError as IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
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
            group = Group.objects.get('default')
            group.user_set.add(user)
            group.save()
        except IntegrityError as e:
            isLoginUnique = False
        except Exception as e:
            print(e)

    if user != None:
        user.save()
    else:
        response = HttpResponse('incorrect registration')

    return response

def change_password(request):
    isFormCorrect = set(['old_password', 'new_password', 'new_password_repeat']).issubset(request.POST.keys())
    isNewPasswordRepeated = False if not isFormCorrect else (request.POST['new_password'] == request.POST['new_password_repeat'])
    isUserLogged = request.user.is_authenticated

    isOperationSuccess = False
    response = HttpResponse('')

    if isUserLogged and isFormCorrect and isNewPasswordRepeated:
        try:
            user = authenticate(username=request.user.username, password=request.POST['old_password'])
            user.set_password(request.POST['new_password'])
            user.save()
            user = authenticate(username=request.user.username, password=request.POST['new_password'])
            login(request, user)
            isOperationSuccess = True
        except Exception as e:
            print(type(e), e)
            isOperationSuccess = False
    else:
        response = HttpResponse(str({'isFormCorrect': isFormCorrect, 
                                     'isNewPasswordRepeated': isNewPasswordRepeated, 
                                     'isUserLogged': isUserLogged}))

    return response