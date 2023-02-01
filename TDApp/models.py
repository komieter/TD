from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)  #this is the description for the task
    completed = models.BooleanField(default=True)  #thiis shows wether the task is done or not
    
    def __str__(self):
        return self.task
    
    def add_url(self):
        return reverse('add')
    
    
    