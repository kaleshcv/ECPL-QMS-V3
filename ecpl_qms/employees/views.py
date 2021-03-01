from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from . import forms


#Index
def index(request):
    return render(request,'index.html')

#Guidelines
def outboundGuidelines(request):
    return render(request,'guidelines/outbound.html')
def inboundGuidelines(request):
    return render(request,'guidelines/inbound.html')
def chatGuidelines(request):
    return render(request,'guidelines/chat.html')
def emailGuidelines(request):
    return render(request,'guidelines/email.html')

# Reistration, Sign up, Login, Logout, Change Password

def signup(request):
    team_leaders=Profile.objects.filter(emp_desi='Team Leader')
    managers=Profile.objects.filter(emp_desi='Manager')
    ams = Profile.objects.filter(emp_desi='AM')

    if request.method == 'POST':
        admin_id = request.POST['admin-id']
        admin_pwd = request.POST['admin-pwd']

        form = UserCreationForm(request.POST)  # form to create user
        profile_form = forms.ProfileCreation(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            # Admin ID PWD validation
            if admin_id=='ecpl-qms' and admin_pwd=='500199':

                manager=request.POST['manager']
                team_lead=request.POST['team-leader']
                am=request.POST['am']

                user = form.save()
                profile = profile_form.save(commit=False)

                profile.user = user
                profile.manager=manager
                profile.team_lead=team_lead
                profile.am=am

                profile.save()
                # login(request,user)
                return render(request,'index.html')
            else:
                messages.info(request, 'Invalid Admin Credentials !')
                return render(request,'sign-up.html',{'form': form, 'profile_form': profile_form})
    else:
        form = UserCreationForm()
        profile_form = forms.ProfileCreation()

    return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form,
                                            'team_leaders':team_leaders,'managers':managers,'ams':ams
                                            })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Login form
        if form.is_valid():

            # login the user
            user = form.get_user()
            login(request, user)

            # redirecting
            if user.profile.emp_desi=='QA':
                return redirect('/employees/qahome')
            elif user.profile.emp_desi=='Manager':
                return redirect('/employees/manager-home')
            else:
                return redirect('/employees/agenthome')
        else:
            form = AuthenticationForm()
            messages.info(request,'Invalid Credentials !')
            return render(request,'login.html',{'form':form})
    else:
        logout(request)
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/employees/login')

