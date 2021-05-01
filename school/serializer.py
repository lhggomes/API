from rest_framework import serializers
from school.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class ListEnrollmentsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    @staticmethod
    def get_period(obj):
        return obj.get_period_display()


