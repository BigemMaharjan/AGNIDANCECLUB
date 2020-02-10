from django.db import models

class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	full_name=models.CharField(max_length=100)
	gaurdian_name=models.CharField(max_length=100)
	date_of_birth=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	email=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=100)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=100)
	class Meta:
		db_table="user"

class Admin(models.Model):
	admin_id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	gender=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="admin"

class Book(models.Model):
	booking_id=models.AutoField(auto_created=True,primary_key=True)
	student_name=models.CharField(max_length=100)
	class_types=models.CharField(max_length=100)
	class_shift=models.CharField(max_length=100)
	booking_date=models.CharField(max_length=100)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		db_table="bookclass"