from django import forms
from DanceClub.models.createmodel import User
from DanceClub.models.createmodel import Admin
from DanceClub.models.createmodel import Book
from DanceClub.models.createmodel import Event


class Signupform(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"

class Adminform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Admin
		fields="__all__"

class Bookform(forms.ModelForm):
	class Meta:
		model=Book
		fields="__all__"

class Eventform(forms.ModelForm):
	class Meta:
		model=Event
		fields="__all__"