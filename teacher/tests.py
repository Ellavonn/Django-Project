from django.test import TestCase
import datetime
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse
class AddTeacherTestCase(TestCase):
	def setUp(self):
		self.data={
			"first_name" : "Nyandia",
			"last_name":"Kamawe",
			"gender":"Female",
			"id_number":1234,
			"email" :"nyandia@akirachix.com",
			"phone_number":"0713176657",
			"profession":"trainer",
			"date_employed": datetime.date(2019,2,1),
			"subject_taught":"Design",
		}
		self.bad_data={
			"first_name" : 5,
			"last_name":"Kamawe",
			"gender":"Female",
			"email" :"nyandia@akirachix.com",
			"phone_number":"0713176657",
			"profession":"trainer",
			"date_employed ": datetime.date(2019,2,1),
			"subject_training ":"Design",
			"id_number":"12345",
	   }

	# def test_teacher_form_accepts_valid_data(self):
	# 	form = TeacherForm(self.data)
	# 	self.assertTrue(form.is_valid())

	# def test_teacher_form_rejects_invalid_data(self):
	# 	form=TeacherForm(self.bad_data)
	# 	self.assertFalse(form.is_valid())

	# def test_add_teacher_view(self):
	# 	client = Client() 
	# 	url = reverse("add_teacher")
	# 	response = client.post(url, self.data)
	# 	self.assertEqual(response.status_code, 302)

	# def test_teacher_view_for_bad_data(self):
	# 	client = Client()
	# 	url = reverse("add_teacher")
	# 	response = client.post(url,self.bad_data)
	# 	self.assertEqual(response.status_code, 400)




# Create your tests here.
