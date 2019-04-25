from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView,DetailView,ListView, CreateView
from django.contrib import auth


def signup(request):
	if request.method == 'POST':
		print(request.POST)
		if '@' not in request.POST['email']:
			return render(request, 'registration/signup.html', {'errors':'invalid email address.'})
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'registration/signup.html', {'errors':'username has already been taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request, 'registration/signup.html', {'errors':'password does not match.'})
	else:
		return render(request, 'registration/signup.html')








	



