from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, \
    ListEnrollmentsStudentSerializer, ListStudentEnrolledSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """
    Show all Students
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Show all Courses
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    Show all enrollments
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListEnrollmentsStudent(generics.ListAPIView):
    """
    Listing the enrollments of a student
    """

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListEnrollmentsStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListStudentsEnrolled(generics.ListAPIView):
    """
    Listing all enrolled students
    """

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course__id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentEnrolledSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
