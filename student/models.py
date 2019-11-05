from django.db import models
from course.models import Course
import datetime
from django.core.exceptions import  ValidationError

# Create your models here.
#Note the conventions
#CharField is a class inside the models thingie.
#max_length is not always required.
#Include this app in the settings.py file as part of the INSTALLED APPS - to make the app discoverable by django.
#This enables it to be converted into a database table.

# from .models import Student
# admin.site.register(Student)

#The two above are to be added to admin.py
class Student(models.Model) :  #Inheritance of attributes of another class. Model class in models.
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()  #Empty brackets because date formats are standard. No need for length declaration.
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 20)
	date_joined = models.DateField()
	courses = models.ManyToManyField(Course, blank=True, related_name = "students")
	image = models.ImageField(upload_to = "profile_pictures", blank = True)

	def __str__(self):
		return self.first_name

	def full_name(self):
		return "{} {}".format(self.first_name,self.last_name)

	def get_age(self):
		today = datetime.date.today()
		return today.year - self.date_of_birth.year - ((today.month,today.day) < (self.date_of_birth.month, self.date_of_birth.day))

	age = property( get_age)
	def clean(self):
		age = self.age
		if age < 18 or age > 30 :
			raise ValidationError("You cant")

