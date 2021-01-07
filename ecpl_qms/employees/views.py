from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import *

from . import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages

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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # form to create user
        profile_form = forms.ProfileCreation(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # login(request,user)
            return render(request,'index.html')
    else:
        form = UserCreationForm()
        profile_form = forms.ProfileCreation()

    return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form})


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
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/employees/login')

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

        coaching_eva = ChatMonitoringFormEva.objects.filter(emp_id=emp_id)

        ce_total = []
        for i in coaching_eva:
            ce_total.append(i.ce_total)
        if len(ce_total) > 0:
            ce_avg = sum(ce_total) / len(ce_total)
            ce_perc = (ce_avg / 40) * 100
        else:
            ce_perc = 100

        co_total = []
        for i in coaching_eva:
            co_total.append(i.compliance_total)
        if len(co_total) > 0:
            co_avg = sum(co_total) / len(co_total)
            co_perc=(co_avg/60)*100

        else:
            co_perc = 100

        overall_total = []
        for i in coaching_eva:
            overall_total.append(i.overall_score)
        if len(overall_total) > 0:
            ov_perc = sum(overall_total) / len(overall_total)

        else:
            ov_perc = 100

        eva_details = {'name': 'EVA Chat', 'ce_avg': ce_perc, 'co_avg': co_perc,'ov_avg':ov_perc}

        # --------------------

        coaching_eva = ChatMonitoringFormPodFather.objects.filter(emp_id=emp_id)

        ce_total = []
        for i in coaching_eva:
            ce_total.append(i.ce_total)
        if len(ce_total) > 0:
            ce_avg = sum(ce_total) / len(ce_total)
            ce_perc = (ce_avg / 40) * 100
        else:
            ce_perc = 100

        co_total = []
        for i in coaching_eva:
            co_total.append(i.compliance_total)
        if len(co_total) > 0:
            co_avg = sum(co_total) / len(co_total)
            co_perc=(co_avg/60)*100
        else:
            co_perc = 100

        overall_total = []
        for i in coaching_eva:
            overall_total.append(i.overall_score)
        if len(overall_total) > 0:
            ov_perc = sum(overall_total) / len(overall_total)
        else:
            ov_perc = 100

        pod_details = {'name': 'POD Chat', 'ce_avg': ce_perc, 'co_avg': co_perc,'ov_avg':ov_perc}



        campaign_details=[eva_details,pod_details,
                          ]

        data={'campaign':campaign_details,'profile':profile}

        return render(request,'employee-wise-report.html',data)


