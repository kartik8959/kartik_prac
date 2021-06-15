from django.db import models
from django.contrib.auth.models import User
from home.models import State,Status,City


# Create your models here.

class PicType(models.Model):
    pic_type=models.CharField(max_length=30)
    
    class Meta:
        db_table="pic_types"

import os
class Institutes(models.Model):
    def get_upload_path(self,filename):
        user=User.objects.get(id=self.user_id)
        upload_path=os.path.join("institutes",user.username,filename)
        print(upload_path)
        return upload_path
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    contact=models.CharField(max_length=10)
    activation_code=models.CharField(max_length=20,null=True)
    status=models.ForeignKey(Status, on_delete=models.SET_NULL,null=True,default=2)
    details=models.TextField()
    address=models.CharField(max_length=200,null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=50,null=True)
    start_date=models.DateField(null=True)
    logo=models.ImageField(upload_to=get_upload_path,null=True)
    
    class Meta:
        db_table="institutes"


class Institute_pic(models.Model):
    def get_upload_path(self,filename):
        user=User.objects.get(id=self.institute_id)
        pic_type_obj=PicType.objects.get(id=self.pictype_id)
        folder=pic_type_obj.pic_type
        upload_path=os.path.join("institutes",user.username,folder,filename)
        return upload_path

    institute=models.ForeignKey(Institutes,on_delete=models.CASCADE)
    pic_path=models.ImageField(upload_to=get_upload_path)
    pictype=models.ForeignKey(PicType,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table="institute_pics"