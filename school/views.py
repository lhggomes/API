from django.http import JsonResponse
from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, \
    ListEnrollmentsStudentSerializer


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


class ListEnrollmentsStudent(generics.ListAPIView):
    """
    Listing the enrollments of a student
    """
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListEnrollmentsStudentSerializer

