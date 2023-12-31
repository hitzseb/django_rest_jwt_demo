from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharField(max_length=200)
    date = models.DateTimeField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
