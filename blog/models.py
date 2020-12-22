from django.db import models
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
       'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
