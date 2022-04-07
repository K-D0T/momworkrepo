from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import random 
from home.models import *

from .forms import *


def Home(request):
	form = MainForm(request.POST, request.FILES)
	
	
	data = list(SubmitModel.objects.filter(author__icontains=request.user).values('pic'))
	
	pics = []
	
	for i in data:
		pics.append(i['pic'])
	return render(request, 'home.html', {"pics": pics, 'form': form})

def addpics(request):
	form = MainForm(request.POST, request.FILES)
	return render(request, 'addpics.html', {'form': form})


def submitpics(request):
	if request.method != 'POST':

		return HttpResponseRedirect(reverse("home"))
	else:
		
		form = MainForm(request.POST, request.FILES)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return HttpResponseRedirect(reverse('home'))
		else:
			print("Form is invalid")
			return HttpResponseRedirect(reverse('home'))

def create(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse('home'))
	else:
		global numberofpictures
		numberofpictures = request.POST['quantity']
		return HttpResponseRedirect(reverse('images'))

def images(request):
	data = list(SubmitModel.objects.filter(author__icontains=request.user).values('pic'))
	pics = []
	
	for i in data:
		pics.append(i['pic'])
	pics = random.sample(pics, int(numberofpictures))
	

	return render(request, 'images.html', {'pics':pics})

def logout_request(request):
	logout(request)
	return HttpResponseRedirect(reverse("home"))

def login_request(request):

	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:

			login(request, user)
			return HttpResponseRedirect(reverse("home"))
	else:
		print("invalid pass")

	form = AuthenticationForm()
	return render(request = request,template_name = "login.html", context={"form":form})

def createUser(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect(reverse("home"))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="createUser.html", context={"register_form":form})
