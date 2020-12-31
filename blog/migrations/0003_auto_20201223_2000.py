# Generated by Django 3.1.4 on 2020-12-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
    ]