# Password Reset
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            logout(request)
            return render(request,'login.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def managerHome(request):
    user_id = request.user.id
    teams = Team.objects.filter(manager_id=user_id)
    employees = Profile.objects.filter(emp_desi='CRO')

    eva_total=ChatMonitoringFormEva.objects.all().count()
    eva_open_total = ChatMonitoringFormEva.objects.filter(status=False).count()
    closed_percentage_eva=int((eva_open_total/eva_total)*100)

    pod_total = ChatMonitoringFormPodFather.objects.all().count()
    pod_open_total = ChatMonitoringFormPodFather.objects.filter(status=False).count()
    closed_percentage_pod = int((pod_open_total / pod_total) * 100)

    pod={'name':'Noom-POD','total':pod_total,'total_open':pod_open_total,'perc':closed_percentage_pod}
    eva={'name':'Noom-EVA','total':eva_total,'total_open':eva_open_total,'perc':closed_percentage_eva}

    campaigns=[pod,eva,]

    data = {'teams': teams,
            'campaigns':campaigns,
            'employees':employees,
            }

    return render(request,'manager-home.html',data)

def employeeWiseReport(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        profile=Profile.objects.get(emp_id=emp_id)

        # function to calcluate overall Score, process name
        def scoreCalculator(campaign):
            overall_total = []
            name=[]
            for i in campaign:
                overall_total.append(i.overall_score)
                name.append(i.process)
            if len(overall_total) > 0:
                ov_perc = sum(overall_total) / len(overall_total)
            else:
                ov_perc = 100
            return ov_perc,name[0]

        # Mon Form List
        mon_forms = [ChatMonitoringFormEva,ChatMonitoringFormPodFather,InboundMonitoringFormNucleusMedia,FameHouseMonitoringForm,
                     FLAMonitoringForm,MasterMonitoringFormMTCosmetics,MasterMonitoringFormTonnChatsEmail,MasterMonitoringFormMovementInsurance,
                     WitDigitalMasteringMonitoringForm,PrinterPixMasterMonitoringFormChatsEmail,PrinterPixMasterMonitoringFormInboundCalls,
                     MonitoringFormLeadsAadhyaSolution,MonitoringFormLeadsInsalvage,MonitoringFormLeadsMedicare,MonitoringFormLeadsCTS,
                     MonitoringFormLeadsTentamusFood,MonitoringFormLeadsTentamusPet,MonitoringFormLeadsCitySecurity,
                     MonitoringFormLeadsAllenConsulting,MonitoringFormLeadsSystem4,MonitoringFormLeadsLouisville,MonitoringFormLeadsInfothinkLLC,
                     MonitoringFormLeadsPSECU,MonitoringFormLeadsGetARates,MonitoringFormLeadsAdvanceConsultants]

        #Campaign List
        campaign_details = []

        # Score in All forms
        for i in mon_forms:
            coaching=i.objects.filter(emp_id=emp_id)

            if coaching.count()>0:
                ov_perc,name=scoreCalculator(coaching)
                summary={'feedbacks_count':coaching.count(),'ov_avg':ov_perc,'name':name}
                campaign_details.append(summary)
            else:
                pass

        data={'campaign':campaign_details,'profile':profile}
        return render(request,'employee-wise-report.html',data)


def managerWiseReport(request):
    if request.method == 'POST':
        manager_emp_id=request.POST['emp_id']
        profile=Profile.objects.get(emp_id=manager_emp_id)
        manager_name=profile.emp_name

        # function to calcluate overall Score, process name
        def scoreCalculator(campaign):
            overall_total = []
            name=[]
            for i in campaign:
                overall_total.append(i.overall_score)
                name.append(i.process)
            if len(overall_total) > 0:
                ov_perc = sum(overall_total) / len(overall_total)
            else:
                ov_perc = 100
            return ov_perc,name[0]

        # Mon Form List
        mon_forms = [ChatMonitoringFormEva, ChatMonitoringFormPodFather, InboundMonitoringFormNucleusMedia,
                     FameHouseMonitoringForm,
                     FLAMonitoringForm, MasterMonitoringFormMTCosmetics, MasterMonitoringFormTonnChatsEmail,
                     MasterMonitoringFormMovementInsurance,
                     WitDigitalMasteringMonitoringForm, PrinterPixMasterMonitoringFormChatsEmail,
                     PrinterPixMasterMonitoringFormInboundCalls,
                     MonitoringFormLeadsAadhyaSolution, MonitoringFormLeadsInsalvage, MonitoringFormLeadsMedicare,
                     MonitoringFormLeadsCTS,
                     MonitoringFormLeadsTentamusFood, MonitoringFormLeadsTentamusPet, MonitoringFormLeadsCitySecurity,
                     MonitoringFormLeadsAllenConsulting, MonitoringFormLeadsSystem4, MonitoringFormLeadsLouisville,
                     MonitoringFormLeadsInfothinkLLC,
                     MonitoringFormLeadsPSECU, MonitoringFormLeadsGetARates, MonitoringFormLeadsAdvanceConsultants]

        #Campaign List
        campaign_details = []

        # Score in All forms
        for i in mon_forms:
            coaching=i.objects.filter(manager_id=manager_emp_id)

            if coaching.count()>0:
                ov_perc,name=scoreCalculator(coaching)
                summary={'feedbacks_count':coaching.count(),'ov_avg':ov_perc,'name':name}
                campaign_details.append(summary)
            else:
                pass


        data={'campaign':campaign_details,'manager_name':manager_name}

        return render(request,'manager-wise-report.html',data)

def qualityDashboardMgt(request):
    # Date Time
    import datetime
    d = datetime.datetime.now()

    month = d.strftime("%m")
    year = d.strftime("%Y")

    user_id = request.user.id

    employees = Profile.objects.filter(emp_desi='CRO')
    managers = Profile.objects.filter(emp_desi='Manager')

    teams=Team.objects.all()


    ############ Avg Score Calculator

    def avgscoreCalculator(monform):
        a=monform.objects.filter(audit_date__year=year, audit_date__month=month)
        a_avg=[]
        for i in a:
            a_avg.append(i.overall_score)
        if len(a_avg)>0:
            a_avg_score=sum(a_avg)/len(a_avg)
            return a_avg_score
        else:
            return 100

    eva_avg_score=avgscoreCalculator(ChatMonitoringFormEva)
    pod_avg_score=avgscoreCalculator(ChatMonitoringFormPodFather)
    nuc_avg_score=avgscoreCalculator(InboundMonitoringFormNucleusMedia)
    fame_avg_score=avgscoreCalculator(FameHouseMonitoringForm)
    fla_avg_score=avgscoreCalculator(FLAMonitoringForm)
    mt_avg_score=avgscoreCalculator(MasterMonitoringFormMTCosmetics)
    ton_avg_score=avgscoreCalculator(MasterMonitoringFormTonnChatsEmail)
    mov_avg_score=avgscoreCalculator(MasterMonitoringFormMovementInsurance)
    wit_avg_score=avgscoreCalculator(WitDigitalMasteringMonitoringForm)
    pixchat_avg_score=avgscoreCalculator(PrinterPixMasterMonitoringFormChatsEmail)
    pixcall_avg_score=avgscoreCalculator(PrinterPixMasterMonitoringFormInboundCalls)
    aadya_avg_score=avgscoreCalculator(MonitoringFormLeadsAadhyaSolution)
    insalvage_avg_score=avgscoreCalculator(MonitoringFormLeadsInsalvage)
    medicare_avg_score=avgscoreCalculator(MonitoringFormLeadsMedicare)
    cts_avg_score=avgscoreCalculator(MonitoringFormLeadsCTS)
    tfood_avg_score=avgscoreCalculator(MonitoringFormLeadsTentamusFood)
    tpet_avg_score=avgscoreCalculator(MonitoringFormLeadsTentamusPet)
    city_avg_score=avgscoreCalculator(MonitoringFormLeadsCitySecurity)
    allen_avg_score=avgscoreCalculator(MonitoringFormLeadsAllenConsulting)
    system4_avg_score=avgscoreCalculator(MonitoringFormLeadsSystem4)
    louis_avg_score=avgscoreCalculator(MonitoringFormLeadsLouisville)
    info_avg_score=avgscoreCalculator(MonitoringFormLeadsInfothinkLLC)
    psecu_avg_score=avgscoreCalculator(MonitoringFormLeadsPSECU)
    get_avg_score=avgscoreCalculator(MonitoringFormLeadsGetARates)
    adv_avg_score=avgscoreCalculator(MonitoringFormLeadsAdvanceConsultants)


    chat=(eva_avg_score+pod_avg_score+ton_avg_score+pixchat_avg_score)/4
    outbound=(mt_avg_score+mov_avg_score+aadya_avg_score)/3
    email=(eva_avg_score+pod_avg_score+ton_avg_score+pixchat_avg_score)/4
    inbound=(nuc_avg_score+pixcall_avg_score)/2
    other=(fame_avg_score+fla_avg_score+wit_avg_score)/3
    leads=(mt_avg_score+mov_avg_score+aadya_avg_score)/3

    # Coaching closure

    user_id = request.user.id

    employees = Profile.objects.filter(emp_desi='CRO')

    ######## Coaching closed Percentage Calculator

    def coachingClosureCalculator(monform):

        total=monform.objects.all().count()
        closed_total=monform.objects.filter(status=True).count()

        if total>0:
            closure=int((closed_total/total)*100)
            return closure
        else:
            return 100

    closed_percentage_eva=coachingClosureCalculator(ChatMonitoringFormEva)
    closed_percentage_pod=coachingClosureCalculator(ChatMonitoringFormPodFather)
    closed_percentage_nuc=coachingClosureCalculator(InboundMonitoringFormNucleusMedia)
    closed_percentage_fame=coachingClosureCalculator(FameHouseMonitoringForm)
    closed_percentage_fla=coachingClosureCalculator(FLAMonitoringForm)
    closed_percentage_mt=coachingClosureCalculator(MasterMonitoringFormMTCosmetics)
    closed_percentage_ton=coachingClosureCalculator(MasterMonitoringFormTonnChatsEmail)
    closed_percentage_mov=coachingClosureCalculator(MasterMonitoringFormMovementInsurance)
    closed_percentage_wit=coachingClosureCalculator(WitDigitalMasteringMonitoringForm)
    closed_percentage_pixchat=coachingClosureCalculator(PrinterPixMasterMonitoringFormChatsEmail)
    closed_percentage_pixcall=coachingClosureCalculator(PrinterPixMasterMonitoringFormInboundCalls)
    closed_percentage_aadya=coachingClosureCalculator(MonitoringFormLeadsAadhyaSolution)
    closed_percentage_insalvage=coachingClosureCalculator(MonitoringFormLeadsInsalvage)
    closed_percentage_medicare=coachingClosureCalculator(MonitoringFormLeadsMedicare)
    closed_percentage_cts=coachingClosureCalculator(MonitoringFormLeadsCTS)
    closed_percentage_tfood=coachingClosureCalculator(MonitoringFormLeadsTentamusFood)
    closed_percentage_tpet=coachingClosureCalculator(MonitoringFormLeadsTentamusPet)
    closed_percentage_city=coachingClosureCalculator(MonitoringFormLeadsCitySecurity)
    closed_percentage_allen=coachingClosureCalculator(MonitoringFormLeadsAllenConsulting)
    closed_percentage_system4=coachingClosureCalculator(MonitoringFormLeadsSystem4)
    closed_percentage_louis=coachingClosureCalculator(MonitoringFormLeadsLouisville)
    closed_percentage_info=coachingClosureCalculator(MonitoringFormLeadsInfothinkLLC)
    closed_percentage_psecu=coachingClosureCalculator(MonitoringFormLeadsPSECU)
    closed_percentage_getarates=coachingClosureCalculator(MonitoringFormLeadsGetARates)
    closed_percentage_advance=coachingClosureCalculator(MonitoringFormLeadsAdvanceConsultants)




    pod = {'name': 'Noom-POD', 'perc': closed_percentage_pod,'score':pod_avg_score}
    eva = {'name': 'Noom-EVA', 'perc': closed_percentage_eva,'score':eva_avg_score}
    nucleus={'name': 'Nucleus','perc':closed_percentage_nuc,'score':nuc_avg_score}
    famehouse={'name':'Fame House','perc':closed_percentage_fame,'score':fame_avg_score}
    fla={'name':'FLA','perc':closed_percentage_fla,'score':fla_avg_score}
    mt={'name':'MT Cosmetic','perc':closed_percentage_mt,'score':mt_avg_score}
    ton={'name':'Tonn Chat Email','perc':closed_percentage_ton,'score':ton_avg_score}
    mov={'name':'Movement of Insurance','perc':closed_percentage_mov,'score':mov_avg_score}
    wit={'name':'Wit Digital','perc':closed_percentage_wit,'score':wit_avg_score}
    pixchat={'name':'Printer Pix Chat Email','perc':closed_percentage_pixchat,'score':pixchat_avg_score}
    pixcall={'name':'Printer Pix Inbound','perc':closed_percentage_pixcall,'score':pixcall_avg_score}
    aadya={'name':'AAdya','perc':closed_percentage_aadya,'score':aadya_avg_score}
    insalvage={'name':'Insalvage','perc':closed_percentage_insalvage,'score':insalvage_avg_score}
    medicare={'name':'Medicare','perc':closed_percentage_medicare,'score':medicare_avg_score}
    cts={'name':'CTS','perc':closed_percentage_cts,'score':cts_avg_score}
    tfood={'name':'Tentamus Food','perc':closed_percentage_tfood,'score':tfood_avg_score}
    tpet={'name':'Tentamus Pet','perc':closed_percentage_tpet,'score':tpet_avg_score}
    city={'name':'City Security','perc':closed_percentage_city,'score':city_avg_score}
    allen={'name':'Allen Consulting','perc':closed_percentage_allen,'score':allen_avg_score}
    system={'name':'System4','perc':closed_percentage_system4,'score':system4_avg_score}
    louis={'name':'Louisville','perc':closed_percentage_louis,'score':louis_avg_score}
    info={'name':'Info Think LLC','perc':closed_percentage_info,'score':info_avg_score}
    psecu={'name':'PSECU','perc':closed_percentage_psecu,'score':psecu_avg_score}
    getarates={'name':'Get A Rates','perc':closed_percentage_getarates,'score':get_avg_score}
    advance={'name':'Advance Consultants','perc':closed_percentage_advance,'score':adv_avg_score}



    campaigns = [pod, eva,nucleus,famehouse,fla,mt,ton,mov,wit,pixchat,pixcall,aadya,
                 insalvage,medicare,cts,tfood,tpet,city,allen,system,louis,info,psecu,
                 getarates,advance]


    data = {

            'chat':chat,'outbound':outbound,'email':email,'inbound':inbound,'other':other,'leads':leads,

            'employees':employees,'managers':managers,'campaigns':campaigns,

            'teams':teams,

            }

    return render(request, 'quality-dashboard-management.html',data)



# Categorywise

def inboundSummary(request):
    # Date Time
    import datetime
    d = datetime.datetime.now()

    month = d.strftime("%m")
    year = d.strftime("%Y")


    nucleus_avg_score = InboundMonitoringFormNucleusMedia.objects.filter(audit_date__year=year, audit_date__month=month)
    nuc_avg = []
    for i in nucleus_avg_score:
        nuc_avg.append(i.overall_score)
    if len(nuc_avg) > 0:
        nuc_avg_score = sum(nuc_avg) / len(nuc_avg)
    else:
        nuc_avg_score = 100

    #Printer Pix Inbound
    pixcall_avgs=PrinterPixMasterMonitoringFormInboundCalls.objects.filter(audit_date__year=year, audit_date__month=month)
    pixcall_avg=[]
    for i in pixcall_avgs:
        pixcall_avg.append(i.overall_score)
    if len(pixcall_avg)>0:
        pixcall_avg_score=sum(pixcall_avg)/len(pixcall_avg)
    else:
        pixcall_avg_score=100

    nucleus={'name':'Nucleus','avg_score':nuc_avg_score}
    pix_inbound={'name':'Printer Pix Inbound','avg_score':pixcall_avg_score}

    campaigns=[nucleus,pix_inbound]

    data={'campaigns':campaigns,'month':month,'year':year}



    return render(request,'summary/inbound.html',data)

def chatSummary(request):
    # Date Time
    import datetime
    d = datetime.datetime.now()

    month = d.strftime("%m")
    year = d.strftime("%Y")

    # Eva Chat Details

    eva_avg_score=ChatMonitoringFormEva.objects.filter(audit_date__year=year,audit_date__month=month)
    eva_avg=[]
    for i in eva_avg_score:
        eva_avg.append(i.overall_score)
    if len(eva_avg)>0:
        eva_avg_score=sum(eva_avg)/len(eva_avg)
    else:
        eva_avg_score=100


    # Pod Father Chat Details

    pod_avg_score = ChatMonitoringFormPodFather.objects.filter(audit_date__year=year, audit_date__month=month)
    pod_avg = []
    for i in pod_avg_score:
        pod_avg.append(i.overall_score)
    if len(pod_avg) > 0:
        pod_avg_score = sum(pod_avg) / len(pod_avg)
    else:
        pod_avg_score = 100

    #Tonn Chats
    ton_avgs=MasterMonitoringFormTonnChatsEmail.objects.filter(audit_date__year=year, audit_date__month=month)
    ton_avg=[]
    for i in ton_avgs:
        ton_avg.append(i.overall_score)
    if len(ton_avg)>0:
        ton_avg_score=sum(ton_avg)/len(ton_avg)
    else:
        ton_avg_score=100

    #Printer Pix chat Email
    pixchat_avgs=PrinterPixMasterMonitoringFormChatsEmail.objects.filter(audit_date__year=year, audit_date__month=month)
    pixchat_avg=[]
    for i in pixchat_avgs:
        pixchat_avg.append(i.overall_score)
    if len(pixchat_avg)>0:
        pixchat_avg_score=sum(pixchat_avg)/len(pixchat_avg)
    else:
        pixchat_avg_score=100

    eva={'name':'Eva Noom','avg_score':eva_avg_score}
    pod={'name':'POD','avg_score':pod_avg_score}
    tonn_chat={'name':'Tonn Chats','avg_score':ton_avg_score}
    pix_chat={'name':'Printer Pix Chat','avg_score':pixchat_avg_score}

    campaigns=[eva,pod,tonn_chat,pix_chat]

    data = {'campaigns': campaigns, 'month': month, 'year': year}

    return render(request, 'summary/chat.html', data)

def leadsSummary(request):
    # Date Time
    import datetime
    d = datetime.datetime.now()

    month = d.strftime("%m")
    year = d.strftime("%Y")

    # MT Cosmetics
    mt_avgs = MasterMonitoringFormMTCosmetics.objects.filter(audit_date__year=year, audit_date__month=month)
    mt_avg = []
    for i in mt_avgs:
        mt_avg.append(i.overall_score)
    if len(mt_avg) > 0:
        mt_avg_score = sum(mt_avg) / len(mt_avg)
    else:
        mt_avg_score = 100

    #Leads AAdya
    aadya_avgs=MonitoringFormLeadsAadhyaSolution.objects.filter(audit_date__year=year, audit_date__month=month)
    aadya_avg=[]
    for i in aadya_avgs:
        aadya_avg.append(i.overall_score)
    if len(aadya_avg)>0:
        aadya_avg_score=sum(aadya_avg)/len(aadya_avg)
    else:
        aadya_avg_score=100

    #Movement of Insurance
    mov_avgs=MasterMonitoringFormMovementInsurance.objects.filter(audit_date__year=year, audit_date__month=month)
    mov_avg=[]
    for i in mov_avgs:
        mov_avg.append(i.overall_score)
    if len(mov_avg)>0:
        mov_avg_score=sum(mov_avg)/len(mov_avg)
    else:
        mov_avg_score=100

    mt={'name':'MT Cosmetic','avg_score':mt_avg_score}
    aadya={'name':'Aadya','avg_score':aadya_avg_score}
    mov_ins={'name':'Movement of Insurance','avg_score':mov_avg_score}

    campaigns=[mt,aadya,mov_ins]

    data = {'campaigns': campaigns, 'month': month, 'year': year}

    return render(request, 'summary/leads.html', data)

def otherSummary(request):
    # Date Time
    import datetime
    d = datetime.datetime.now()

    month = d.strftime("%m")
    year = d.strftime("%Y")

    # Fame House
    fameh_avg_score = FameHouseMonitoringForm.objects.filter(audit_date__year=year, audit_date__month=month)
    fame_avg = []
    for i in fameh_avg_score:
        fame_avg.append(i.overall_score)
    if len(fame_avg) > 0:
        fame_avg_score = sum(fame_avg) / len(fame_avg)
    else:
        fame_avg_score = 100

    # FLA
    fla_avgs = FLAMonitoringForm.objects.filter(audit_date__year=year, audit_date__month=month)
    fla_avg = []
    for i in fla_avgs:
        fla_avg.append(i.overall_score)
    if len(fla_avg) > 0:
        fla_avg_score = sum(fla_avg) / len(fla_avg)
    else:
        fla_avg_score = 100

    #Wit Digital
    wit_avgs=WitDigitalMasteringMonitoringForm.objects.filter(audit_date__year=year, audit_date__month=month)
    wit_avg=[]
    for i in wit_avgs:
        wit_avg.append(i.overall_score)
    if len(wit_avg)>0:
        wit_avg_score=sum(wit_avg)/len(wit_avg)
    else:
        wit_avg_score=100

    fame={'name':'Fame House','avg_score':fame_avg_score}
    fla={'name':'FLA','avg_score':fla_avg_score}
    wit={'name':'Wit Digital','avg_score':wit_avg_score}

    campaigns=[fame,fla,wit]

    data = {'campaigns': campaigns, 'month': month, 'year': year}

    return render(request, 'summary/other.html', data)



def agenthome(request):

    agent_name = request.user.profile.emp_name
    team_name=request.user.profile.team
    team = Team.objects.get(name=team_name)

    # Chat Eva Details

    #################### open campaigns indevidual

    def openCampaigns(monforms):
        open_obj = monforms.objects.filter(associate_name=agent_name, status=False)
        return open_obj

    open_eva = openCampaigns(ChatMonitoringFormEva)
    open_pod = openCampaigns(ChatMonitoringFormPodFather)
    open_nuc = openCampaigns(InboundMonitoringFormNucleusMedia)
    open_fame = openCampaigns(FameHouseMonitoringForm)
    open_fla = openCampaigns(FLAMonitoringForm)
    open_mt = openCampaigns(MasterMonitoringFormMTCosmetics)
    open_ton = openCampaigns(MasterMonitoringFormTonnChatsEmail)
    open_mov = openCampaigns(MasterMonitoringFormMovementInsurance)
    open_wit = openCampaigns(WitDigitalMasteringMonitoringForm)
    open_pixchat = openCampaigns(PrinterPixMasterMonitoringFormChatsEmail)
    open_pixcall = openCampaigns(PrinterPixMasterMonitoringFormInboundCalls)
    open_aadya = openCampaigns(MonitoringFormLeadsAadhyaSolution)
    open_insalvage = openCampaigns(MonitoringFormLeadsInsalvage)
    open_medicare = openCampaigns(MonitoringFormLeadsMedicare)
    open_cts = openCampaigns(MonitoringFormLeadsCTS)
    open_tfood = openCampaigns(MonitoringFormLeadsTentamusFood)
    open_tpet = openCampaigns(MonitoringFormLeadsTentamusPet)
    open_city = openCampaigns(MonitoringFormLeadsCitySecurity)
    open_allen = openCampaigns(MonitoringFormLeadsAllenConsulting)
    open_system4 = openCampaigns(MonitoringFormLeadsSystem4)
    open_louis = openCampaigns(MonitoringFormLeadsLouisville)
    open_info = openCampaigns(MonitoringFormLeadsInfothinkLLC)
    open_psecu = openCampaigns(MonitoringFormLeadsPSECU)
    open_getarates = openCampaigns(MonitoringFormLeadsGetARates)
    open_advance = openCampaigns(MonitoringFormLeadsAdvanceConsultants)

    ################### opn_count #############

    list_of_monforms = [ChatMonitoringFormEva, ChatMonitoringFormPodFather, InboundMonitoringFormNucleusMedia,
                        FameHouseMonitoringForm, FLAMonitoringForm, MasterMonitoringFormMTCosmetics,
                        MasterMonitoringFormTonnChatsEmail, MasterMonitoringFormMovementInsurance,
                        WitDigitalMasteringMonitoringForm,
                        PrinterPixMasterMonitoringFormChatsEmail, PrinterPixMasterMonitoringFormInboundCalls,
                        MonitoringFormLeadsAadhyaSolution,
                        MonitoringFormLeadsInsalvage, MonitoringFormLeadsMedicare, MonitoringFormLeadsCTS,
                        MonitoringFormLeadsTentamusFood,
                        MonitoringFormLeadsTentamusPet, MonitoringFormLeadsCitySecurity,
                        MonitoringFormLeadsAllenConsulting,
                        MonitoringFormLeadsSystem4, MonitoringFormLeadsLouisville, MonitoringFormLeadsInfothinkLLC,
                        MonitoringFormLeadsPSECU, MonitoringFormLeadsGetARates, MonitoringFormLeadsAdvanceConsultants,
                        ]

    list_of_open_count = []

    for i in list_of_monforms:
        count = i.objects.filter(associate_name=agent_name, status=False).count()
        list_of_open_count.append(count)

    total_open_coachings = sum(list_of_open_count)

    data = {
            'open_eva_chat': open_eva,
            'open_pod_chat': open_pod,
            'open_nucleus': open_nuc,
            'open_famehouse': open_fame,
            'open_fla': open_fla,
            'open_mt': open_mt,
            'open_tonnchat': open_ton,
            'open_mov': open_mov,
            'open_wit': open_wit,
            'open_pixchat': open_pixchat,
            'open_pixinbound': open_pixcall,
            'open_aadya': open_aadya,
            'open_insalvage': open_insalvage,
            'open_medicare': open_medicare,
            'open_cts': open_cts,
            'open_tfood': open_tfood,
            'open_tpet': open_tpet,
            'open_city': open_city,
            'open_allen': open_allen,
            'open_system4': open_system4,
            'open_louis': open_louis,
            'open_info': open_info,
            'open_psecu': open_psecu,
            'open_get': open_getarates,
            'open_advance': open_advance,

            'total_open': total_open_coachings,

            'team':team
            }






    return render(request, 'agent-home.html',data)




# Coaching View ---------------------------- !!!

def empCoachingViewEvachat(request,pk):
    coaching=ChatMonitoringFormEva.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'coaching-views/emp-coaching-view-eva-chat.html',data)

def qaCoachingViewEvachat(request,pk):
    coaching = ChatMonitoringFormEva.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-eva-chat.html', data)

def empCoachingViewPodchat(request,pk):
    coaching=ChatMonitoringFormPodFather.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'coaching-views/emp-coaching-view-pod-chat.html',data)

