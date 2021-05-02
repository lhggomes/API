import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.settings')
django.setup()

import random
from faker import Faker
from validate_docbr import CPF

from school.models import Student, Course


def creating_students(persons: int):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(persons):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999),
                               random.randrange(0, 9))
        cpf = cpf.generate()
        birth_date = fake.date_between(start_date='-18y', end_date='today')
        print(f'Generating student: {name}')
        a = Student(name=name, rg=rg, cpf=cpf, birth_date=birth_date, active=True)
        a.save()


def creating_courses(courses: int):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(courses):
        code = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99), random.randrange(1, 9))
        desc = ['Python Fundamentals', 'Python Intermediate', 'Python Advanced', 'Python for  Data Science',
                'Python/React', 'Java Enterprise Edition', 'Java Swing']
        description = random.choice(desc)
        desc.remove(description)
        level = random.choice("BIA")
        print(f'Generating course: {description}')
        c = Course(code=code, description=description, level=level)
        c.save()


creating_students(200)
creating_courses(5)
