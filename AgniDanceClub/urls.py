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
    path('entry/', views.entry, name='entry'),
    path('signup/',views.signupview, name='signup'),
    path('userdashboard/', views.userdashboardview, name='userdashboard'),
    path('userprofile/', views.userprofileview, name='userprofile'),
    path('adminprofile/', views.adminprofileview, name='adminprofile'),
    path('admindashboard/', views.admindashboardview, name='admindashboard'),
    path('search',views.search, name='search'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('userDetail/', views.userdetailview, name='userDetail'),
    path('addclass/', views.addclass, name='addclass'),
    path('addevent/', views.addevent, name='addevent'),
    path('logout/', views.logout, name='logout')
]
