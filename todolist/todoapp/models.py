from django.db import models
from datetime import datetime
# Create your models here.
status_choice = [('1','In progress'), ('2','completed'), ('3','pending')]

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_at = models.DateTimeField(default = datetime.now)
    status = models.CharField(max_length=30, choices=status_choice, default='pending')

    def __str__(self):
        return self.title