def qaCoachingViewPodchat(request,pk):
    coaching = ChatMonitoringFormPodFather.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-pod-chat.html', data)

def empCoachingviewNucleus(request,pk):
    coaching=InboundMonitoringFormNucleusMedia.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'coaching-views/emp-coaching-view-inbound.html',data)

def qaCoachingviewNucleus(request,pk):
    coaching=InboundMonitoringFormNucleusMedia.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'coaching-views/qa-coaching-view-inbound.html',data)

def empCoachingviewFamehouse(request,pk):
    coaching=FameHouseMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-fame-house.html', data)
def qaCoachingviewFamehouse(request,pk):
    coaching=FameHouseMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-fame-house.html', data)

def empCoachingviewFLA(request,pk):
    coaching = FLAMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-fla.html', data)
def qaCoachingviewFLA(request,pk):
    coaching = FLAMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-fla.html', data)
def empCoachingviewMt(request,pk):
    coaching = MasterMonitoringFormMTCosmetics.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-mt.html', data)
def qaCoachingviewMt(request,pk):
    coaching = MasterMonitoringFormMTCosmetics.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-mt.html', data)
def empCoachingviewMovIns(request,pk):
    coaching = MasterMonitoringFormMovementInsurance.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-mov-ins.html', data)
def qaCoachingviewMovIns(request,pk):
    coaching = MasterMonitoringFormMovementInsurance.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-mov-ins.html', data)
