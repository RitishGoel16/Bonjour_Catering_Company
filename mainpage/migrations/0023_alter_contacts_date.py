# Generated by Django 5.0.4 on 2024-05-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0022_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateField(default=0),
        ),
    ]