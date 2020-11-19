from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_desi=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    email=models.EmailField(default='test@ecpl.com',null=True)


    def __str__(self):
        return self.user.username



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

    opening_1=models.CharField(max_length=10)
    opening_2=models.CharField(max_length=10)

    softskill_1=models.CharField(max_length=10)
    softskill_2 = models.CharField(max_length=10)
    softskill_3 = models.CharField(max_length=10)
    softskill_4 = models.CharField(max_length=10)
    softskill_5 = models.CharField(max_length=10)
    softskill_6 = models.CharField(max_length=10)

    business_1=models.CharField(max_length=10)
    business_2 = models.CharField(max_length=10)
    business_3 = models.CharField(max_length=10)

    closing_1=models.CharField(max_length=10)
    closing_2 = models.CharField(max_length=10)

    compliance_1=models.CharField(max_length=10)
    compliance_2 = models.CharField(max_length=10)
    compliance_3 = models.CharField(max_length=10)

    total_score=models.IntegerField(null=True)
    compliance=models.IntegerField(null=True)

    opening_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    closing_total=models.IntegerField(null=True)
    compliance_total=models.IntegerField(null=True)

    areas_improvement = models.TextField()
    positives=models.TextField()
    comments=models.TextField()
    added_by=models.CharField(max_length=30)
    status=models.BooleanField(default=False)
    closed_date=models.DateField(null=True)


    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100]+'...'



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

    opening_1=models.CharField(max_length=10)
    opening_2=models.CharField(max_length=10)

    softskill_1=models.CharField(max_length=10)
    softskill_2 = models.CharField(max_length=10)
    softskill_3 = models.CharField(max_length=10)
    softskill_4 = models.CharField(max_length=10)
    softskill_5 = models.CharField(max_length=10)
    softskill_6 = models.CharField(max_length=10)

    business_1=models.CharField(max_length=10)
    business_2 = models.CharField(max_length=10)
    business_3 = models.CharField(max_length=10)

    closing_1=models.CharField(max_length=10)
    closing_2 = models.CharField(max_length=10)

    compliance_1=models.CharField(max_length=10)
    compliance_2 = models.CharField(max_length=10)
    compliance_3 = models.CharField(max_length=10)

    total_score=models.IntegerField(null=True)
    compliance=models.IntegerField(null=True)

    opening_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    closing_total=models.IntegerField(null=True)
    compliance_total=models.IntegerField(null=True)

    areas_improvement = models.TextField()
    positives=models.TextField()
    comments=models.TextField()
    added_by=models.CharField(max_length=30)
    status=models.BooleanField(default=False)
    closed_date=models.DateField(null=True)


    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100]+'...'


class InboundMonitoringForm(models.Model):
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

    opening_1=models.CharField(max_length=10)
    opening_2=models.CharField(max_length=10)

    softskill_1=models.CharField(max_length=10)
    softskill_2 = models.CharField(max_length=10)
    softskill_3 = models.CharField(max_length=10)
    softskill_4 = models.CharField(max_length=10)
    softskill_5 = models.CharField(max_length=10)
    softskill_6 = models.CharField(max_length=10)

    business_1=models.CharField(max_length=10)
    business_2 = models.CharField(max_length=10)
    business_3 = models.CharField(max_length=10)

    closing_1=models.CharField(max_length=10)
    closing_2 = models.CharField(max_length=10)

    compliance_1=models.CharField(max_length=10)
    compliance_2 = models.CharField(max_length=10)
    compliance_3 = models.CharField(max_length=10)

    total_score=models.IntegerField(null=True)
    compliance=models.IntegerField(null=True)

    opening_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    closing_total=models.IntegerField(null=True)
    compliance_total=models.IntegerField(null=True)

    areas_improvement = models.TextField()
    positives=models.TextField()
    comments=models.TextField()
    added_by=models.CharField(max_length=30)
    status=models.BooleanField(default=False)
    closed_date=models.DateField(null=True)


    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100]+'...'
