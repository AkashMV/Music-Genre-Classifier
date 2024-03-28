from django.db import models

# Create your models here.

class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to="audi_files/")
