# Generated by Django 3.1.3 on 2021-01-03 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_blogpost_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
