# Generated by Django 5.1 on 2024-09-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_review_date_review_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='cat_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cat_name',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