def managerWiseReport(request):
    if request.method == 'POST':
        manager_emp_id=request.POST['emp_id']
        profile=Profile.objects.get(emp_id=manager_emp_id)
        manager_name=profile.emp_name

        coaching_eva = ChatMonitoringFormEva.objects.filter(manager_id=manager_emp_id)

        ce_total = []
        for i in coaching_eva:
            ce_total.append(i.ce_total)
        if len(ce_total) > 0:
            ce_avg = sum(ce_total) / len(ce_total)
            ce_perc = (ce_avg / 40) * 100
        else:
            ce_perc = 100

        co_total = []
        for i in coaching_eva:
            co_total.append(i.compliance_total)
        if len(co_total) > 0:
            co_avg = sum(co_total) / len(co_total)
            co_perc=(co_avg/60)*100

        else:
            co_perc = 100

        overall_total = []
        for i in coaching_eva:
            overall_total.append(i.overall_score)
        if len(overall_total) > 0:
            ov_perc = sum(overall_total) / len(overall_total)

        else:
            ov_perc = 100

        eva_details = {'name': 'EVA Chat', 'ce_avg': ce_perc, 'co_avg': co_perc,'ov_avg':ov_perc}

        # --------------------

        coaching_eva = ChatMonitoringFormPodFather.objects.filter(manager_id=manager_emp_id)

        ce_total = []
        for i in coaching_eva:
            ce_total.append(i.ce_total)
        if len(ce_total) > 0:
            ce_avg = sum(ce_total) / len(ce_total)
            ce_perc = (ce_avg / 40) * 100
        else:
            ce_perc = 100

        co_total = []
        for i in coaching_eva:
            co_total.append(i.compliance_total)
        if len(co_total) > 0:
            co_avg = sum(co_total) / len(co_total)
            co_perc=(co_avg/60)*100
        else:
            co_perc = 100

        overall_total = []
        for i in coaching_eva:
            overall_total.append(i.overall_score)
        if len(overall_total) > 0:
            ov_perc = sum(overall_total) / len(overall_total)
        else:
            ov_perc = 100

        pod_details = {'name': 'POD Chat', 'ce_avg': ce_perc, 'co_avg': co_perc,'ov_avg':ov_perc}



        campaign_details=[eva_details,pod_details,
                          ]

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


    # Eva Chat Details
    eva_all = ChatMonitoringFormEva.objects.all()
    eva_all_count = ChatMonitoringFormEva.objects.all().count()
    open_eva_chat = ChatMonitoringFormEva.objects.filter(status=False)
    open_eva_count = ChatMonitoringFormEva.objects.filter(status=False).count()

    eva_avg_score=ChatMonitoringFormEva.objects.filter(audit_date__year=year,audit_date__month=month)
    eva_avg=[]
    for i in eva_avg_score:
        eva_avg.append(i.overall_score)
    if len(eva_avg)>0:
        eva_avg_score=sum(eva_avg)/len(eva_avg)
    else:
        eva_avg_score=100



    # Pod Father Chat Details
    pod_all = ChatMonitoringFormPodFather.objects.all()
    pod_all_count = ChatMonitoringFormPodFather.objects.all().count()
    open_pod_chat = ChatMonitoringFormPodFather.objects.filter(status=False)
    open_pod_count = ChatMonitoringFormPodFather.objects.filter(status=False).count()

    pod_avg_score = ChatMonitoringFormPodFather.objects.filter(audit_date__year=year, audit_date__month=month)
    pod_avg = []
    for i in pod_avg_score:
        pod_avg.append(i.overall_score)
    if len(pod_avg) > 0:
        pod_avg_score = sum(pod_avg) / len(pod_avg)
    else:
        pod_avg_score = 100




    #Categorywise


    chat=(eva_avg_score+pod_avg_score)/2
    outbound=100
    email=100



    # Coaching closure

    user_id = request.user.id

    employees = Profile.objects.filter(emp_desi='CRO')

    eva_total = ChatMonitoringFormEva.objects.all().count()
    eva_open_total = ChatMonitoringFormEva.objects.filter(status=False).count()
    closed_percentage_eva = int((eva_open_total / eva_total) * 100)

    pod_total = ChatMonitoringFormPodFather.objects.all().count()
    pod_open_total = ChatMonitoringFormPodFather.objects.filter(status=False).count()
    closed_percentage_pod = int((pod_open_total / pod_total) * 100)



    pod = {'name': 'Noom-POD', 'total': pod_total, 'total_open': pod_open_total, 'perc': closed_percentage_pod}
    eva = {'name': 'Noom-EVA', 'total': eva_total, 'total_open': eva_open_total, 'perc': closed_percentage_eva}


    campaigns = [pod, eva,]

    data = {

            'open_eva_chat': open_eva_chat, 'open_eva_count': open_eva_count,'eva_all':eva_all,'eva_all_count':eva_all_count,
            'open_pod_chat': open_pod_chat, 'open_pod_count': open_pod_count,'pod_all':pod_all,'pod_all_count':pod_all_count,


            'eva_avg_score':eva_avg_score,'pod_avg_score':pod_avg_score,

            'chat':chat,'outbound':outbound,'email':email,

            'employees':employees,'managers':managers,'campaigns':campaigns

            }

    return render(request, 'quality-dashboard-management.html',data)

