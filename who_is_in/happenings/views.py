from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Hashtag, Happening

# Create your views here.

def profile(request):
    handle_profile(request)
    return HttpResponse("profile")

def board(request):
    handle_profile(request)
    return HttpResponse("board")

def sign_to_happening(request, happening_id):
    handle_profile(request)
    return HttpResponse("sign_to_happening")

def unsign_from_happening(request, happening_id):
    handle_profile(request)
    return HttpResponse("unsign_from_happening")

def follow_hashtag(request, hashtag_name):
    handle_profile(request)
    return HttpResponse("follow_hashtag")

def unfollow_hashtag(request, hashtag_name):
    handle_profile(request)
    return HttpResponse("unfollow_hashtag")

def happening_create(request, happening_id):
    handle_profile(request)
    return HttpResponse("happening_create")

def happening_detail(request, happening_id):
    handle_profile(request)
    return HttpResponse("happening_detail")

def delete_happening(request, happening_id):
    handle_profile(request)
    return HttpResponse("delete_happening")

# check if profile for logged user exists - if not - create new profile
# and tie it to profile from request
def handle_profile(request):
    if request.user.is_authenticated:
        reqUser = User.objects.get(username=request.user.username)
        resultProfile = None

        try:
            resultProfile = Profile.objects.get(user=reqUser)
        except Exception as e:
            resultProfile = None

        if resultProfile == None:
            tempProfile = Profile()
            tempProfile.user = reqUser
            tempProfile.save()
            reqUser.save()