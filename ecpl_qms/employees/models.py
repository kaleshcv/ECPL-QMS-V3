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
        ('System 4','System 4'),('Naffa Innovations Pvt Ltd','Naffa Innovations Pvt Ltd'),('Support Staff','Support Staff'),
        ('Quality Team', 'Quality Team')

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
        ('Support Staff', 'Support Staff'),('Quality Team','Quality Team')

    )
    name=models.CharField(max_length=50,choices=team_list)
    qa = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qa',null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager', null=True)
    tl = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tl', null=True)

    def __str__(self):
        return self.name



# Final Forms ----------------------- #

class ChatMonitoringFormEva(models.Model):
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.IntegerField()
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    evaluator = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'
