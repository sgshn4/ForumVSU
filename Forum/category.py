from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name