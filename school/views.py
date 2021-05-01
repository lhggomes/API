from django.http import JsonResponse
from rest_framework import viewsets
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """
    Show all Students
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Show all Courses
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    Show all enrollments
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

