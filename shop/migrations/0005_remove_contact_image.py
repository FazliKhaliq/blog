# Generated by Django 3.1.3 on 2020-12-09 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]
