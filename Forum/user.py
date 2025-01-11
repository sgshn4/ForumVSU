from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField(default=0)
    nickname = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    avatar = models.TextField(max_length=500)
    login = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    def __str__(self):
        return self.nickname