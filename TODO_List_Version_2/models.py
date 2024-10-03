from django.db import models

# Create your models here.
class Tasks(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    Task = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.Task
    