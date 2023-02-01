from django.contrib import admin
from .models import Task  # we import the model

# Register your models here.
admin.site.register(Task)
