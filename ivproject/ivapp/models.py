from django.db import models

# Create your models here.
class IVModel(models.Model):
    Mname = models.CharField(max_length=20)