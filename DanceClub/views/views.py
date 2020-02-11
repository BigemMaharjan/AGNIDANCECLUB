from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from DanceClub.models.createmodel import User
from DanceClub.models.createmodel import Admin
from DanceClub.models.createmodel import Book
from DanceClub.models.createmodel import Event
from DanceClub.forms import Signupform
from DanceClub.forms import Adminform
from DanceClub.forms import Bookform
from DanceClub.forms import Eventform
from DanceClub.authentication import Authenticate
from DanceClub.authentication import Lock

# /*--------------------------------------------------------------
# ADMIN
# --------------------------------------------------------------*/
@Lock.valid_admin
def adminIndexview(request):
	limit=3
	pages=1
	if request.method=="POST":
		if "next" in request.POST:
			pages=(int(request.POST['pages'])+1)
		elif "prev" in request.POST:
			pages=(int(request.POST['pages'])-1)
		tempoffset=pages-1
		offset=tempoffset*pages
		admins=Admin.objects.raw("SELECT * FROM admin LIMIT 3 offset %s",[offset])
	else:
		admins=Admin.objects.raw("SELECT  * FROM admin LIMIT 3 offset 0")
	return render(request, 'backend/adminIndex.html',{'admins':admins, 'pages':pages})

def adminsearch(request):
	admins=Admin.objects.filter(name__contains=request.GET['adminsearch']).values()
	return JsonResponse(list(admins),safe=False)

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
	request.session['name']=request.POST['name']
	request.session['password']=request.POST['password']
	return redirect('/admindashboard')

# @Lock.valid_admin
def adminprofileview(request, name="request.session.name"):
	admin=Admin.objects.get(name=name)
	return render(request, 'backend/adminprofile.html',{'admin':admin})

@Lock.valid_admin
def admindashboardview(request):
	return render(request, 'backend/admindashboard.html')

# @Lock.valid_admin
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

# /*--------------------------------------------------------------
# ADMIN CRUD
# --------------------------------------------------------------*/

def adminEdit(request,id):
	admin=Admin.objects.get(admin_id=id)
	return render(request, 'adminEdit.html', {'admin': admin})

def adminUpdate(request,id):
	admin=Admin.objects.get(admin_id=id)
	structure=Adminform(request.POST,request.FILES,instance=admin)
	structure.save()
	return redirect('admindashboard')

def adminDelete(request,id):
	Admin.objects.get(admin_id=id).image.delete()
	admin=admin.objects.get(admin_id=id)
	admin.delete()
	return redirect('admindashboard')

# /*--------------------------------------------------------------
# EVENT CRUD
# --------------------------------------------------------------*/

@Lock.valid_admin
def addevent(request):
	if request.method == "POST":
		program=Eventform(request.POST)
		program.save()
		return redirect('admindashboard')

	program=Eventform()
	return render(request, 'backend/addevent.html', {'program':program})

def viewevent(request):
	events=Event.objects.all()
	return render(request, 'frontend/viewevent.html', {'events':events})

def eventEdit(request,id):
	event=Event.objects.get(event_id=id)
	return render(request, 'eventEdit.html', {'event': event})

def eventUpdate(request,id):
	event=Event.objects.get(event_id=id)
	program=Eventform(request.POST,instance=event)
	program.save()
	return redirect('admindashboard')

def eventDelete(request,id):
	event=Event.objects.get(event_id=id)
	event.delete()
	return redirect('admindashboard')


# /*--------------------------------------------------------------
# ADMIN LOGOUT
# --------------------------------------------------------------*/

def adminlogout(request):
	del request.session['name']
	del request.session['password']
	return redirect('adminlogin')

# /*--------------------------------------------------------------
# FRONTPAGE
# --------------------------------------------------------------*/

def indexview(request):
	users=User.objects.all()
	return render(request, 'index.html',{'users':users})

def aboutview(request):
	return render(request, 'about.html')

def whereview(request):
	return render(request, 'where.html')

# /*--------------------------------------------------------------
# USER
# --------------------------------------------------------------*/

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
	if request.method == "POST":
		reserve=Bookform(request.POST)
		reserve.save()
		return redirect('userdashboard')

	reserve=Bookform()
	return render(request, 'frontend/userBooking.html', {'reserve':reserve})

# def book()

# @Authenticate.valid_user
def userprofileview(request, username="request.session.username"):
	user=User.objects.get(username=username)
	return render(request, 'frontend/userprofile.html',{'user':user})

# /*--------------------------------------------------------------
# USER CRUD
# --------------------------------------------------------------*/

def edit(request,id):
	user=User.objects.get(user_id=id)
	return render(request, 'edit.html', {'user': user})

def update(request,id):
	user=User.objects.get(user_id=id)
	form=Signupform(request.POST,instance=user)
	form.save()
	return redirect('userdashboard')

def delete(request,id):
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('userdashboard')

# /*--------------------------------------------------------------
# USER LOGOUT
# --------------------------------------------------------------*/

def logout(request):
	del request.session['username']
	del request.session['password']
	return redirect('login')


