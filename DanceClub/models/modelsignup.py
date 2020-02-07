from django.db import models

class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	full_name=models.CharField(max_length=100)
	gaurdian_name=models.CharField(max_length=100)
	date_of_birth=models.CharField(max_length=50)
	classes=models.CharField(max_length=50)
	types=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	email=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=100)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=100)
	class Meta:
		db_table="user"