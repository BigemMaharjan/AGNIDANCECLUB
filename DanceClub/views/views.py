from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from DanceClub.models.createmodel import User
from DanceClub.models.createmodel import Admin
from DanceClub.models.createmodel import Book
from DanceClub.forms import Signupform
from DanceClub.forms import Adminform
from DanceClub.forms import Bookform
from DanceClub.authentication import Authenticate
from DanceClub.authentication import Lock

@Lock.valid_admin
def adminIndexview(request):
	admins=Admin.objects.all()
	return render(request, 'adminIndex.html',{'admins':admins})

@Lock.valid_admin
def createview(request):
	if request.method=="POST":
		structure=Adminform(request.POST,request.FILES)
		structure.save()
		return redirect('index')

	structure=Adminform()
	return render(request, 'create.html',{'structure':structure})

def adminlogin(request):
	return render(request, 'adminlogin.html')

def enter(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect('/admindashboard')

def adminEdit(request,id):
	admin=Admin.objects.get(admin_id=id)
	return render(request, 'adminEdit.html', {'admin': admin})

def adminUpdate(request,id):
	admin=Admin.objects.get(admin_id=id)
	structure=Adminform(request.POST,request.FILES,instance=user)
	structure.save()
	return redirect('adminprofile')

def adminDelete(request,id):
	Admin.objects.get(admin_id=id).image.delete()
	admin=admin.objects.get(admin_id=id)
	admin.delete()
	return redirect('adminprofile')

@Lock.valid_admin
def adminprofileview(request):
	admin=Admin.objects.all()
	return render(request, 'backend/adminprofile.html',{'admin':admin})

@Lock.valid_admin
def admindashboardview(request):
	return render(request, 'backend/admindashboard.html')

@Lock.valid_admin
def viewBooking(request):
	bookclasses=Book.objects.all()
	return render(request, 'backend/viewBooking.html', {'bookclasses':bookclasses})

@Lock.valid_admin
def userdetailview(request):
	limit=3
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "prev" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		users=User.objects.raw("SELECT * FROM user LIMIT 3 offset %s",[offset])
	else:
		users=User.objects.raw("SELECT  * FROM user LIMIT 3 offset 0")
	return render(request, 'backend/userDetail.html',{'users':users, 'page':page})

def search(request):
	users=User.objects.filter(username__contains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)

@Lock.valid_admin
def addevent(request):
	return render(request, 'backend/addevent.html')

def adminlogout(request):
	del request.session['email']
	del request.session['password']
	return redirect('adminlogin')

def indexview(request):
	users=User.objects.all()
	return render(request, 'index.html',{'users':users})

def aboutview(request):
	return render(request, 'about.html')

def whereview(request):
	return render(request, 'where.html')

def signupview(request):	
	if request.method == 'POST':
		form=Signupform(request.POST)
		form.save()
		return redirect('login')

	form=Signupform()
	return render(request, 'signup.html',{'form':form})

def loginview(request):
	return render(request, 'login.html')

def entry(request):
	request.session['username']=request.POST['username']
	request.session['password']=request.POST['password']
	return redirect('/userdashboard')

@Authenticate.valid_user
def userdashboardview(request):
	return render(request, 'frontend/userdashboard.html')

@Authenticate.valid_user
def userBooking(request):
	if request.method == 'POST':
		reserve=Bookform(request.POST)
		reserve.save()
		return redirect('userdashboard')

	reserve=Bookform()
	return render(request, 'frontend/userBooking.html', {'reserve':reserve})

# @Authenticate.valid_user
def userprofileview(request, username="request.session.username"):
	user=User.objects.get(username=username)
	return render(request, 'frontend/userprofile.html',{'user':user})

def edit(request,id):
	user=User.objects.get(user_id=id)
	return render(request, 'edit.html', {'user': user})

def update(request,id):
	user=User.objects.get(user_id=id)
	form=Signupform(request.POST,instance=user)
	form.save()
	return redirect('userprofile')

def delete(request,id):
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('userprofile')

def logout(request):
	del request.session['username']
	del request.session['password']
	return redirect('login')


