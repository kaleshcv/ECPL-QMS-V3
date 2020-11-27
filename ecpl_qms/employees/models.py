from django.db import models
from django.contrib.auth.models import User
import pandas as pd


# Create your models here.
class Profile(models.Model):
    team_list=(
        ('Noom','Noom'),('Aadya Solutions','Aadya Solutions'),('UPS CLP','UPS CLP'),('Gardening Express','Gardening Express'),
        ('Maxwell Properties','Maxwell Properties'),('Gubagoo','Gubagoo'),('Digital Swiss Gold','Digital Swiss Gold'),
        ('Digital Signage','Digital Signage'),('Success Systems','Success Systems'),('Advancement Consulting ','Advancement Consulting'),
        ('Insalvage','Insalvage'),('Medicare','Medicare'),('Printerpix','Printerpix'),('Printerpix Training','Printerpix Training'),
        ('First Look Appraisal','First Look Appraisal'),('TCA Counseling Group','TCA Counseling Group'),('Advit Sahdev Marketing','Advit Sahdev Marketing'),
        ('AKDY','AKDY'),('AKDY Training','AKDY Training'),('Monster Lead Group','Monster Lead Group'),('Fame House','Fame House'),
        ('Lecanto Green coffee','Lecanto Green coffee'),('Micro Distributing','Micro Distributing'),('Aditya Birla','Aditya Birla'),
        ('Aditya Birla Cellulose','Aditya Birla Cellulose'),('Aditya Birla Cellulose Training','Aditya Birla Cellulose Training'),
        ('City Security Services','City Security Services'),('Active Sports Club','Active Sports Club'),('Aditya Birla Sampling Team','Aditya Birla Sampling Team'),
        ('Aditya Birla Sampling Team Trainig','Aditya Birla Sampling Team Trainig'),('Bigo - IMO Group Chat','Bigo - IMO Group Chat'),
        ('Bigo Monitor Team','Bigo Monitor Team'),('Daniel Wellington','Daniel Wellington'),('Option Matrix','Option Matrix'),
        ('Info Think LLC','Info Think LLC'),('MT Cosmetics','MT Cosmetics'),("Something's Brewing","Something's Brewing"),
        ('WIT Digital','WIT Digital'),('Sync Treasury LLC','Sync Treasury LLC'),('SANA GAMING CONSULTING','SANA GAMING CONSULTING'),
        ('GrayStone LLC','GrayStone LLC'),('Kaapi Machines','Kaapi Machines'),('Richmond Assets & Holdings','Richmond Assets & Holdings'),
        ('US Home Exterior','US Home Exterior'),('Pre Management Leicester LTD','Pre Management Leicester LTD'),('American Income Life','American Income Life'),
        ('Life Alarm Services','Life Alarm Services'),('ERI Global','ERI Global'),('Allen Consulting group','Allen Consulting group'),
        ('Jeffery Tan ','Jeffery Tan '),('Student Life','Student Life'),('Career Transition Specialist','Career Transition Specialist'),
        ('Golden Eye Tech CCTV','Golden Eye Tech CCTV'),('MOVEMENT INSURANCE','MOVEMENT INSURANCE'),('Nucleus Media','Nucleus Media'),
        ('PSECU','PSECU'),('Tentamus','Tentamus'),('L&D','L&D'),('Get A Rate','Get A Rate'),('Mayfair Acct and Wealth','Mayfair Acct and Wealth'),
        ('Superking','Superking'),('Millionaires Group','Millionaires Group'),('PROTOSTAR','PROTOSTAR'),('MESSE FRANKFURT','MESSE FRANKFURT'),
        ('System 4','System 4'),('Naffa Innovations Pvt Ltd','Naffa Innovations Pvt Ltd'),('Support Staff','Support Staff')

                    )

    emp_desi_list=(
        ('CRO','CRO'),('Patrolling officer','Patrolling officer'),('TL','TL'),('AM','AM'),('Trainer','Trainer'),
        ('AD','AD'),('Manager','Manager'),('Service Delivery Manager','Service Delivery Manager'),('Asst.Manager','Asst.Manager'),
        ('CC Team','CC Team'),('BD','BD'),('MIS','MIS'),('Data Analyst','Data Analyst'),('Team Leader','Team Leader'),('QA','QA'),
        ('ATL','ATL'),('SME','SME')

                   )

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_desi=models.CharField(max_length=50,choices=emp_desi_list)
    team=models.CharField(max_length=50,choices=team_list)
    email=models.EmailField(default='emp@ecpl.com',null=True)


    def __str__(self):
        return self.emp_name