def empCoachingviewWit(request,pk):
    coaching = WitDigitalMasteringMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-wit.html', data)
def qaCoachingviewWit(request,pk):
    coaching = WitDigitalMasteringMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-wit.html', data)
def empCoachingviewTonnchat(request,pk):
    coaching = MasterMonitoringFormTonnChatsEmail.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-tonn-chat.html', data)
def qaCoachingviewTonnchat(request,pk):
    coaching = MasterMonitoringFormTonnChatsEmail.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-tonn-chat.html', data)

def empCoachingviewPixchat(request,pk):
    coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-pix-chat.html', data)
def qaCoachingviewPixchat(request,pk):
    coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-pix-chat.html', data)
def empCoachingviewPixinbound(request,pk):
    coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-pix-inbound.html', data)
def qaCoachingviewPixinbound(request,pk):
    coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-pix-inbound.html', data)

def empCoachingviewAadya(request,pk):
    coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-aadya.html', data)

def empCoachingviewInsalvage(request,pk):
    coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-insalvage.html', data)
def empCoachingviewMedicare(request,pk):
    coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-medicare.html', data)
def empCoachingviewCts(request,pk):
    coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-cts.html', data)
def empCoachingviewTfood(request,pk):
    coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-tfood.html', data)
def empCoachingviewTpet(request,pk):
    coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-tpet.html', data)
def empCoachingviewCity(request,pk):
    coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-city.html', data)
def empCoachingviewAllen(request,pk):
    coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-allen.html', data)
def empCoachingviewSystem4(request,pk):
    coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-system4.html', data)
def empCoachingviewLouis(request,pk):
    coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-louis.html', data)
