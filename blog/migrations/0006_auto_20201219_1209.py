# Generated by Django 3.1.3 on 2020-12-19 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201218_0401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='content_0',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='heading0',
            new_name='heading',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='content_1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='content_2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='heading1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='heading2',
        ),
    ]
