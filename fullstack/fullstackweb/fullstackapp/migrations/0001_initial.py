# Generated by Django 5.1 on 2024-09-06 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.CharField(max_length=30)),
                ('LocationName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('TitleName', models.CharField(max_length=30)),
                ('HasPassport', models.BooleanField()),
                ('Salary', models.IntegerField()),
                ('BirthDate', models.DateField()),
                ('HireDate', models.DateField()),
                ('Notes', models.CharField(max_length=30)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('PhoneNumber', models.CharField(default='', max_length=30)),
                ('EmpCountry', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='fullstackapp.country')),
                ('EmpDepartment', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='fullstackapp.department')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
