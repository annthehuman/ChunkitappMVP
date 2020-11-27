from django.db import models
from django.conf import settings
# Create your models here.

class sess(models.Model):
    session_key = models.CharField(max_length=40)

class Meta:
    unique_together = ('session_key',)