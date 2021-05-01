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
        ('CRO','CRO'),('Patrolling officer','Patrolling officer'),('AM','AM'),('Trainer','Trainer'),
        ('AD','AD'),('Manager','Manager'),('Service Delivery Manager','Service Delivery Manager'),
        ('CC Team','CC Team'),('BD','BD'),('MIS','MIS'),('Data Analyst','Data Analyst'),('Team Leader','Team Leader'),('QA','QA'),
        ('ATL','ATL'),('SME','SME')

                   )




    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_desi=models.CharField(max_length=50,choices=emp_desi_list)
    team=models.CharField(max_length=50,choices=team_list)
    email=models.EmailField(default='emp@ecpl.com',null=True)

    process = models.CharField(max_length=100,choices=team_list)
    team_lead = models.CharField(max_length=50,default='Testlead')
    manager = models.CharField(max_length=50,default='Testmanager')
    am = models.CharField(max_length=50,default='testam')


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
    #qa = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qa',null=True)
    #manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager', null=True)
    #tl = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tl', null=True)

    def __str__(self):
        return self.name

class Process(models.Model):

    process_name=models.CharField(max_length=200)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)


class Campaigns(models.Model):
    name=models.CharField(max_length=200)
    campaign_id=models.IntegerField()
    qa_id=models.IntegerField(null=True)


# Final Forms ----------------------- #

