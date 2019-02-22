from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
    return HttpResponse("profile")

def board(request):
    return HttpResponse("board")

def sign_to_happening(request, happening_id):
    return HttpResponse("sign_to_happening")

def unsign_from_happening(request, happening_id):
    return HttpResponse("unsign_from_happening")

def follow_hashtag(request, hashtag_name):
    return HttpResponse("follow_hashtag")

def unfollow_hashtag(request, hashtag_name):
    return HttpResponse("unfollow_hashtag")

def happening_create(request, happening_id):
    return HttpResponse("happening_create")

def happening_detail(request, happening_id):
    return HttpResponse("happening_detail")

def delete_happening(request, happening_id):
    return HttpResponse("delete_happening")