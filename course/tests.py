from django.test import TestCase
import datetime
from course.forms import CourseForm

class AddCourseTestCase(TestCase):
	def setUp(self):
		self.data={
			"name":"Design",
			"duration_in_months":10,
			"start_date":datetime.date(2019,2,1),
			"end_date":datetime.date(2019,12,1),
			"course_description":"Graphic Design",
		}
		self.bad_data={
			"name":"Design",
			"duration_in_months":10,
			"start_date":datetime.date(2019,2,1),
			"end_date":"done",
			"course_description":"Graphic Design",
			"teacher":"Nyandia Kamawe",
		}
	def test_course_form_accepts_valid_data(self):
		form = CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form=CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_course_view(self):
		client = Client() 
		url = reverse("add_course_view")
		response = client.post(url, self.data)
		self.assertEqual(response.status_code, 302)

	def test_course_form_for_bad_data(self):
		client = Client()
		url = reverse("add_course_view")
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code, 400)




# Create your tests here.
