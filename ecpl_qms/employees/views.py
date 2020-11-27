from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile,Team,OutboundMonitoringForm,InboundMonitoringForm,EmailMonitoringForm,ChatMonitorinForm
from . import forms
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    return render(request,'index.html')


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

            if user.profile.emp_desi=='qa':
                return redirect('/employees/qahome')

            else:
                return redirect('/employees/agenthome')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/employees/login')


def agenthome(request):
    user = request.user.profile.emp_name
    team_name=request.user.profile.team

    out_coachings = OutboundMonitoringForm.objects.filter(associate_name=user)
    out_counts = OutboundMonitoringForm.objects.filter(associate_name=user).count()
    open_out = OutboundMonitoringForm.objects.filter(associate_name=user,status=False)

    in_coachings=InboundMonitoringForm.objects.filter(associate_name=user)
    in_counts=InboundMonitoringForm.objects.filter(associate_name=user).count()
    open_in=InboundMonitoringForm.objects.filter(associate_name=user,status=False)

    email_coachings=EmailMonitoringForm.objects.filter(associate_name=user)
    email_counts=EmailMonitoringForm.objects.filter(associate_name=user).count()
    open_email=EmailMonitoringForm.objects.filter(associate_name=user,status=False)

    chat_coachings = ChatMonitorinForm.objects.filter(associate_name=user)
    chat_counts = ChatMonitorinForm.objects.filter(associate_name=user).count()
    open_chat = ChatMonitorinForm.objects.filter(associate_name=user, status=False)


    team=Team.objects.get(name=team_name)

    data={'out_coachings':out_coachings,'in_coachings':in_coachings,'email_coachings':email_coachings,'chat_coachings':chat_coachings,

          'out_counts':out_counts,'in_counts':in_counts,'email_counts':email_counts,'chat_counts':chat_counts,
          'open_out':open_out,'open_in':open_in,'open_email':open_email,'open_chat':open_chat,'team':team}

    return render(request, 'agent-home.html',data)


def empCoachingViewOutbound(request,pk):
    coaching=OutboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'emp-coaching-view-outbound.html',data)

def empCoachingViewInbound(request,pk):
    coaching=InboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'emp-coaching-view-inbound.html',data)
def empCoachingViewEmail(request,pk):
    coaching = EmailMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'emp-coaching-view-email.html', data)


def empCoachingViewChat(request,pk):
    coaching = OutboundMonitoringForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'emp-coaching-view-chat.html', data)

def qaCoachingView(request,pk):
    coaching=OutboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'qa-coaching-view.html',data)


def signCoaching(request,pk):
    now = datetime.now()
    category=request.POST['category']

    if category == 'outbound':
        coaching=OutboundMonitoringForm.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.save()
        return redirect('/employees/agenthome')
    elif category=='inbound':
        coaching = InboundMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.save()
        return redirect('/employees/agenthome')
    elif category=='chat':
        coaching = ChatMonitorinForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.save()
        return redirect('/employees/agenthome')
    elif category=='email':
        coaching = EmailMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.save()
        return redirect('/employees/agenthome')



def qahome(request):
    user=request.user.profile.emp_name
    coachings=OutboundMonitoringForm.objects.filter(added_by=user).order_by('id').reverse()[:8]

    counts=OutboundMonitoringForm.objects.filter(added_by=user).count()

    opencounts = OutboundMonitoringForm.objects.filter(added_by=user,status=False).count()

    data={'coachings':coachings,'counts':counts,'opencounts':opencounts}

    return render(request,'qa-home.html',data)

