# Generated by Django 3.1.4 on 2020-12-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('tech', 'Technology'), ('finance', 'Financial'), ('cons', 'Consumer'), ('cyber', 'Cybersecurity')], default='DEFAULT VALUE', max_length=25),
        ),
    ]
