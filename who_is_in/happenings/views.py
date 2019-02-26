import datetime 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

def happening_create(request):
    handle_profile(request)

    isSuccess = False
    isUserLogged = request.user.is_authenticated

    path_name = request.GET.get('path_name')

    happening = None
    name = request.POST.get('name')
    description = request.POST.get('description')
    max_participants = request.POST.get('max_participants')
    date = request.POST.get('date')
    date = try_to_get_date(date) if date != None else None
    hashtags = request.POST.getlist('hashtag')
    print(hashtags)

    isFormCorrect = None not in [name, description, max_participants, date, hashtags] and is_int(max_participants)

    if isUserLogged and isFormCorrect:
        try:
            happening = Happening()
            happening.hashtags.set(handle_hashtags(hashtags))
            happening.creator = request.user
            happening.date = date
            happening.description = description
            happening.save()
        except Exception as e:
            print(e)
            isSuccess = False
        else:
            isSuccess = True

    response = None
    if not isUserLogged:
        response = HttpResponseRedirect(reverse('index'))
    else:
        response = render(request, "happening_create.html", {'isFormCorrect': isFormCorrect,
                                                             'isSuccess': isSuccess,
                                                             'isUserLogged': isUserLogged,
                                                             'path_name': path_name,
                                                             'max_range': list(range(1,100))})

    return response

def happening_detail(request, happening_id):
    handle_profile(request)
    return HttpResponse("happening_detail")

def delete_happening(request, happening_id):
    handle_profile(request)
    return HttpResponse("delete_happening")

def try_to_get_date(date_string):
    newDateString = date_string.replace("/", "-")
    return datetime.datetime.fromisoformat(newDateString)

#check if argument is int
def is_int(arg):
    isInt = True
    try:
        int(arg)
    except Exception as e:
        isInt = False
    return isInt


# get hashtags object for specific hastags, if hashtag does not exist - create new
def handle_hashtags(hashtags_list):
    ret = []
    for hashtag in hashtags_list:
        hashtagToAdd = Hashtag.objects.get(hashtag_name=hashtag)
        if hashtagToAdd == None:
            newHashtag = Hashtag()
            newHashtag.hashtag_name = hashtag
            newHashtag.save()
            hashtagToAdd = newHashtag
        ret.append(hashtagToAdd)
    return ret


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