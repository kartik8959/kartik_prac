from django.db import models

# Create your models here.

class State(models.Model):
    state=models.CharField(max_length=35)

    def __str__(self):
        return self.state
    class Meta:
        db_table="states"



class Status(models.Model):
    status=models.CharField(max_length=20)

    class Meta:
        db_table="status"


class City(models.Model):
    city=models.CharField(max_length=25)
    state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    
    

    class Meta:
        db_table="cities"

