# Generated by Django 3.1.3 on 2021-01-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_blogpost_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-publish',)},
        ),
    ]
