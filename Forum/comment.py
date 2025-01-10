from django.db import models
from django.contrib.auth.models import User
from . import post

class Comment(models.Model):
    post = models.ForeignKey(post.Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'