def outboundCoachingform(request):

    if request.method== 'POST':

        associate_name=request.POST['empname']
        emp_id=request.POST['empid']
        qa=request.POST['qa']
        team_lead=request.POST['tl']
        customer_name=request.POST['cname']
        customer_contact=request.POST['ccontact']
        call_date=request.POST['calldate']
        audit_date=request.POST['auditdate']
        campaign=request.POST['campaign']
        zone=request.POST['zone']
        concept=request.POST['concept']
        call_duration=request.POST['callduration']


        opening_1=request.POST['opening_1']
        opening_2=request.POST['opening_2']

        x=categoryOne(opening_1)
        y=categoryOne(opening_2)
        op_total=x+y
        print(op_total)

        softskill_1=request.POST['softskill_1']
        softskill_2 = request.POST['softskill_2']
        softskill_3 = request.POST['softskill_3']
        softskill_4 = request.POST['softskill_4']

        n1=categoryOne(softskill_1)
        n2=categoryOne(softskill_2)
        n3=categoryOne(softskill_3)
        n4=categoryOne(softskill_4)

        softskill_5 = request.POST['softskill_5']
        softskill_6 = request.POST['softskill_6']

        n5=categoryTwo(softskill_5)
        n6=categoryTwo(softskill_6)
        sf_total=n1+n2+n3+n4+n5+n6
        print(sf_total)

        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']
        business_3 = request.POST['business_3']

        b1=categoryTwo(business_1)
        b2=categoryTwo(business_2)
        b3=categoryTwo(business_3)
        bs_total=b1+b2+b3
        print(bs_total)

        closing_1=request.POST['closing_1']
        closing_2 = request.POST['closing_2']

        c1=categoryTwo(closing_1)
        c2=categoryTwo(closing_2)
        cl_total=c1+c2
        print(cl_total)

        compliance_1=request.POST['compliance_1']
        compliance_2 = request.POST['compliance_2']
        compliance_3 = request.POST['compliance_3']

        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        comments=request.POST['comments']

        total_score=op_total+sf_total+bs_total+cl_total
        added_by=request.user.profile.emp_name

        outbound=OutboundMonitoringForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                        customer_contact=customer_contact,call_date=call_date,audit_date=audit_date,campaign=campaign,
                                        zone=zone,concept=concept,call_duration=call_duration,opening_1=opening_1,opening_2=opening_2,
                                        softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,
                                        softskill_5=softskill_5,softskill_6=softskill_6,business_1=business_1,business_2=business_2,
                                        business_3=business_3,closing_1=closing_1,closing_2=closing_2,compliance_1=compliance_1,
                                        compliance_2=compliance_2,compliance_3=compliance_3,areas_improvement=areas_improvement,
                                        positives=positives,comments=comments,
                                        opening_total=op_total,softskill_total=sf_total,business_total=bs_total,
                                        closing_total=cl_total,total_score=total_score,added_by=added_by,

                                        )
        outbound.save()
        return redirect('/employees/qahome')



    else:

        team_name = request.user.profile.team
        team = Team.objects.get(name=team_name)
        users = User.objects.all()
        data={'team':team,'users':users}
        return render(request, 'outbound-coaching-form.html',data)

def inboundCoachingform(request):

    if request.method== 'POST':

        associate_name=request.POST['empname']
        emp_id=request.POST['empid']
        qa=request.POST['qa']
        team_lead=request.POST['tl']
        customer_name=request.POST['cname']
        customer_contact=request.POST['ccontact']
        call_date=request.POST['calldate']
        audit_date=request.POST['auditdate']
        campaign=request.POST['campaign']
        zone=request.POST['zone']
        concept=request.POST['concept']
        call_duration=request.POST['callduration']


        opening_1=request.POST['opening_1']
        opening_2=request.POST['opening_2']

        x=categoryOne(opening_1)
        y=categoryOne(opening_2)
        op_total=x+y
        print(op_total)

        softskill_1=request.POST['softskill_1']
        softskill_2 = request.POST['softskill_2']
        softskill_3 = request.POST['softskill_3']
        softskill_4 = request.POST['softskill_4']

        n1=categoryOne(softskill_1)
        n2=categoryOne(softskill_2)
        n3=categoryOne(softskill_3)
        n4=categoryOne(softskill_4)

        softskill_5 = request.POST['softskill_5']
        softskill_6 = request.POST['softskill_6']

        n5=categoryTwo(softskill_5)
        n6=categoryTwo(softskill_6)
        sf_total=n1+n2+n3+n4+n5+n6
        print(sf_total)

        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']
        business_3 = request.POST['business_3']

        b1=categoryTwo(business_1)
        b2=categoryTwo(business_2)
        b3=categoryTwo(business_3)
        bs_total=b1+b2+b3
        print(bs_total)

        closing_1=request.POST['closing_1']
        closing_2 = request.POST['closing_2']

        c1=categoryTwo(closing_1)
        c2=categoryTwo(closing_2)
        cl_total=c1+c2
        print(cl_total)

        compliance_1=request.POST['compliance_1']
        compliance_2 = request.POST['compliance_2']
        compliance_3 = request.POST['compliance_3']

        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        comments=request.POST['comments']

        total_score=op_total+sf_total+bs_total+cl_total
        added_by=request.user.profile.emp_name

        inbound=InboundMonitoringForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                        customer_contact=customer_contact,call_date=call_date,audit_date=audit_date,campaign=campaign,
                                        zone=zone,concept=concept,call_duration=call_duration,opening_1=opening_1,opening_2=opening_2,
                                        softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,
                                        softskill_5=softskill_5,softskill_6=softskill_6,business_1=business_1,business_2=business_2,
                                        business_3=business_3,closing_1=closing_1,closing_2=closing_2,compliance_1=compliance_1,
                                        compliance_2=compliance_2,compliance_3=compliance_3,areas_improvement=areas_improvement,
                                        positives=positives,comments=comments,
                                        opening_total=op_total,softskill_total=sf_total,business_total=bs_total,
                                        closing_total=cl_total,total_score=total_score,added_by=added_by,

                                        )
        inbound.save()
        return redirect('/employees/qahome')



    else:

        team_name = request.user.profile.team
        team = Team.objects.get(name=team_name)
        users = User.objects.all()
        data={'team':team,'users':users}
        return render(request, 'inbound-coaching-form.html',data)

