# Generated by Django 5.1 on 2024-09-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanme', models.CharField(max_length=100)),
                ('sclass', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
