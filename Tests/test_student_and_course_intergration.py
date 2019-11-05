from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime

class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(
			first_name="Stella",
			last_name="Njeri",
			id= 32363024,
			date_of_birth=datetime.date(1999,3,30),
			gender="Female",
			registration_number="1234",
			email="snjeri6@gmail.com",
			phone_number="0713174435",
			date_joined=datetime.date.today(),


			)
		self.student_b = Student.objects.create(
			first_name="Luciana",
			last_name="Wambui",
			id = 2358758,
			date_of_birth=datetime.date(1999,3,30),
			gender="Female",
			registration_number="1234",
			email="luciana@gmail.com",
			phone_number="0705193357",
			date_joined=datetime.date.today(),

			)
		self.python = Course.objects.create(
			name ="python",
           	duration_in_months=10,
            start_date=datetime.date(2019,2,1),
            end_date=datetime.date(2019,12,1),
            course_description="Database",

			)
		self.design = Course.objects.create(
			name="design",
            duration_in_months=10,
            start_date=datetime.date(2019,2,1),
            end_date=datetime.date(2019,12,1),
            course_description="Graphic Design",

			)
		self.electronics = Course.objects.create(
			name="electronics",
            duration_in_months=10,
            start_date=datetime.date(2019,2,1),
            end_date=datetime.date(2019,12,1),
            course_description="arduino",

			)
	def test_student_can_join_a_course(self):
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.design)
		self.assertEqual(self.student_a.courses.count(),2)
		self.student_a.courses.add(self.electronics)
		self.assertEqual(self.student_a.courses.count(),3)

	def test_student_can_add_multiple_courses(self):
		self.student_b.courses.add(self.python, self.design,self.electronics)
		self.assertEqual(self.student_b.courses.count(),3)




