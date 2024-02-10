from django.db import models
import datetime


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 2000)
    description = models.TextField(default = 'N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now= True, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.name}" 
