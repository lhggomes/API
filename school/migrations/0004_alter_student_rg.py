# Generated by Django 3.2 on 2021-05-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rg',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
