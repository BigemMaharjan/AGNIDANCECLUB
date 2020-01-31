from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from DanceClub.models.modelsignup import User
from DanceClub.forms import Signupform
from DanceClub.authentication import Authenticate


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
	return render(request, 'login.html')

def entry(request):
	request.session['username']=request.POST['username']
	request.session['password']=request.POST['password']
	return redirect('/userprofile')

def search(request):
	users=User.objects.filter(username__contains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)

@Authenticate.valid_user
def userdashboardview(request):
	return render(request, 'frontend/userdashboard.html')

@Authenticate.valid_user
def userprofileview(request):
	users=User.objects.all()
	return render(request, 'frontend/userprofile.html',{'users':users})

@Authenticate.valid_user
def adminprofileview(request):
	users=User.objects.all()
	return render(request, 'backend/adminprofile.html',{'users':users})

@Authenticate.valid_user
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
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('adminprofile')

@Authenticate.valid_user
def userdetailview(request):
	users=User.objects.all()
	return render(request, 'backend/userDetail.html',{'users':users})

@Authenticate.valid_user
def addclass(request):
	return render(request, 'backend/addclass.html')

@Authenticate.valid_user
def addevent(request):
	return render(request, 'backend/addevent.html')
