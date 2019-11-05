from django.test import TestCase
from .models import Student
import datetime
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse



class StudentTestCase(TestCase):
	def setUp(self):
		self.student=Student(
			first_name="Stella",
			last_name="Njeri",
			date_of_birth=datetime.date(1999,3,30),
			gender="Female",
			registration_number="1234",
			email="snjeri6@gmail.com",
			phone_number="0713174435",
			date_joined=datetime.date.today(),
			)
	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())
	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

	def test_age_is_always_above_17(self):
		self.assertFalse(self.student.get_age() <17 )

	def test_age_ias_always_below_30(self):
		self.assertFalse(self.student.get_age() > 30)

	
class AddStudentTestCase(TestCase):
	def setUp(self):
		self.data={
			"first_name":"Stella",
			"last_name":"Njeri",
			"date_of_birth":datetime.date(1999,3,30),
			"gender":"Female",
			"registration_number":"1234",
			"email":"snjeri6@gmail.com",
			"phone_number":"0713174435",
			"date_joined":datetime.date.today()
		}

		self.bad_data = {
			"first_name":"Stella",
			"last_name":"Njeri",
			"date_of_birth":datetime.date(1999,3,30),
			"gender":"Female",
			"registration_number":"1234",
			"email":"snjeri6gmail.com",
			"phone_number":"0713174435",
			"date_joined":datetime.date.today()
		}

	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_student_view(self):
		client = Client() 
		url = reverse("add_student")
		response = client.post(url, self.data)
		self.assertEqual(response.status_code, 302)

	def test_student_form_for_bad_data(self):
		client = Client()
		url = reverse("add_student")
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code, 400)





			
      	
      	

    


      





# Create your tests /here.