def empCoachingviewInfo(request,pk):
    coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-info.html', data)
def empCoachingviewPsecu(request,pk):
    coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-psecu.html', data)
def empCoachingviewGet(request,pk):
    coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-get.html', data)
def empCoachingviewAdvance(request,pk):
    coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/emp-coaching-view-advance.html', data)



def qaCoachingviewAadya(request,pk):
    coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-aadya.html', data)

def qaCoachingviewInsalvage(request,pk):
    coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-insalvage.html', data)

def qaCoachingviewMedicare(request,pk):
    coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-medicare.html', data)

def qaCoachingviewCts(request,pk):
    coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-cts.html', data)

def qaCoachingviewTfood(request,pk):
    coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-tfood.html', data)

def qaCoachingviewTpet(request,pk):
    coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-tpet.html', data)

def qaCoachingviewCity(request,pk):
    coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-city.html', data)
def qaCoachingviewAllen(request,pk):
    coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-allen.html', data)
def qaCoachingviewSystem4(request,pk):
    coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-system4.html', data)
def qaCoachingviewLouis(request,pk):
    coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-louis.html', data)
def qaCoachingviewInfo(request,pk):
    coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-info.html', data)

def qaCoachingviewPsecu(request,pk):
    coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-psecu.html', data)

def qaCoachingviewGet(request,pk):
    coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-get.html', data)


def qaCoachingviewAdvance(request,pk):
    coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'coaching-views/qa-coaching-view-advance.html', data)



# Open status Coaching View
def qacoachingViewOpenAll(request,pk):
    if pk>0:

        qa_name=request.user.profile.emp_name

        eva = ChatMonitoringFormEva.objects.filter(added_by=qa_name, status=False)
        pod = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False)
        nucleus = InboundMonitoringFormNucleusMedia.objects.filter(added_by=qa_name, status=False)
        famehouse = FameHouseMonitoringForm.objects.filter(added_by=qa_name, status=False)
        fla = FLAMonitoringForm.objects.filter(added_by=qa_name, status=False)
        mt = MasterMonitoringFormMTCosmetics.objects.filter(added_by=qa_name, status=False)
        tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(added_by=qa_name, status=False)
        mov = MasterMonitoringFormMovementInsurance.objects.filter(added_by=qa_name, status=False)
        wit = WitDigitalMasteringMonitoringForm.objects.filter(added_by=qa_name, status=False)
        pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(added_by=qa_name, status=False)
        pixinbound = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(added_by=qa_name, status=False)
        aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(added_by=qa_name, status=False)

        data={
                'eva':eva,'pod':pod,'nucleus':nucleus,'famehouse':famehouse,'fla':fla,'mt':mt,'tonnchat':tonnchat,
                'mov':mov,'wit':wit,'pixchat':pixchat,'pixinbound':pixinbound,'aadya':aadya
             }
        return render(request,'qa-open-status-coachings-view.html',data)
    else:
        return redirect('/employees/qahome')

# Campaign wise coaching view - qa - manager

def campaignwiseCoachings(request):

    if request.method == 'POST':
        team_id = request.POST['team_id']
        status=request.POST['status']
        team_name=Team.objects.get(id=team_id)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        if start_date and end_date:

            if status=='all':

                eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,
                                                                audit_date__range=[start_date, end_date])
                pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,
                                                                      audit_date__range=[start_date, end_date])
                nucleus = InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,
                                                                           audit_date__range=[start_date, end_date])
                fame = FameHouseMonitoringForm.objects.filter(campaign=team_name,
                                                              audit_date__range=[start_date, end_date])
                fla = FLAMonitoringForm.objects.filter(campaign=team_name, audit_date__range=[start_date, end_date])
                mt = MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,
                                                                    audit_date__range=[start_date, end_date])
                tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,
                                                                             audit_date__range=[start_date, end_date])
                mov = MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,
                                                                           audit_date__range=[start_date, end_date])
                wit = WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,
                                                                       audit_date__range=[start_date, end_date])
                pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,
                                                                                  audit_date__range=[start_date,
                                                                                                     end_date])
                pixinbound = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,
                                                                                       audit_date__range=[start_date,
                                                                                                          end_date])
                aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,
                                                                         audit_date__range=[start_date, end_date])


            else:

                eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name, status=status,
                                                                audit_date__range=[start_date, end_date])
                pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name, status=status,
                                                                      audit_date__range=[start_date, end_date])
                nucleus = InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name, status=status,
                                                                           audit_date__range=[start_date, end_date])
                fame = FameHouseMonitoringForm.objects.filter(campaign=team_name, status=status,
                                                              audit_date__range=[start_date, end_date])
                fla = FLAMonitoringForm.objects.filter(campaign=team_name, status=status,
                                                       audit_date__range=[start_date, end_date])
                mt = MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name, status=status,
                                                                    audit_date__range=[start_date, end_date])
                tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name, status=status,
                                                                             audit_date__range=[start_date, end_date])
                mov = MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name, status=status,
                                                                           audit_date__range=[start_date, end_date])
                wit = WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name, status=status,
                                                                       audit_date__range=[start_date, end_date])
                pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name, status=status,
                                                                                  audit_date__range=[start_date,
                                                                                                     end_date])
                pixinbound = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,
                                                                                       status=status,
                                                                                       audit_date__range=[start_date,
                                                                                                          end_date])
                aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name, status=status,
                                                                         audit_date__range=[start_date, end_date])


            data={
                'eva_chat': eva_chat, 'pod_chat': pod_chat, 'nucleus': nucleus, 'fame': fame, 'fla': fla, 'mt': mt,
                'tonnchat': tonnchat, 'mov': mov, 'wit': wit, 'pixchat': pixchat, 'pixinbound': pixinbound,
                'aadya': aadya,
                 }

            return render(request,'campaign-wise-coaching-view.html',data)


        else:

            if status=='all':

                eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name)
                pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name)
                nucleus=InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name)
                fame=FameHouseMonitoringForm.objects.filter(campaign=team_name)
                fla=FLAMonitoringForm.objects.filter(campaign=team_name)
                mt=MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name)
                tonnchat=MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name)
                mov=MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name)
                wit=WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name)
                pixchat=PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name)
                pixinbound=PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name)
                aadya=MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name)
            else:


                eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status)
                pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status)
                nucleus=InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,status=status)
                fame=FameHouseMonitoringForm.objects.filter(campaign=team_name,status=status)
                fla=FLAMonitoringForm.objects.filter(campaign=team_name,status=status)
                mt=MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,status=status)
                tonnchat=MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,status=status)
                mov=MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,status=status)
                wit=WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,status=status)
                pixchat=PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,status=status)
                pixinbound=PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,status=status)
                aadya=MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,status=status)

        data={
                'eva_chat':eva_chat,'pod_chat':pod_chat,'nucleus':nucleus,'fame':fame,'fla':fla,'mt':mt,
                'tonnchat':tonnchat,'mov':mov,'wit':wit,'pixchat':pixchat,'pixinbound':pixinbound,'aadya':aadya,
             }

        return render(request,'campaign-wise-coaching-view.html',data)
    else:
        pass


# Campaign wise coaching view - Agent

