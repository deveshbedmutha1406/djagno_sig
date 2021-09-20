from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    phone_no = models.CharField(max_length=10)
    #onetoonerealtion
    #models.cascade deletes data if user deleted
    gender = models.CharField(max_length=50,null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_no

