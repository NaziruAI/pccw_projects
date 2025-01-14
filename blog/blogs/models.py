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

class Comment(models.Model):
    text = models.TextField()  # Updated to use 'text'
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]  # Show the first 20 characters of the text