class Team(models.Model):

    team_list = (
        ('Noom', 'Noom'), ('Aadya Solutions', 'Aadya Solutions'), ('UPS CLP', 'UPS CLP'),
        ('Gardening Express', 'Gardening Express'),
        ('Maxwell Properties', 'Maxwell Properties'), ('Gubagoo', 'Gubagoo'),
        ('Digital Swiss Gold', 'Digital Swiss Gold'),
        ('Digital Signage', 'Digital Signage'), ('Success Systems', 'Success Systems'),
        ('Advancement Consulting ', 'Advancement Consulting'),
        ('Insalvage', 'Insalvage'), ('Medicare', 'Medicare'), ('Printerpix', 'Printerpix'),
        ('Printerpix Training', 'Printerpix Training'),
        ('First Look Appraisal', 'First Look Appraisal'), ('TCA Counseling Group', 'TCA Counseling Group'),
        ('Advit Sahdev Marketing', 'Advit Sahdev Marketing'),
        ('AKDY', 'AKDY'), ('AKDY Training', 'AKDY Training'), ('Monster Lead Group', 'Monster Lead Group'),
        ('Fame House', 'Fame House'),
        ('Lecanto Green coffee', 'Lecanto Green coffee'), ('Micro Distributing', 'Micro Distributing'),
        ('Aditya Birla', 'Aditya Birla'),
        ('Aditya Birla Cellulose', 'Aditya Birla Cellulose'),
        ('Aditya Birla Cellulose Training', 'Aditya Birla Cellulose Training'),
        ('City Security Services', 'City Security Services'), ('Active Sports Club', 'Active Sports Club'),
        ('Aditya Birla Sampling Team', 'Aditya Birla Sampling Team'),
        ('Aditya Birla Sampling Team Trainig', 'Aditya Birla Sampling Team Trainig'),
        ('Bigo - IMO Group Chat', 'Bigo - IMO Group Chat'),
        ('Bigo Monitor Team', 'Bigo Monitor Team'), ('Daniel Wellington', 'Daniel Wellington'),
        ('Option Matrix', 'Option Matrix'),
        ('Info Think LLC', 'Info Think LLC'), ('MT Cosmetics', 'MT Cosmetics'),
        ("Something's Brewing", "Something's Brewing"),
        ('WIT Digital', 'WIT Digital'), ('Sync Treasury LLC', 'Sync Treasury LLC'),
        ('SANA GAMING CONSULTING', 'SANA GAMING CONSULTING'),
        ('GrayStone LLC', 'GrayStone LLC'), ('Kaapi Machines', 'Kaapi Machines'),
        ('Richmond Assets & Holdings', 'Richmond Assets & Holdings'),
        ('US Home Exterior', 'US Home Exterior'), ('Pre Management Leicester LTD', 'Pre Management Leicester LTD'),
        ('American Income Life', 'American Income Life'),
        ('Life Alarm Services', 'Life Alarm Services'), ('ERI Global', 'ERI Global'),
        ('Allen Consulting group', 'Allen Consulting group'),
        ('Jeffery Tan ', 'Jeffery Tan '), ('Student Life', 'Student Life'),
        ('Career Transition Specialist', 'Career Transition Specialist'),
        ('Golden Eye Tech CCTV', 'Golden Eye Tech CCTV'), ('MOVEMENT INSURANCE', 'MOVEMENT INSURANCE'),
        ('Nucleus Media', 'Nucleus Media'),
        ('PSECU', 'PSECU'), ('Tentamus', 'Tentamus'), ('L&D', 'L&D'), ('Get A Rate', 'Get A Rate'),
        ('Mayfair Acct and Wealth', 'Mayfair Acct and Wealth'),
        ('Superking', 'Superking'), ('Millionaires Group', 'Millionaires Group'), ('PROTOSTAR', 'PROTOSTAR'),
        ('MESSE FRANKFURT', 'MESSE FRANKFURT'),
        ('System 4', 'System 4'), ('Naffa Innovations Pvt Ltd', 'Naffa Innovations Pvt Ltd'),
        ('Support Staff', 'Support Staff')

    )
    name=models.CharField(max_length=50,choices=team_list)
    qa = models.OneToOneField(User, on_delete=models.CASCADE,related_name='qa',null=True)
    manager = models.OneToOneField(User, on_delete=models.CASCADE,related_name='manager',null=True)




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
    closed_date=models.DateTimeField(null=True)


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
    closed_date=models.DateTimeField(null=True)


    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100]+'...'

class EmailMonitoringForm(models.Model):
    record_no=models.IntegerField()
    associate_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    email_date = models.DateField()
    audit_date = models.DateField()
    ticket_no=models.IntegerField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=60)
    concept = models.CharField(max_length=60)

    ce_1 = models.CharField(max_length=10)
    ce_2 = models.CharField(max_length=10)
    ce_3 = models.CharField(max_length=10)
    ce_4 = models.CharField(max_length=10)
    ce_5 = models.CharField(max_length=10)
    ce_6 = models.CharField(max_length=10)

    business_1 = models.CharField(max_length=10)
    business_2 = models.CharField(max_length=10)

    compliance_1 = models.CharField(max_length=10)
    compliance_2 = models.CharField(max_length=10)
    compliance_3 = models.CharField(max_length=10)

    email_summary=models.TextField()
    areas_improvement = models.TextField()
    positives = models.TextField()
    customer_feedback = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)

    ce_total=models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total=models.IntegerField(null=True)
    overall_score=models.IntegerField(null=True)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100]+'...'

class ChatMonitorinForm(models.Model):
    record_no = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    chat_date = models.DateField()
    audit_date = models.DateField()
    ticket_no = models.IntegerField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=60)
    concept = models.CharField(max_length=60)

    ce_1 = models.CharField(max_length=10)
    ce_2 = models.CharField(max_length=10)
    ce_3 = models.CharField(max_length=10)
    ce_4 = models.CharField(max_length=10)
    ce_5 = models.CharField(max_length=10)
    ce_6 = models.CharField(max_length=10)

    business_1 = models.CharField(max_length=10)
    business_2 = models.CharField(max_length=10)

    compliance_1 = models.CharField(max_length=10)
    compliance_2 = models.CharField(max_length=10)
    compliance_3 = models.CharField(max_length=10)

    chat_summary = models.TextField()
    areas_improvement = models.TextField()
    positives = models.TextField()
    customer_feedback = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'