def emailmonitoringform(request):

    if request.method== 'POST':

        associate_name=request.POST['empname']
        emp_id=request.POST['empid']
        qa=request.POST['qa']
        team_lead=request.POST['tl']
        customer_name=request.POST['cname']
        record_no=request.POST['recordnumber']

        email_date=request.POST['emaildate']
        audit_date=request.POST['auditdate']
        campaign=request.POST['campaign']
        zone=request.POST['zone']
        concept=request.POST['concept']
        ticket_no=request.POST['ticketnumber']

        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']

        ce_1=request.POST['ce_1']
        ce_2 = request.POST['ce_2']
        ce_3 = request.POST['ce_3']
        ce_4 = request.POST['ce_4']
        ce_5 = request.POST['ce_5']
        ce_6 = request.POST['ce_6']

        compliance_1=request.POST['compliance_1']
        compliance_2 = request.POST['compliance_2']
        compliance_3 = request.POST['compliance_3']

        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        customer_feedback=request.POST['cfeedback']

        #total_score=op_total+sf_total+bs_total+cl_total
        added_by=request.user.profile.emp_name

        email=EmailMonitoringForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                  record_no=record_no,email_date=email_date,audit_date=audit_date,campaign=campaign,zone=zone,
                                  concept=concept,ticket_no=ticket_no,business_1=business_1,business_2=business_2,ce_1=ce_1,
                                  ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_5=ce_5,ce_6=ce_6,compliance_1=compliance_1,compliance_2=compliance_2,
                                  compliance_3=compliance_3,areas_improvement=areas_improvement,positives=positives,customer_feedback=customer_feedback,
                                  added_by=added_by)
        email.save()
        return redirect('/employees/qahome')



    else:

        team_name = request.user.profile.team
        team = Team.objects.get(name=team_name)
        users = User.objects.all()
        data={'team':team,'users':users}
        return render(request, 'email-coaching-form.html',data)

def chatmonitoringform(request):

    if request.method== 'POST':

        associate_name=request.POST['empname']
        emp_id=request.POST['empid']
        qa=request.POST['qa']
        team_lead=request.POST['tl']
        customer_name=request.POST['cname']
        record_no=request.POST['recordnumber']

        chat_date=request.POST['chatdate']
        audit_date=request.POST['auditdate']
        campaign=request.POST['campaign']
        zone=request.POST['zone']
        concept=request.POST['concept']
        ticket_no=request.POST['ticketnumber']

        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']

        ce_1=request.POST['ce_1']
        ce_2 = request.POST['ce_2']
        ce_3 = request.POST['ce_3']
        ce_4 = request.POST['ce_4']
        ce_5 = request.POST['ce_5']
        ce_6 = request.POST['ce_6']

        compliance_1=request.POST['compliance_1']
        compliance_2 = request.POST['compliance_2']
        compliance_3 = request.POST['compliance_3']

        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        customer_feedback=request.POST['cfeedback']

        #total_score=op_total+sf_total+bs_total+cl_total
        added_by=request.user.profile.emp_name

        chat=ChatMonitorinForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                  record_no=record_no,chat_date=chat_date,audit_date=audit_date,campaign=campaign,zone=zone,
                                  concept=concept,ticket_no=ticket_no,business_1=business_1,business_2=business_2,ce_1=ce_1,
                                  ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_5=ce_5,ce_6=ce_6,compliance_1=compliance_1,compliance_2=compliance_2,
                                  compliance_3=compliance_3,areas_improvement=areas_improvement,positives=positives,customer_feedback=customer_feedback,
                                  added_by=added_by)
        chat.save()
        return redirect('/employees/qahome')



    else:

        team_name = request.user.profile.team
        team = Team.objects.get(name=team_name)
        users = User.objects.all()
        data={'team':team,'users':users}
        return render(request, 'chat-coaching-form.html',data)


#calculation

def categoryOne(val):

    if val=='good':
        return 5
    elif val=='average':
        return 3
    else:
        return 1

def categoryTwo(val):

    if val=='good':
        return 10
    elif val=='average':
        return 6
    else:
        return 2

