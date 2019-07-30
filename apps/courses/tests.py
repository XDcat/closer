from django.test import TestCase

# Create your tests here.
from courses.models import Course


class CourseModelTests(TestCase):

    def test_course_teacher(self):
        all_course = Course.objects.all()
        for i_course in all_course:
            print(i_course)


# if __name__ == '__main__':
#     all_course = Course.objects.all()
#     for i_course in all_course:
#         print(i_course)
