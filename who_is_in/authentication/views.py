from django.db.utils import IntegrityError as IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group, UserManager
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.

def login_user(request):
    user = None
    response = HttpResponse('')
    isFormCorrect = set(['login', 'password']).issubset(request.POST.keys())
    isLoginCorrect = False
    if isFormCorrect:
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
    if user != None:
        isLoginCorrect = True
        login(request, user)
    else:
        isLoginCorrect = False

   
    
    if isLoginCorrect:
        response = HttpResponseRedirect(reverse('index'))
    else:
        response = render(request, "login.html", {'isLoginCorrect': isLoginCorrect, 
                                                  'isFormCorrect': isFormCorrect, 
                                                  'path_name': 'login'})

    return response

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def register_user(request):
    isFormCorrect = set(['login', 'password']).issubset(request.POST.keys())
    isLoginUnique = True
    isRegistrationSuccess = False
    registrationFailureReason = ""
    user = None
    response = HttpResponse('')

    if isFormCorrect:
        try:
            user = User.objects.create_user(username=request.POST['login'], password=request.POST['password'])
            user.save()
        except IntegrityError as e:
            registrationFailureReason = "username is not unique"
            isLoginUnique = False
        except Exception as e:
            registrationFailureReason = "unknown: "+str(e)

    if user != None:
        logout(request)
        login(request, user)
        isRegistrationSuccess = True

    if isRegistrationSuccess:
        response = HttpResponseRedirect(reverse('index'))
    else:
        response = render(request, 'register.html', {'isFormCorrect': isFormCorrect, 
                                                     'isLoginCorrect': request.user.is_authenticated, 
                                                     'isRegistractionSuccess': isRegistrationSuccess,
                                                     'registrationFailureReason': registrationFailureReason,
                                                     'path_name': 'register'})

    return response

def change_password(request):
    isFormCorrect = set(['old_password', 'new_password', 'new_password_repeat']).issubset(request.POST.keys())
    isNewPasswordRepeated = False if not isFormCorrect else (request.POST['new_password'] == request.POST['new_password_repeat'])
    isUserLogged = request.user.is_authenticated
    path_name = request.GET.get('path_name')

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
    
    if isUserLogged:
        response = render(request, 'change_password.html', {'isFormCorrect': isFormCorrect, 
                                                            'isNewPasswordRepeated': isNewPasswordRepeated, 
                                                            'isUserLogged': isUserLogged,
                                                            'isOperationSuccess': isOperationSuccess,
                                                            'path_name': path_name})
    else:
        response = HttpResponseRedirect(reverse('index'))

    return response