def campaignwiseCoachingsAgent(request):
    if request.method == 'POST':
        team_id = request.POST['team_id']
        status=request.POST['status']
        team_name=Team.objects.get(id=team_id)

        emp_id=request.user.profile.emp_id
        start_date=request.POST['start_date']
        end_date = request.POST['end_date']


        if start_date and end_date:

            if status=='all':

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_nucleus=InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_famehouse=FameHouseMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_fla=FLAMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_mt=MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_tonnchat=MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_mov=MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_wit=WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pixchat=PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pixinboud=PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_aadya=MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])


            else:

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_nucleus = InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,status=status,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_famehouse = FameHouseMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_fla = FLAMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_mt = MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_mov = MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_wit = WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pixinboud = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,emp_id=emp_id,audit_date__range=[start_date,end_date])


            data={
                    'coaching_eva_chat':coaching_eva_chat,'coaching_pod_chat':coaching_pod_chat,'coaching_nucleus':coaching_nucleus,
                    'coaching_famehouse':coaching_famehouse,'coaching_fla':coaching_fla,'coaching_mt':coaching_mt,
                    'coaching_tonnchat':coaching_tonnchat,'coaching_mov':coaching_mov,'coaching_wit':coaching_wit,
                    'coaching_pixchat':coaching_pixchat,'coaching_pixinboud':coaching_pixinboud,'coaching_aadya':coaching_aadya,
                 }

            return render(request,'campaign-wise-coaching-view-agent.html',data)
        else:
            if status=='all':

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_nucleus = InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_famehouse = FameHouseMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_fla = FLAMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_mt = MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_mov = MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_wit = WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_pixinboud = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,emp_id=emp_id)


            else:

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_nucleus = InboundMonitoringFormNucleusMedia.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_famehouse = FameHouseMonitoringForm.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_fla = FLAMonitoringForm.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_mt = MasterMonitoringFormMTCosmetics.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_tonnchat = MasterMonitoringFormTonnChatsEmail.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_mov = MasterMonitoringFormMovementInsurance.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_wit = WitDigitalMasteringMonitoringForm.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_pixchat = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_pixinboud = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_aadya = MonitoringFormLeadsAadhyaSolution.objects.filter(campaign=team_name,status=status,emp_id=emp_id)

            data = {
                'coaching_eva_chat': coaching_eva_chat, 'coaching_pod_chat': coaching_pod_chat,
                'coaching_nucleus': coaching_nucleus,
                'coaching_famehouse': coaching_famehouse, 'coaching_fla': coaching_fla, 'coaching_mt': coaching_mt,
                'coaching_tonnchat': coaching_tonnchat, 'coaching_mov': coaching_mov, 'coaching_wit': coaching_wit,
                'coaching_pixchat': coaching_pixchat, 'coaching_pixinboud': coaching_pixinboud,
                'coaching_aadya': coaching_aadya,
            }

            return render(request,'campaign-wise-coaching-view-agent.html',data)

    else:
        return redirect('/employees/agenthome')

def signCoaching(request,pk):
    now = datetime.now()
    category=request.POST['category']
    emp_comments=request.POST['emp_comments']

    if category == 'eva-chat':
        coaching=ChatMonitoringFormEva.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'pod-chat':
        coaching=ChatMonitoringFormPodFather.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'nucleus':
        coaching = InboundMonitoringFormNucleusMedia.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'fame-house':
        coaching = FameHouseMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'fla':
        coaching = FLAMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'mt':
        coaching = MasterMonitoringFormMTCosmetics.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'mov-ins':
        coaching = MasterMonitoringFormMovementInsurance.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'wit':
        coaching = WitDigitalMasteringMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'tonn-chat':
        coaching = MasterMonitoringFormTonnChatsEmail.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'pix-inbound':
        coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'pix-chat':
        coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'aadya':
        coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'insalvage':
        coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'medicare':
        coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'cts':
        coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'tfood':
        coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'tpet':
        coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'city':
        coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'allen':
        coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'system4':
        coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'louis':
        coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'info':
        coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'psecu':
        coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'get':
        coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'advance':
        coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')


    else:
        return redirect('/employees/agenthome')


def coachingSuccess(request):

    return render(request,'coaching-success-message.html')

def coachingDispute(request):
    if request.method == 'POST':

        team= request.user.profile.team

        team=Team.objects.get(name=team)
        data={'team':team}
        return render(request,'coaching-dispute-message.html',data)
    else:
        return redirect('/employees/agenthome')

def qahome(request):

    qa_name=request.user.profile.emp_name
    user_id=request.user.id
    teams=Team.objects.all()

    ######### List of All Coachings ##############3

    list_of_monforms=[ChatMonitoringFormEva,ChatMonitoringFormPodFather,InboundMonitoringFormNucleusMedia,
                      FameHouseMonitoringForm,FLAMonitoringForm,MasterMonitoringFormMTCosmetics,
                      MasterMonitoringFormTonnChatsEmail,MasterMonitoringFormMovementInsurance,WitDigitalMasteringMonitoringForm,
                      PrinterPixMasterMonitoringFormChatsEmail,PrinterPixMasterMonitoringFormInboundCalls,MonitoringFormLeadsAadhyaSolution,
                      MonitoringFormLeadsInsalvage,MonitoringFormLeadsMedicare,MonitoringFormLeadsCTS,MonitoringFormLeadsTentamusFood,
                      MonitoringFormLeadsTentamusPet,MonitoringFormLeadsCitySecurity,MonitoringFormLeadsAllenConsulting,
                      MonitoringFormLeadsSystem4,MonitoringFormLeadsLouisville,MonitoringFormLeadsInfothinkLLC,
                      MonitoringFormLeadsPSECU,MonitoringFormLeadsGetARates,MonitoringFormLeadsAdvanceConsultants,
                      ]

    # Total NO of Coachings
    total_coaching_ids=[]

    for i in list_of_monforms:
        x=i.objects.filter(added_by=qa_name)

        for i in x:
            total_coaching_ids.append(i.id)

    total_coaching=len(total_coaching_ids)

    # All coaching objects

    all_coaching_obj=[]

    for i in list_of_monforms:
        x=i.objects.filter(added_by=qa_name).order_by('audit_date')
        all_coaching_obj.append(x)

    ##### Open_campaigns_objects  ###############

    list_open_campaigns=[]

    for i in list_of_monforms:
        opn_cmp_obj=i.objects.filter(status=False)
        list_open_campaigns.append(opn_cmp_obj)


    #################### open campaigns indevidual

    def openCampaigns(monforms):
        open_obj=monforms.objects.filter(added_by=qa_name,status=False)
        return open_obj

    open_eva=openCampaigns(ChatMonitoringFormEva)
    open_pod=openCampaigns(ChatMonitoringFormPodFather)
    open_nuc=openCampaigns(InboundMonitoringFormNucleusMedia)
    open_fame=openCampaigns(FameHouseMonitoringForm)
    open_fla=openCampaigns(FLAMonitoringForm)
    open_mt=openCampaigns(MasterMonitoringFormMTCosmetics)
    open_ton=openCampaigns(MasterMonitoringFormTonnChatsEmail)
    open_mov=openCampaigns(MasterMonitoringFormMovementInsurance)
    open_wit=openCampaigns(WitDigitalMasteringMonitoringForm)
    open_pixchat=openCampaigns(PrinterPixMasterMonitoringFormChatsEmail)
    open_pixcall=openCampaigns(PrinterPixMasterMonitoringFormInboundCalls)
    open_aadya=openCampaigns(MonitoringFormLeadsAadhyaSolution)
    open_insalvage=openCampaigns(MonitoringFormLeadsInsalvage)
    open_medicare=openCampaigns(MonitoringFormLeadsMedicare)
    open_cts=openCampaigns(MonitoringFormLeadsCTS)
    open_tfood=openCampaigns(MonitoringFormLeadsTentamusFood)
    open_tpet=openCampaigns(MonitoringFormLeadsTentamusPet)
    open_city=openCampaigns(MonitoringFormLeadsCitySecurity)
    open_allen=openCampaigns(MonitoringFormLeadsAllenConsulting)
    open_system4=openCampaigns(MonitoringFormLeadsSystem4)
    open_louis=openCampaigns(MonitoringFormLeadsLouisville)
    open_info=openCampaigns(MonitoringFormLeadsInfothinkLLC)
    open_psecu=openCampaigns(MonitoringFormLeadsPSECU)
    open_getarates=openCampaigns(MonitoringFormLeadsGetARates)
    open_advance=openCampaigns(MonitoringFormLeadsAdvanceConsultants)