class ChatMonitoringFormEva(models.Model):
    process=models.CharField(default='Noom-EVA',max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    trans_date = models.DateField()
    audit_date = models.DateField()

    campaign = models.CharField(max_length=100)
    evaluator = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # mgt
    manager=models.CharField(max_length=50)
    manager_id=models.IntegerField()

    category = models.CharField(max_length=20)

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

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)

    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ChatMonitoringFormPodFather(models.Model):
    process = models.CharField(default='Noom-POD', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    evaluator = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

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

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class InboundMonitoringFormNucleusMedia(models.Model):
    process = models.CharField(default='Nucleus', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)

    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



class FameHouseMonitoringForm(models.Model):
    process = models.CharField(default='Fame House', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    ticket_type = models.CharField(max_length=50)

    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)


    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()


    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()

    #ZENDESK

    ze_1 = models.IntegerField()
    ze_2 = models.IntegerField()
    ze_3 = models.IntegerField()
    ze_4 = models.IntegerField()

    #SHIPHERO
    sh_1 = models.IntegerField()
    sh_2 = models.IntegerField()
    sh_3 = models.IntegerField()
    sh_4 = models.IntegerField()
    sh_5 = models.IntegerField()

    ce_total = models.IntegerField(null=True)
    ze_total = models.IntegerField(null=True)
    sh_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    am = models.CharField(max_length=50,null=True)
    week=models.CharField(max_length=20,null=True)
    ##############
    fatal=models.BooleanField(default=False)
    fatal_count=models.IntegerField(default=0)

    disput_status=models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class FLAMonitoringForm(models.Model):
    process = models.CharField(default='FLA', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    check_list = models.CharField(max_length=400)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Checklist
    checklist_1 = models.IntegerField()

    reason_for_failure = models.TextField()
    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    overall_score = models.IntegerField()

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MasterMonitoringFormGetaRatesPSECU(models.Model):
    process = models.CharField(default='PSECU', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    softskill_6 = models.IntegerField()
    softskill_7 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    oc_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MasterMonitoringFormMovementInsurance(models.Model):
    process = models.CharField(default='Movement of Insurance', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    softskill_6 = models.IntegerField()
    softskill_7 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    oc_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



class MasterMonitoringFormTonnChatsEmail(models.Model):
    process = models.CharField(default='Tonn Chat Email', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)

    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()


    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    business_total=models.IntegerField(null=True)
    ce_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MasterMonitoringFormTonnCoaInboundCalls(models.Model):
    process = models.CharField(default='Tonn Coa', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsAadhyaSolution(models.Model):
    process = models.CharField(default='AAdya', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MTCosmeticsMonForm(models.Model):
    process = models.CharField(default='MT Cosmetic', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class PrinterPixMasterMonitoringFormInboundCalls(models.Model):
    process = models.CharField(default='Printer Pix Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class PrinterPixMasterMonitoringFormChatsEmail(models.Model):
    process = models.CharField(default='Printer Pix Chat Email', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class WitDigitalMasteringMonitoringForm(models.Model):
    process = models.CharField(default='Wit Digital', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_type=models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    service=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Tagging
    tagging_1=models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class Test(models.Model):
    test = models.IntegerField()


# ##### ######### Lead Sales Forms

class MonitoringFormLeadsInsalvage(models.Model):
    process = models.CharField(default='Insalvage', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsMedicare(models.Model):
    process = models.CharField(default='Medicare', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsCTS(models.Model):
    process = models.CharField(default='CTS', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsTentamusFood(models.Model):
    process = models.CharField(default='Tentamus Food', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsTentamusPet(models.Model):
    process = models.CharField(default='Tentamus Pet', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsCitySecurity(models.Model):
    process = models.CharField(default='City Security', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsAllenConsulting(models.Model):
    process = models.CharField(default='Allen Consulting', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsSystem4(models.Model):
    process = models.CharField(default='System4', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsLouisville(models.Model):
    process = models.CharField(default='Louisville', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsInfothinkLLC(models.Model):
    process = models.CharField(default='Info Think LLC', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsPSECU(models.Model):
    process = models.CharField(default='PSECU', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsGetARates(models.Model):
    process = models.CharField(default='Get A Rates', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsAdvanceConsultants(models.Model):
    process = models.CharField(default='Advance Consultants', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


############################## New Forms ############

class FurBabyMonForm(models.Model):
    process = models.CharField(default='Fur Baby', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MaxwellProperties(models.Model):
    process = models.CharField(default='Maxwell Properties', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



########## Domestic CHat ###############

class SuperPlayMonForm(models.Model):
    process = models.CharField(default='Super Play', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class DanielWellinChatEmailMonForm(models.Model):
    process = models.CharField(default='Daniel Wellington - Chat - Email', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class TerraceoChatEmailMonForm(models.Model):
    process = models.CharField(default='Terraceo - Chat - Email', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

######################################

class UpfrontOnlineLLCMonform(models.Model):
    process = models.CharField(default='Upfront Online LLC', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MicroDistributingMonForm(models.Model):
    process = models.CharField(default='Micro Distributing', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class JJStudioMonForm(models.Model):
    process = models.CharField(default='JJ Studio', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

# New Series Mon forms ~~ AAdya copy

class ZeroStressMarketingMonForm(models.Model):

    process = models.CharField(default='Zero Stress Marketing', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class WTUMonForm(models.Model):
    process = models.CharField(default='WTU', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class RoofWellMonForm(models.Model):
    process = models.CharField(default='Roof Well', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class GlydeAppMonForm(models.Model):
    process = models.CharField(default='Glyde App', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MillenniumScientificMonForm(models.Model):
    process = models.CharField(default='Millennium Scientific', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class FinesseMortgageMonForm(models.Model):
    process = models.CharField(default='Finesse Mortgage', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class StandSpotMonForm(models.Model):
    process = models.CharField(default='Stand Spot', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class CamIndustrialMonForm(models.Model):
    process = models.CharField(default='Cam Industrial', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class OptimalStudentLoanMonForm(models.Model):
    process = models.CharField(default='Optimal Student Loan', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class NavigatorBioMonForm(models.Model):
    process = models.CharField(default='Navigator Bio', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class AKDYInboundMonForm(models.Model):
    process = models.CharField(default='AKDY - Inbound', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class AKDYEmailMonForm(models.Model):

    process = models.CharField(default='AKDY - Email', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()

    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class IbizMonForm(models.Model):
    process = models.CharField(default='Ibiz', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class AdityaBirlaMonForm(models.Model):
    process = models.CharField(default='Aditya Birla Cellulose', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class BagyalakshmiMonForm(models.Model):
    process = models.CharField(default='Bhagyalaxmi Industries', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class DigitalSwissMonForm(models.Model):
    process = models.CharField(default='Digital Swiss Gold', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class NafaInnovationsMonForm(models.Model):
    process = models.CharField(default='Naffa Innovations', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class DanialWellingtonInboundMonForm(models.Model):
    process = models.CharField(default='Daniel Wellington - Inbound', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ProtostarMonForm(models.Model):
    process = models.CharField(default='Protostar', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class KappiMachineMonForm(models.Model):
    process = models.CharField(default='Kappi machine', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



class SomethingsBrewMonForm(models.Model):
    process = models.CharField(default='Somethings Brewing', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ABHMonForm(models.Model):
    process = models.CharField(default='AB - Hindalco', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class EmbassyLuxuryMonForm(models.Model):
    process = models.CharField(default='Embassy Luxury', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class IIBMonForm(models.Model):
    process = models.CharField(default='IIB', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class TerraceoLeadMonForm(models.Model):
    process = models.CharField(default='Terraceo - Lead', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class KalkiFashions(models.Model):
    process = models.CharField(default='Kalki Fashions', max_length=50)

    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
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
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



class Empdata(models.Model):
    uid=models.IntegerField(unique=True)
    username=models.IntegerField()
    password=models.CharField(max_length=30)

class Empprofile(models.Model):
    uid = models.IntegerField(unique=True)
    empname=models.CharField(max_length=50)
    empid=models.IntegerField()
    empdesi=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    teamlead=models.CharField(max_length=50)
    manager=models.CharField(max_length=50)
    user_id=models.IntegerField()
    am=models.CharField(max_length=50)
    process=models.CharField(max_length=50)


class EmpdataTest(models.Model):
    uid=models.IntegerField(unique=True)
