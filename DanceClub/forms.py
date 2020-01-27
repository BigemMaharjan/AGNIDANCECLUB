from django import forms
from DanceClub.models.modelsignup import User

class Signupform(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"