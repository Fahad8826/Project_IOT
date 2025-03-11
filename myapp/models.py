from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length= 200)
    phone=models.CharField(max_length=10)
    Status=models.BooleanField(default=False)

    def __str__(self):
        return  self.username
