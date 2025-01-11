from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    content_id = models.IntegerField(primary_key=True)
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE)
    url = models.TextField()
    type = models.TextField(50)


    def __str__(self):
        return self.url