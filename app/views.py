from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm

def home(request):
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username = username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, "Login Successful")
				return redirect('home')
			else:
				messages.success(request, "Login Error")
				return redirect('home')
		else:
			return render(request, 'home.html',{})


#def login_user(request):
#	pass

def logout_user(request):
	logout(request)
	messages.success(request,"Logged out")
	return redirect('home')

def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password= password)
			login(request,user)
			messages.success(request,"Sign In Successful")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request,'register.html',{'form':form})

	return render(request,'register.html',{})