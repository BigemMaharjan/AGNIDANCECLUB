"""AgniDanceClub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DanceClub.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.indexview, name='home'),
    path('aboutus/', views.aboutview, name='aboutus'),
    path('where/', views.whereview, name='where'),
    path('login/', views.loginview, name='login'),
    path('entry', views.entry, name='entry'),
    path('signup/',views.signupview, name='signup'),
    path('index/', views.adminIndexview, name='index'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('enter', views.enter, name='enter'),
    path('adminsearch', views.adminsearch, name='adminsearch'),
    path('create/', views.createview, name='create'),
    path('adminEdit/<int:id>', views.adminEdit, name='adminEdit'),
    path('adminUpdate/<int:id>', views.adminUpdate, name='adminUpdate'),
    path('adminDelete/<int:id>', views.adminDelete, name="adminDelete"),
    path('userDetail/', views.userdetailview, name='userDetail'),
    path('search',views.search, name='search'),
    path('viewBooking/', views.viewBooking, name='viewBooking'),
    path('addevent/', views.addevent, name='addevent'),
    path('eventEdit/<int:id>', views.eventEdit, name='eventEdit'),
    path('eventUpdate/<int:id>', views.eventUpdate, name='eventUpdate'),
    path('eventDelete/<int:id>', views.eventDelete, name='eventDelete'),
    path('viewevent/', views.viewevent, name='viewevent'),
    path('sets/', views.sets, name='sets'),
    path('setUpdate/<int:id>', views.setUpdate, name='setUpdate'),
    path('setEdit/<int:id>', views.setEdit, name='setEdit'),
    path('setDelete/<int:id>', views.setDelete, name='setDelete'),
    path('adminprofile/<str:name>', views.adminprofileview, name='adminprofile'),
    path('admindashboard/', views.admindashboardview, name='admindashboard'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('userdashboard/', views.userdashboardview, name='userdashboard'),
    path('userBooking/', views.userBooking, name='userBooking'),
    path('yourBooking/', views.yourBooking, name='yourBooking'),
    path('viewTimeDate/', views.viewTimeDate, name='viewTimeDate'),
    path('bookEdit/<int:id>', views.bookEdit, name='bookEdit'),
    path('bookUpdate/<int:id>', views.bookUpdate, name='bookUpdate'),
    path('bookDelete/<int:id>', views.bookDelete, name='bookDelete'),
    path('userprofile/<str:username>', views.userprofileview, name='userprofile'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout/', views.logout, name='logout')
]
