from django.db import models
from django.contrib.auth.models import User

class TopicInCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
