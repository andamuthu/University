# Generated by Django 3.0.5 on 2020-04-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students_details', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, unique=True)),
                ('Tamil', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Maths', models.IntegerField()),
                ('Science', models.IntegerField()),
                ('Socialscience', models.IntegerField()),
                ('Total_Marks', models.IntegerField()),
            ],
        ),
    ]