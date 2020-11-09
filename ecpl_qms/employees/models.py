from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_desi=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    email=models.EmailField()



    def __str__(self):
        return self.user.username

class Coaching(models.Model):
    ticket_no=models.IntegerField()
    feedback=models.TextField()
    agent=models.CharField(max_length=50)
    qa=models.CharField(max_length=50)
    status=models.BooleanField(default=True)



class Team(models.Model):
    name=models.CharField(max_length=50)
    mgr=models.ForeignKey(User,on_delete=models.CASCADE,related_name='mgr')
    qa=models.ForeignKey(User,on_delete=models.CASCADE,related_name='qa')
