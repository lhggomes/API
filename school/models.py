from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=300)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    email = models.EmailField(default="test@getnada.com")
    phone = models.CharField(max_length=13, default="1")
    active = models.BooleanField(default=True)

    ordering = ('name',)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = [
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')

    ]
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description


class Enrollment(models.Model):
    PERIOD = [
        ('M', 'Morning'),
        ('E', 'Evening'),
        ('N', 'Night')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')
