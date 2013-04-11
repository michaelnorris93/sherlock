from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

from suggestions.models import suggestion, group
from suggestions.views import groupSuggestions

def homepage(request):
    if request.POST:    
        #go to group
        groupName = request.POST.get('groupName')
        if(groupName is not None):
            return groupSuggestions(request)
 
        #log in user
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')
        if(login_username is not None and login_password is not None):
            return login_user(request)    

        #register user
        register_username = request.POST.get('register_username')
        register_password = request.POST.get('register_password')
        register_cpassword = request.POST.get('register_cpassword')
        register_email = request.POST.get('register_email')
        if(register_username is not None and register_password is not None and register_cpassword is not None and register_email is not None):
            return register_user(request)

    return render_to_response('homepage.html', context_instance = RequestContext(request))

def login_user(request):
    if request.user.is_authenticated():
        #should never run since html should remove login modal if user is logged in 
        return render_to_response('homepage.html', context_instance = RequestContext(request)) 

    state = "Please log in below..."
    username = request.POST.get('login_username')
    password = request.POST.get('login_password')

    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            state = "You're successfully logged in!"
        else:
            state = "Your account is not active, please contact a site admin."
    else:
        state = "Your username and/or password were incorrect."    

    return render_to_response('homepage.html', {'state': state}, context_instance = RequestContext(request))

def logout_user(request):
    logout(request)
    return render_to_response('homepage.html', context_instance = RequestContext(request))

def register_user(request):
    state = "Please fill in all of the blanks below..."
    username = request.POST.get('register_username')
    password = request.POST.get('register_password')
    confirm_password = request.POST.get('register_cpassword')
    email = request.POST.get('register_email')
 
    try:
        user = User.objects.get(username = username)
        state = "That username is already taken."
    except User.DoesNotExist:
        donothing = 3

    if(password != confirm_password):
        state = "Your passwords do not match."
    else:
        if(password == ''):
            state = "Please enter a valid password."

    if(email == ''):
        state = "Please enter an email address."

    if(state == "Please fill in all of the blanks below..."):
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        user = authenticate(username=username, password = password)
        login(request, user)
    
    return render_to_response('homepage.html', {'state': state}, context_instance = RequestContext(request))

def about(request):
	return render_to_response('about.html', context_instance = RequestContext(request))
