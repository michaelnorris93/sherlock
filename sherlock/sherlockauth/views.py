from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

def login_user(request):
	if request.user.is_authenticated():
		return render(request, 'useractive.html', {'user': request.user})

	state = "Please log in below..."
	username = password = ''
	
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
				return render(request, 'useractive.html', {'user': user})
			else:
				state = "Your account is not active, please contact the site admin."
		else:
			state = "Your username and/or password were incorrect."

	return render(request, 'login.html', {'state': state, 'username': username})

def logout_user(request):
	logout(request)
	return render(request, 'logout.html')

@login_required(login_url="/login/")
def homepage(request):
	return render(request, 'useractive.html', {'user': request.user})



def register_user(request):
	state = "Please fill in all of the blanks below..."
	username = password = confirm_password = email = '';
	
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm password')
		email = request.POST.get('email')

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
			return render(request, 'useractive.html', {'user': user})

	return render_to_response('register.html', {'state': state, 'username': username, 'email': email}, context_instance = RequestContext(request))
