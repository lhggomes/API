from rest_framework import serializers
from school.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    @staticmethod
    def validate_cpf(cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("The CPF must have 11 digits")
        return cpf

    @staticmethod
    def validate_name(name):
        if not name.isalpha():
            raise serializers.ValidationError("Do not include numbers in this field")
        return name

    @staticmethod
    def validate_rg(rg):
        if len(rg) != 9:
            raise serializers.ValidationError("RG Number must have 9 digits")
        return rg


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


class ListStudentEnrolledSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrollment
        fields = ['student_name']