################### opn_count #############

    list_of_open_count=[]

    for i in list_of_monforms:

        count=i.objects.filter(added_by=qa_name,status=False).count()
        list_of_open_count.append(count)

    total_open_coachings=sum(list_of_open_count)

    data={'teams':teams,
          'open_eva_chat':open_eva,
          'open_pod_chat':open_pod,
          'open_nucleus':open_nuc,
          'open_famehouse':open_fame,
          'open_fla':open_fla,
          'open_mt':open_mt,
          'open_tonnchat':open_ton,
          'open_mov':open_mov,
          'open_wit':open_wit,
          'open_pixchat':open_pixchat,
          'open_pixinbound':open_pixcall,
          'open_aadya':open_aadya,
          'open_insalvage': open_insalvage,
          'open_medicare':open_medicare,
          'open_cts':open_cts,
          'open_tfood':open_tfood,
          'open_tpet':open_tpet,
          'open_city':open_city,
          'open_allen':open_allen,
          'open_system4':open_system4,
          'open_louis':open_louis,
          'open_info':open_info,
          'open_psecu':open_psecu,
          'open_get':open_getarates,
          'open_advance':open_advance,

          'total_open':total_open_coachings,'total_coaching':total_coaching,
          'all_c_obj':all_coaching_obj,

          'open_campaigns':list_open_campaigns

          }

    return render(request,'qa-home.html',data)


# Final Forms

def chatCoachingformEva(request):
    if request.method == 'POST':
        category='chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no=request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator=request.POST['evaluator']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################


        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])

        ce_total=ce_1+ce_2+ce_3+ce_4

        #Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total=compliance_1+compliance_2+compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1==0 or compliance_2==0 or compliance_3==0 or compliance_4==0 or compliance_5==0 or compliance_6==0:
            overall_score=0
        else:
            overall_score=ce_total+compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        chat = ChatMonitoringFormEva(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,concept=concept,evaluator=evaluator,

                                     ce_1=ce_1,ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_total=ce_total,

                                     compliance_1=compliance_1,compliance_2=compliance_2,compliance_3=compliance_3,
                                     compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score,category=category
                                     )
        chat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)

def chatCoachingformPodFather(request):
    if request.method == 'POST':
        category='chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no=request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator=request.POST['evaluator']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])

        ce_total=ce_1+ce_2+ce_3+ce_4

        #Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total=compliance_1+compliance_2+compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1==0 or compliance_2==0 or compliance_3==0 or compliance_4==0 or compliance_5==0 or compliance_6==0:
            overall_score=0
        else:
            overall_score=ce_total+compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        chat = ChatMonitoringFormPodFather(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                           manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,concept=concept,evaluator=evaluator,

                                     ce_1=ce_1,ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_total=ce_total,

                                     compliance_1=compliance_1,compliance_2=compliance_2,compliance_3=compliance_3,
                                     compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score,category=category
                                     )
        chat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request,'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)

def inboundCoachingForm(request):
    if request.method == 'POST':
        category='inbound'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])
        ce_5 = int(request.POST['ce_5'])
        ce_6 = int(request.POST['ce_6'])
        ce_7 = int(request.POST['ce_7'])
        ce_8 = int(request.POST['ce_8'])
        ce_9 = int(request.POST['ce_9'])
        ce_10 = int(request.POST['ce_10'])
        ce_11 = int(request.POST['ce_11'])

        ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

        # Business
        business_1 = int(request.POST['business_1'])
        business_2 = int(request.POST['business_2'])

        business_total = business_1 + business_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])

        compliance_total = compliance_1 + compliance_2 + compliance_3

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0:
            overall_score = 0
        else:
            overall_score = ce_total + business_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        inbound = InboundMonitoringFormNucleusMedia(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5, ce_6=ce_6, ce_7=ce_7, ce_8=ce_8, ce_9=ce_9, ce_10=ce_10, ce_11=ce_11,
                                           ce_total=ce_total,

                                           business_1=business_1,business_2=business_2,business_total=business_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        inbound.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/ECPL-INBOUND-CALL-MONITORING-FORM.html', data)

def fameHouse(request):
    if request.method == 'POST':
        category='Chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        am=request.POST['am']

        ticket_no=request.POST['ticket_no']
        ticket_type = request.POST['ticket_type']

        trans_date = request.POST['ticketdate']
        audit_date = request.POST['auditdate']

        campaign = request.POST['campaign']


        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        #Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])
        ce_5 = int(request.POST['ce_5'])

        ce_total=ce_1+ce_2+ce_3+ce_4+ce_5

        #ZENDESK
        ze_1 = int(request.POST['ze_1'])
        ze_2 = int(request.POST['ze_2'])
        ze_3 = int(request.POST['ze_3'])
        ze_4 = int(request.POST['ze_4'])

        ze_total = ze_1+ze_2+ze_3+ze_4

        ###SHIPHERO
        sh_1 = int(request.POST['sh_1'])
        sh_2 = int(request.POST['sh_2'])
        sh_3 = int(request.POST['sh_3'])
        sh_4 = int(request.POST['sh_4'])
        sh_5 = int(request.POST['sh_5'])

        sh_total = sh_1+sh_2+sh_3+sh_4+sh_5
        #################################################
        if ze_3 == 0 or ze_4 ==0 or sh_1==0 or sh_2==0 or sh_3==0 or sh_4==0 or sh_5==0:
            overall_score=0
        else:
            overall_score=ce_total+ze_total+sh_total



        #################################################

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']

        added_by = request.user.profile.emp_name

        famehouse = FameHouseMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,am=am,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,

                                    ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5,
                                    ce_total=ce_total,

                                    ze_1=ze_1, ze_2=ze_2, ze_3=ze_3, ze_4=ze_4,
                                    ze_total=ze_total,

                                    sh_1=sh_1, sh_2=sh_2, sh_3=sh_3, sh_4=sh_4, sh_5=sh_5,
                                    sh_total=sh_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,ticket_type=ticket_type,

                                     category=category,overall_score=overall_score
                                     )
        famehouse.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Fame-house-mon-form.html', data)

def flaMonForm(request):
    if request.method == 'POST':
        category='other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        order_id=request.POST['order_id']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        service=request.POST['service']
        check_list=request.POST['checklist']

        #######################################
        prof_obj=Profile.objects.get(emp_id=emp_id)
        manager=prof_obj.manager

        manager_emp_id_obj=Profile.objects.get(emp_name=manager)

        manager_emp_id=manager_emp_id_obj.emp_id
        manager_name=manager
        #########################################

        # Macros
        checklist_1 = int(request.POST['checklist_1'])

        reason_for_failure=request.POST['reason_for_failure']
        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        fla = FLAMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,order_id=order_id,
                                     campaign=campaign,concept=concept,service=service,

                                     check_list=check_list,
                                     checklist_1=checklist_1,

                                     reason_for_failure=reason_for_failure,
                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=checklist_1,category=category
                                     )
        fla.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/FLA-mon-form.html', data)


def leadsandSalesMonForm(request):
    if request.method == 'POST':
        category='leads'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])
        softskill_6 = int(request.POST['softskill_6'])
        softskill_7 = int(request.POST['softskill_7'])

        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5+softskill_6+softskill_7

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total + compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MasterMonitoringFormMTCosmetics(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_6=softskill_6,softskill_7=softskill_7,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Lead-Sales-MONITORING-FORM.html', data)

def emailAndChatmonForm(request):
    if request.method == 'POST':
        category='chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        trans_date = request.POST['trans_date']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])
        ce_5 = int(request.POST['ce_5'])
        ce_6 = int(request.POST['ce_6'])
        ce_7 = int(request.POST['ce_7'])
        ce_8 = int(request.POST['ce_8'])
        ce_9 = int(request.POST['ce_9'])
        ce_10 = int(request.POST['ce_10'])
        ce_11 = int(request.POST['ce_11'])

        ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

        # Business
        business_1 = int(request.POST['business_1'])
        business_2 = int(request.POST['business_2'])

        business_total = business_1 + business_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])


        compliance_total = compliance_1 + compliance_2

        if compliance_1 == 0 or compliance_2 == 0 :
            overall_score = 0
        else:
            overall_score = ce_total + business_total + compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        emailchat = MasterMonitoringFormTonnChatsEmail(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           trans_date=trans_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,duration=duration,

                                           ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5, ce_6=ce_6, ce_7=ce_7, ce_8=ce_8, ce_9=ce_9, ce_10=ce_10, ce_11=ce_11,
                                           ce_total=ce_total,

                                           business_1=business_1,business_2=business_2,business_total=business_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        emailchat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/ECPL-Chat-Email-MONITORING-FORM.html', data)

def movementInsurance(request):
    if request.method == 'POST':
        category='leads'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])
        softskill_6 = int(request.POST['softskill_6'])
        softskill_7 = int(request.POST['softskill_7'])

        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5+softskill_6+softskill_7

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        moveins = MasterMonitoringFormMovementInsurance(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_6=softskill_6,softskill_7=softskill_7,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        moveins.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Master-Monitoring-Form-Movement-Insurance.html', data)

def witDigitel(request):
    if request.method == 'POST':
        category='other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customer_contact']

        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']

        campaign = request.POST['campaign']
        concept = request.POST['concept']
        service=request.POST['service']
        call_duration=request.POST['call_duration']
        call_type=request.POST['call_type']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Tagging
        tagging_1 = int(request.POST['tagging_1'])


        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        wit = WitDigitalMasteringMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     call_date=call_date, audit_date=audit_date,customer_name=customer_name,customer_contact=customer_contact,
                                     campaign=campaign,concept=concept,service=service,
                                        call_duration=call_duration,call_type=call_type,
                                     tagging_1=tagging_1,
                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=tagging_1,category=category
                                     )
        wit.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/FLA-mon-form.html', data)

