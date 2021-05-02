from rest_framework import serializers
from school.models import *
from school.validators import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': "The CPF is invalid"})

        if not name_valid(data['name']):
            raise serializers.ValidationError({'name': "Do not include numbers in this field"})

        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': "RG Number must have 9 digits"})

        if not phone_valid(data['phone']):
            raise serializers.ValidationError({'phone': "The phone number must have this pattern: 11 91234-1234"})
        return data


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