def agenthome(request):

    agent_name = request.user.profile.emp_name
    team_name=request.user.profile.team
    team = Team.objects.get(name=team_name)


    # Chat Eva Details
    open_eva_chat=ChatMonitoringFormEva.objects.filter(associate_name=agent_name, status=False)
    open_eva_count = ChatMonitoringFormEva.objects.filter(associate_name=agent_name, status=False).count()


    # Pod Father Chat Details
    open_pod_chat = ChatMonitoringFormPodFather.objects.filter(associate_name=agent_name, status=False)
    open_pod_count = ChatMonitoringFormPodFather.objects.filter(associate_name=agent_name, status=False).count()



    data={'team':team,
          'open_eva_chat':open_eva_chat,'open_eva_count':open_eva_count,
          'open_pod_chat':open_pod_chat,'open_pod_count':open_pod_count,

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




# Open status Coaching View
def qacoachingViewOpenAll(request,pk):
    if pk>0:

        qa_name=request.user.profile.emp_name

        coaching_chat_eva = ChatMonitoringFormEva.objects.filter(added_by=qa_name, status=False)
        coaching_chat_pod = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False)
        data={
                'coaching_chat_eva':coaching_chat_eva,'coaching_chat_pod':coaching_chat_pod,
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

        if status=='all':

            coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name)
            coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name)
        else:

            coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status)
            coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status)

        data={
                'coaching_eva_chat':coaching_eva_chat,'coaching_pod_chat':coaching_pod_chat,
             }

        return render(request,'campaign-wise-coaching-view.html',data)
    else:
        return redirect('/employees/qahome')

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
            else:

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status,emp_id=emp_id,audit_date__range=[start_date,end_date])
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status,emp_id=emp_id,audit_date__range=[start_date,end_date])

            data={
                    'coaching_eva_chat':coaching_eva_chat,'coaching_pod_chat':coaching_pod_chat,
                 }

            return render(request,'campaign-wise-coaching-view-agent.html',data)
        else:
            if status=='all':

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,emp_id=emp_id)
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,emp_id=emp_id)
            else:

                coaching_eva_chat = ChatMonitoringFormEva.objects.filter(campaign=team_name,status=status,emp_id=emp_id)
                coaching_pod_chat = ChatMonitoringFormPodFather.objects.filter(campaign=team_name,status=status,emp_id=emp_id)

            data={
                    'coaching_eva_chat':coaching_eva_chat,'coaching_pod_chat':coaching_pod_chat,
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
    teams=Team.objects.filter(qa=user_id)

    # Eva Chat Details
    open_eva_chat=ChatMonitoringFormEva.objects.filter(added_by=qa_name,status=False)
    open_eva_count = ChatMonitoringFormEva.objects.filter(added_by=qa_name,status=False).count()

    # Pod Father Chat Details
    open_pod_chat = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False)
    open_pod_count = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False).count()



    total_open=open_eva_count+open_pod_count


    data={'teams':teams,
          'open_eva_chat':open_eva_chat,'open_eva_count':open_eva_count,
          'open_pod_chat':open_pod_chat,'open_pod_count':open_pod_count,

          'total_open':total_open,
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

        team=Team.objects.get(name=campaign)
        manager_id=team.manager
        manager_emp_id=manager_id.profile.emp_id
        manager_name=Profile.objects.get(emp_id=manager_emp_id)


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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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
        category='other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no=request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        service=request.POST['service']

        team=Team.objects.get(name=campaign)
        manager_id=team.manager
        manager_emp_id=manager_id.profile.emp_id
        manager_name=Profile.objects.get(emp_id=manager_emp_id)


        # Macros
        macros_1 = int(request.POST['macros_1'])

        reason_for_failure = request.POST['reason_for_failure']
        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        famehouse = FameHouseMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,concept=concept,service=service,

                                     macros_1=macros_1,

                                     reason_for_failure=reason_for_failure,
                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=macros_1,category=category
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

        team=Team.objects.get(name=campaign)
        manager_id=team.manager
        manager_emp_id=manager_id.profile.emp_id
        manager_name=Profile.objects.get(emp_id=manager_emp_id)


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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        team=Team.objects.get(name=campaign)
        manager_id=team.manager
        manager_emp_id=manager_id.profile.emp_id
        manager_name=Profile.objects.get(emp_id=manager_emp_id)


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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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



        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 +compliance_5

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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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


def leadsandSalesMonFormPsecu(request):
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

        team = Team.objects.get(name=campaign)
        manager_id = team.manager
        manager_emp_id = manager_id.profile.emp_id
        manager_name = Profile.objects.get(emp_id=manager_emp_id)

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

        leadsales = MasterMonitoringFormGetaRatesPSECU(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
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
        return render(request, 'mon-forms/PSECU-Lead-Sales-MONITORING-FORM.html', data)

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
        elif audit_form == 'lead-psecu':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/PSECU-Lead-Sales-MONITORING-FORM.html', data)
    else:
        return redirect('/employees/qahome')

def coachingSummaryView(request):
    return render(request,'coaching-summary-view.html')

def qualityDashboard(request):
    if request.user.profile.emp_desi=='QA':

        qa_id=request.user.id
        qa_name=request.user.profile.emp_name
        teams=Team.objects.filter(qa=qa_id)

        # Eva Chat Details
        all_eva=ChatMonitoringFormEva.objects.filter(added_by=qa_name)
        all_eva_count = ChatMonitoringFormEva.objects.filter(added_by=qa_name).count()
        open_eva_chat = ChatMonitoringFormEva.objects.filter(added_by=qa_name, status=False)
        open_eva_count = ChatMonitoringFormEva.objects.filter(added_by=qa_name, status=False).count()

        # Pod Father Chat Details
        all_pod=ChatMonitoringFormPodFather.objects.filter(added_by=qa_name).count()
        all_pod_count = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name)
        open_pod_chat = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False)
        open_pod_count = ChatMonitoringFormPodFather.objects.filter(added_by=qa_name, status=False).count()


        data={

        }

        return render(request,'quality-dashboard.html',data)

    else:
        pass

