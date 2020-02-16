from django.shortcuts import redirect
from DanceClub.models.createmodel import User
from DanceClub.models.createmodel import Admin
from django.contrib import messages
from django.db.models import Q

class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				User.objects.get(Q(username=request.session['username']) & Q(password=request.session['password']))
				return function (request)
			except:
				messages.warning(request,"Invalid password or username")
				return redirect('login')
		return wrap

class Lock:
	def valid_admin(function):
		def wrap(request):
			try:
				Admin.objects.get(Q(name=request.session['name']) & Q(password=request.session['password']))
				return function (request)
			except:
				messages.warning(request,"Invalid password or name")
				return redirect('adminlogin')
		return wrap

		