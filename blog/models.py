from django.db import models
from datetime import datetime, date
from multiselectfield import MultiSelectField

class Post(models.Model):
    SUBJECT_CHOICES = (
        ('tech', 'Technology'),
        ('finance', 'Financial'),
        ('cons', 'Consumer'),
        ('cyber', 'Cybersecurity'),
    )
    genre = MultiSelectField(choices=SUBJECT_CHOICES, default='DEFAULT VALUE')

    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30, default='DEFAULT VALUE')
    last_name = models.CharField(max_length=30, default='DEFAULT VALUE')
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)






    def __str__(self):
        return self.title

