# Generated by Django 3.1.3 on 2020-12-05 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201203_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]