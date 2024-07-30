# Generated by Django 5.0.4 on 2024-05-17 07:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0021_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('date', models.DateField(auto_now=True)),
                ('review', ckeditor.fields.RichTextField()),
                ('message', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
