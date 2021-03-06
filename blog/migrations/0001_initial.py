# Generated by Django 3.1.3 on 2020-12-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('tilte', models.CharField(max_length=50)),
                ('heading0', models.CharField(default='', max_length=500)),
                ('heading0_content', models.CharField(default='', max_length=5000)),
                ('heading1', models.CharField(default='', max_length=500)),
                ('heading1_content', models.CharField(default='', max_length=5000)),
                ('heading2', models.CharField(default='', max_length=500)),
                ('heading2_content', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
