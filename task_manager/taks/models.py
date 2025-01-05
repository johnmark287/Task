from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(maxlength=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
