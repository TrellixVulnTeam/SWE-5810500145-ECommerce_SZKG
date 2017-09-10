from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='description default text')
    location = models.CharField(max_length=128,default='my location default text',blank=True,null=True)
    job = models.CharField(max_length=128,null=True)
    
    def __str__(self):
        return self.name