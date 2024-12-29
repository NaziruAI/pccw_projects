from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """A blog post"""
    title = models.CharField(max_length=200)
    text = models.TextField()  # Changed to TextField to allow long content
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
