from django.db import models
from datetime import datetime, date
from multiselectfield import MultiSelectField
from django.urls import reverse


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
        return f"{self.body[:50]}..."

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
