from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main_template.html', context={'path_name':'index', 'isUserLogged': request.user.is_authenticated})