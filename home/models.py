from django.db import models
from datetime import date


# Create your models here.
"""
class Registration(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date = models.DateField()
    # Timezone default="timezone.now", editable=False
    #to change the title - contact object1  in database admin site
    #below function is responsible to display the name of the person
    def __str__(self):
        return self.fullname
""" 
