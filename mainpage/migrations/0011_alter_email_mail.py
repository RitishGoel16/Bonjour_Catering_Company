# Generated by Django 4.2.2 on 2023-11-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='mail',
            field=models.CharField(max_length=50),
        ),
    ]
