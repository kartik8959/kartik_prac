from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    status=models.CharField(max_length=20)

    class Meta:
        db_table="status"

class Institutes(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    contact=models.CharField(max_length=10)
    activation_code=models.CharField(max_length=20,null=True)
    status=models.ForeignKey(Status, on_delete=models.SET_NULL,null=True,default=2)
    class Meta:
        db_table="institutes"
