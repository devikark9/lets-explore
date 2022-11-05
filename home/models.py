from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    destination = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
