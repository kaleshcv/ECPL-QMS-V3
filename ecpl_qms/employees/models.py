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
    status=models.BooleanField(default=False)
    date=models.DateField(default="2020-01-01")




class Team(models.Model):
    name=models.CharField(max_length=50)
    mgr=models.ForeignKey(User,on_delete=models.CASCADE,related_name='mgr')
    qa=models.ForeignKey(User,on_delete=models.CASCADE,related_name='qa')


class OutboundMonitoringForm(models.Model):
    associate_name=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name=models.CharField(max_length=50)
    customer_contact=models.IntegerField()
    call_date=models.DateField()
    audit_date = models.DateField()
    campaign=models.CharField(max_length=100)
    zone=models.CharField(max_length=60)
    concept=models.CharField(max_length=60)
    call_duration=models.IntegerField()
    opening_1=models.IntegerField()
    opening_2=models.IntegerField()
    softskill_1=models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    softskill_6 = models.IntegerField()
    business_1=models.IntegerField()
    business_2 = models.IntegerField()
    business_3 = models.IntegerField()
    closing_1=models.IntegerField()
    closing_2 = models.IntegerField()
    compliance_1=models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    total_score=models.IntegerField()
    compliance=models.IntegerField()
    areas_improvement=models.TextField()
    opening_total=models.IntegerField()
    softskill_total=models.IntegerField()
    business_total=models.IntegerField()
    closing_total=models.IntegerField()
    compliance_total=models.IntegerField()
    positives=models.TextField()
    comments=models.TextField()







