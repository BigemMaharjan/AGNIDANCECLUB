from django.shortcuts import render,redirect
from django.contrib import messages
from DanceClub.models.modelsignup import User
from DanceClub.forms import Signupform

def indexview(request):
	users=User.objects.all()
	return render(request, 'index.html',{'users':users})

def aboutview(request):
	return render(request, 'about.html')

def whereview(request):
	return render(request, 'where.html')

def signupview(request):	
	if request.method == 'POST':
		form=Signupform(request.POST,request.FILES)
		form.save()
		return redirect('login')

	form=Signupform()
	return render(request, 'signup.html',{'form':form})

def loginview(request):
	# if request.method == 'POST':
	# 	form=Loginform(request.POST)

	return render(request, 'login.html')

# def entry(request):
	

def userdashboardview(request):
	return render(request, 'frontend/userdashboard.html')

def userprofileview(request):
	users=User.objects.all()
	return render(request, 'frontend/userprofile.html',{'users':users})

def adminprofileview(request):
	users=User.objects.all()
	return render(request, 'backend/adminprofile.html',{'users':users})

def admindashboardview(request):
	return render(request, 'backend/admindashboard.html')

def edit(request,id):
	user=User.objects.get(user_id=id)
	return render(request, 'edit.html', {'user': user})

def update(request,id):
	user=User.objects.get(user_id=id)
	form=Signupform(request.POST,instance=user)
	form.save()
	return redirect('adminprofile')

def delete(request,id):
	# user=User.objects.get(user_id=id).image.delete()
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('adminprofile')

def userdetailview(request):
	return render(request, 'backend/userDetail.html')

def addclass(request):
	return render(request, 'backend/addclass.html')

def addevent(request):
	return render(request, 'backend/addevent.html')