def printerPixChatsEmails(request):
    if request.method == 'POST':
        category='chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        trans_date = request.POST['trans_date']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])
        ce_5 = int(request.POST['ce_5'])
        ce_6 = int(request.POST['ce_6'])
        ce_7 = int(request.POST['ce_7'])
        ce_8 = int(request.POST['ce_8'])
        ce_9 = int(request.POST['ce_9'])
        ce_10 = int(request.POST['ce_10'])
        ce_11 = int(request.POST['ce_11'])

        ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

        # Business
        business_1 = int(request.POST['business_1'])
        business_2 = int(request.POST['business_2'])

        business_total = business_1 + business_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])



        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 :
            overall_score = 0
        else:
            overall_score = ce_total + business_total + compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        emailchat = PrinterPixMasterMonitoringFormChatsEmail(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           trans_date=trans_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,duration=duration,

                                           ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5, ce_6=ce_6, ce_7=ce_7, ce_8=ce_8, ce_9=ce_9, ce_10=ce_10, ce_11=ce_11,
                                           ce_total=ce_total,

                                           business_1=business_1,business_2=business_2,business_total=business_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,
                                           compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        emailchat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Chats-Email.html', data)

def printerPixInboundCalls(request):
    if request.method == 'POST':
        category='inbound'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])
        ce_5 = int(request.POST['ce_5'])
        ce_6 = int(request.POST['ce_6'])
        ce_7 = int(request.POST['ce_7'])
        ce_8 = int(request.POST['ce_8'])
        ce_9 = int(request.POST['ce_9'])
        ce_10 = int(request.POST['ce_10'])
        ce_11 = int(request.POST['ce_11'])

        ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

        # Business
        business_1 = int(request.POST['business_1'])
        business_2 = int(request.POST['business_2'])

        business_total = business_1 + business_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0:
            overall_score = 0
        else:
            overall_score = ce_total + business_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        inbound = PrinterPixMasterMonitoringFormInboundCalls(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5, ce_6=ce_6, ce_7=ce_7, ce_8=ce_8, ce_9=ce_9, ce_10=ce_10, ce_11=ce_11,
                                           ce_total=ce_total,

                                           business_1=business_1,business_2=business_2,business_total=business_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,
                                           compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        inbound.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Inbound-Calls.html', data)

def leadsandSalesAadya(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsAadhyaSolution(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Lead-Sales-MONITORING-FORM.html', data)

def leadsandSalesInsalvage(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsInsalvage(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-Insalvage.html', data)

def leadsandSalesMedicare(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsMedicare(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-Medicare.html', data)

def leadsandSalesCTS(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsCTS(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-CTS.html', data)

def leadsandSalesTenamusFood(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsTentamusFood(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Tentamus-Food.html', data)

def leadsandSalesTenamusPet(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsTentamusPet(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Tentamus-Pet.html', data)

def leadsandSalesCitySecurity(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsCitySecurity(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-City-Security.html', data)

def leadsandSalesAllenConsulting(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsAllenConsulting(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Allen-Consulting.html', data)

def leadsandSalesSystem4(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsSystem4(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-system4.html', data)

def leadsandSalesLouisville(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsLouisville(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Louisville.html', data)

def leadsandSalesInfoThink(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsInfothinkLLC(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-Info-Think-LLC.html', data)

def leadsandSalesPSECU(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsPSECU(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-PSECU.html', data)

def leadsandSalesGetRates(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsGetARates(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-Get-A-Rates.html', data)

def leadsandSalesAdvance(request):
    if request.method == 'POST':

        category='leads'

        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name=request.POST['customer']
        customer_contact=request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone=request.POST['zone']
        call_duration=request.POST['duration']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Opening and Closing
        oc_1 = int(request.POST['oc_1'])
        oc_2 = int(request.POST['oc_2'])
        oc_3 = int(request.POST['oc_3'])


        oc_total = oc_1 + oc_2 + oc_3

        # Softskills
        softskill_1 = int(request.POST['softskill_1'])
        softskill_2 = int(request.POST['softskill_2'])
        softskill_3 = int(request.POST['softskill_3'])
        softskill_4 = int(request.POST['softskill_4'])
        softskill_5 = int(request.POST['softskill_5'])


        softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
        else:
            overall_score = oc_total + softskill_total +compliance_total

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        leadsales = MonitoringFormLeadsAdvanceConsultants(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name,manager_id=manager_emp_id,

                                           call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                           campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,

                                           oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,

                                           softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                                      compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score,category=category
                                           )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/Monitoring-Form-Leads-Advance-Consultant.html', data)


#campaign View

def campaignView(request,pk):
    team=Team.objects.get(id=pk)
    team_name=team.name
    agents=Profile.objects.filter(team=team_name,emp_desi='CRO')

    data = {'team': team,'agents':agents}
    return render(request,'campaign-view.html',data)

def selectCoachingForm(request):
    if request.method == 'POST':
        audit_form=request.POST['audit_form']
        agent=request.POST['agent']
        team=request.POST['team']

        if audit_form=='eva-chat':
            agent=Profile.objects.get(emp_name=agent)
            team=Team.objects.get(name=team)
            data = {'agent':agent,'team':team}
            return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)
        elif audit_form=='pod-chat':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)
        elif audit_form=='inbound-call':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-INBOUND-CALL-MONITORING-FORM.html', data)
        elif audit_form=='fame-house':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Fame-house-mon-form.html', data)
        elif audit_form=='FLA':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/FLA-mon-form.html', data)
        elif audit_form=='lead-sales':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Lead-Sales-MONITORING-FORM.html', data)
        elif audit_form=='email-chat':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-Chat-Email-MONITORING-FORM.html', data)
        elif audit_form=='mov-ins':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Master-Monitoring-Form-Movement-Insurance.html', data)
        elif audit_form=='wit-digital':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Wit-Digital-Mastering-Monitoring-Form.html', data)
        elif audit_form == 'pix-chat-email':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Chats-Email.html', data)
        elif audit_form == 'pix-inbound':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Inbound-Calls.html', data)
        elif audit_form == 'lead-aadya':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Aadhya-Solution.html', data)
        elif audit_form == 'insalvage':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Insalvage.html', data)
        elif audit_form == 'medicare':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Medicare.html', data)
        elif audit_form == 'cts':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-CTS.html', data)
        elif audit_form == 'tentamus-food':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Tentamus-Food.html', data)
        elif audit_form == 'tentamus-pet':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Tentamus-Pet.html', data)
        elif audit_form == 'city-sec':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-City-Security.html', data)
        elif audit_form == 'allen':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Allen-Consulting.html', data)
        elif audit_form == 'system4':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-System4.html', data)
        elif audit_form == 'louisville':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Louisville.html', data)
        elif audit_form == 'info-think':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Info-Think-LLC.html', data)
        elif audit_form == 'psecu':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-PSECU.html', data)
        elif audit_form == 'get-rates':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Get-A-Rates.html', data)
        elif audit_form == 'advance':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Monitoring-Form-Leads-Advance-Consultant.html', data)

    else:
        return redirect('/employees/qahome')

def coachingSummaryView(request):
    return render(request,'coaching-summary-view.html')

def qualityDashboard(request):

    return render(request,'quality-dashboard.html')

