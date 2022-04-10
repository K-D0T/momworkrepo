from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import os
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
		images = request.FILES.getlist('pic')
		
		for image in images:
			SubmitModel.objects.create(pic=image, author=request.user.username)

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


def deleteimage(request):

	if request.method != 'POST':

		return HttpResponseRedirect(reverse("home"))
	else:
		
		image = request.POST.get("pic")
		setup1 = SubmitModel.objects.filter(pic=image)
		setup1.delete()
		os.remove("/Users/Kaiden Thrailkill/Desktop/Environment/momwork/momwork/media/" + image)

		return HttpResponseRedirect(reverse('home'))
def matching(request):
	numberofpictures = request.POST['quantity']
	data = list(SubmitModel.objects.filter(author__icontains=request.user).values('pic'))
	pics = []
	
	for i in data:
		pics.append(i['pic'])
	pics = random.sample(pics, int(numberofpictures))
	match_pic = random.choice(pics)

	return render(request, 'matching.html', {'pics':pics, 'match_pic':match_pic})