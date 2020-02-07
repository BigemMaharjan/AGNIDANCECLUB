from django.shortcuts import redirect
from DanceClub.models.modelsignup import User
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