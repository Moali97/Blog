from django.db import models
from datetime import datetime, date
from multiselectfield import MultiSelectField
from django.urls import reverse
from django.forms import Textarea


class Post(models.Model):
    genre = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)  # self

    def __str__(self):
        return f"{self.body[:50]}..."

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
