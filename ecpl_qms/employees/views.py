from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile,Team,OutboundMonitoringForm,InboundMonitoringForm,EmailMonitoringForm,ChatMonitorinForm,SurveyMonitorinForm
from .models import LeadSalesMonitoringForm
from . import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages

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

            if user.profile.emp_desi=='QA':
                return redirect('/employees/qahome')

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


def agenthome(request):
    user = request.user.profile.emp_name
    team_name=request.user.profile.team

    out_coachings = OutboundMonitoringForm.objects.filter(associate_name=user)
    out_counts = OutboundMonitoringForm.objects.filter(associate_name=user).count()
    open_out = OutboundMonitoringForm.objects.filter(associate_name=user,status=False)
    open_out_count = OutboundMonitoringForm.objects.filter(associate_name=user, status=False).count()

    in_coachings=InboundMonitoringForm.objects.filter(associate_name=user)
    in_counts=InboundMonitoringForm.objects.filter(associate_name=user).count()
    open_in=InboundMonitoringForm.objects.filter(associate_name=user,status=False)
    open_in_count = InboundMonitoringForm.objects.filter(associate_name=user, status=False).count()

    email_coachings=EmailMonitoringForm.objects.filter(associate_name=user)
    email_counts=EmailMonitoringForm.objects.filter(associate_name=user).count()
    open_email=EmailMonitoringForm.objects.filter(associate_name=user,status=False)
    open_email_count = EmailMonitoringForm.objects.filter(associate_name=user, status=False).count()

    chat_coachings = ChatMonitorinForm.objects.filter(associate_name=user)
    chat_counts = ChatMonitorinForm.objects.filter(associate_name=user).count()
    open_chat = ChatMonitorinForm.objects.filter(associate_name=user, status=False)
    open_chat_count = ChatMonitorinForm.objects.filter(associate_name=user, status=False).count()


    team=Team.objects.get(name=team_name)

    data={'out_coachings':out_coachings,'in_coachings':in_coachings,'email_coachings':email_coachings,'chat_coachings':chat_coachings,

          'out_counts':out_counts,'in_counts':in_counts,'email_counts':email_counts,'chat_counts':chat_counts,
          'open_out':open_out,'open_in':open_in,'open_email':open_email,'open_chat':open_chat,'team':team,
          'open_out_count':open_out_count,'open_in_count':open_in_count,'open_chat_count':open_chat_count,
          'open_email_count':open_email_count
          }

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
    coaching = ChatMonitorinForm.objects.get(id=pk)
    data = {'coaching': coaching}
    return render(request, 'emp-coaching-view-chat.html', data)

def qaCoachingViewOutbound(request,pk):
    coaching=OutboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'qa-coaching-view-outbound.html',data)

def qaCoachingViewInbound(request,pk):
    coaching=InboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'qa-coaching-view-inbound.html',data)

def qaCoachingViewEmail(request,pk):
    coaching=EmailMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'qa-coaching-view-email.html',data)

def qaCoachingViewChat(request,pk):
    coaching=ChatMonitorinForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'qa-coaching-view-chat.html',data)

def signCoaching(request,pk):
    now = datetime.now()
    category=request.POST['category']
    emp_comments=request.POST['emp_comments']

    if category == 'outbound':
        coaching=OutboundMonitoringForm.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category=='inbound':
        coaching = InboundMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category=='chat':
        coaching = ChatMonitorinForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/coaching-success')
    elif category=='email':
        coaching = EmailMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

def coachingSuccess(request):

    return render(request,'coaching-success-message.html')

def coachingDispute(request):
    if request.method == 'POST':

        user = request.user.profile.emp_name
        team= request.user.profile.team

        team=Team.objects.get(name=team)
        data={'team':team}
        return render(request,'coaching-dispute-message.html',data)
    else:
        return redirect('/employees/agenthome')

def qahome(request):
    user=request.user.profile.emp_name
    user_id=request.user.id
    teams=Team.objects.filter(qa=user_id)


    out_coachings=OutboundMonitoringForm.objects.filter(added_by=user).order_by('id').reverse()[:8]
    out_counts=OutboundMonitoringForm.objects.filter(added_by=user).count()
    out_open_counts = OutboundMonitoringForm.objects.filter(added_by=user,status=False).count()

    in_coachings=InboundMonitoringForm.objects.filter(added_by=user).order_by('id').reverse()[:8]
    in_counts=InboundMonitoringForm.objects.filter(added_by=user).count()
    in_open_counts=InboundMonitoringForm.objects.filter(added_by=user,status=False).count()

    chat_coachings=ChatMonitorinForm.objects.filter(added_by=user).order_by('id').reverse()[:8]
    chat_counts=ChatMonitorinForm.objects.filter(added_by=user).count()
    chat_open_counts=ChatMonitorinForm.objects.filter(added_by=user,status=False).count()

    email_coachings=EmailMonitoringForm.objects.filter(added_by=user).order_by('id').reverse()[:8]
    email_counts=EmailMonitoringForm.objects.filter(added_by=user).count()
    email_open_counts=EmailMonitoringForm.objects.filter(added_by=user,status=False).count()

    survey_coachings = SurveyMonitorinForm.objects.filter(added_by=user).order_by('id').reverse()[:8]
    survey_counts=SurveyMonitorinForm.objects.filter(added_by=user).count()
    survey_open_counts=SurveyMonitorinForm.objects.filter(added_by=user,status=False).count()

    data={'out_coachings':out_coachings,'out_counts':out_counts,'out_open_counts':out_open_counts,
          'in_coachings':in_coachings,'in_counts':in_counts,'in_open_counts':in_open_counts,
          'chat_coachings':chat_coachings,'chat_counts':chat_counts,'chat_open_counts':chat_open_counts,
          'email_coachings':email_coachings,'email_counts':email_counts,'email_open_counts':email_open_counts,
          'survey_coachings':survey_coachings,'survey_counts':survey_counts,'survey_open_counts':survey_open_counts,
          'teams':teams
          }

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

        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']
        business_3 = request.POST['business_3']

        b1=categoryTwo(business_1)
        b2=categoryTwo(business_2)
        b3=categoryTwo(business_3)
        bs_total=b1+b2+b3

        closing_1=request.POST['closing_1']
        closing_2 = request.POST['closing_2']

        c1=categoryTwo(closing_1)
        c2=categoryTwo(closing_2)
        cl_total=c1+c2

        compliance_1=request.POST['compliance_1']
        cm1=categoryThree(compliance_1)

        compliance_2 = request.POST['compliance_2']
        cm2=categoryFour(compliance_2)

        compliance_3 = request.POST['compliance_3']
        cm3=categoryThree(compliance_3)

        compliance=cm1+cm2+cm3

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
                                        closing_total=cl_total,total_score=total_score,added_by=added_by,compliance=compliance

                                        )
        outbound.save()
        return redirect('/employees/qahome')


    else:

        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
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


        business_1=request.POST['business_1']
        business_2 = request.POST['business_2']
        business_3 = request.POST['business_3']

        b1=categoryTwo(business_1)
        b2=categoryTwo(business_2)
        b3=categoryTwo(business_3)
        bs_total=b1+b2+b3


        closing_1=request.POST['closing_1']
        closing_2 = request.POST['closing_2']

        c1=categoryTwo(closing_1)
        c2=categoryTwo(closing_2)
        cl_total=c1+c2


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


        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
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


        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
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
        bs1=categorySix(business_1)

        business_2 = request.POST['business_2']
        bs2=categoryTwoChat(business_2)

        bs_total=bs1+bs2

        ce_1=request.POST['ce_1']
        ce1=categoryTwoChat(ce_1)


        ce_2 = request.POST['ce_2']
        ce2=categoryTwoChat(ce_2)


        ce_3 = request.POST['ce_3']
        ce3=categoryTwoChat(ce_3)


        ce_4 = request.POST['ce_4']
        ce4=categoryFive(ce_4)


        ce_5 = request.POST['ce_5']
        ce5=categorySix(ce_5)


        ce_6 = request.POST['ce_6']
        ce6=categoryTwoChat(ce_6)


        ce_total=ce1+ce2+ce3+ce4+ce5+ce6

        compliance_1=request.POST['compliance_1']
        c1=categoryFour(compliance_1)

        compliance_2 = request.POST['compliance_2']
        c2=categoryThree(compliance_2)

        compliance_3 = request.POST['compliance_3']
        c3 = categoryThree(compliance_3)

        compliance_total=c1+c2+c3
        overall_score = ce_total + bs_total
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
                                  added_by=added_by,compliance_total=compliance_total,ce_total=ce_total,business_total=bs_total,
                                  overall_score=overall_score
                               )
        chat.save()
        return redirect('/employees/qahome')

    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
        return render(request, 'chat-coaching-form.html',data)


# Survey Monitoring Form
def surveyCoachingform(request):

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


        oc_1 = request.POST['opening_1']
        oc_2 = request.POST['opening_2']
        oc_3 = request.POST['opening_3']
        oc_4 = request.POST['opening_4']
        oc_5 = request.POST['opening_5']

        sc_1 = request.POST['softskill_1']
        sc_2 = request.POST['softskill_2']
        sc_3 = request.POST['softskill_3']
        sc_4 = request.POST['softskill_4']
        sc_5 = request.POST['softskill_5']

        bc_1 = request.POST['business_1']
        bc_2 = request.POST['business_2']
        bc_3 = request.POST['business_3']
        bc_4 = request.POST['business_4']
        bc_5 = request.POST['business_5']
        bc_6 = request.POST['business_6']
        bc_7 = request.POST['business_7']
        bc_8 = request.POST['business_8']


        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        comments=request.POST['comments']
        added_by=request.user.profile.emp_name

        survey=SurveyMonitorinForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                  customer_contact=customer_contact,call_date=call_date,audit_date=audit_date,campaign=campaign,zone=zone,
                                  concept=concept,call_duration=call_duration,oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,oc_4=oc_4,oc_5=oc_5,
                                  sc_1=sc_1,sc_2=sc_2,sc_3=sc_3,sc_4=sc_4,sc_5=sc_5,bc_1=bc_1,bc_2=bc_2,bc_3=bc_3,bc_4=bc_4,bc_5=bc_5,
                                   bc_6=bc_6,bc_7=bc_7,bc_8=bc_8,areas_improvement=areas_improvement,positives=positives,comments=comments,
                                   added_by=added_by
                                   )
        survey.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
        return render(request, 'survey-coaching-form.html',data)


#Lead Sales Coaching form

def leadSalesCoachingForm(request):
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


        oc_1 = request.POST['opening_1']
        oc_2 = request.POST['opening_2']
        oc_3 = request.POST['opening_3']
        #opening and closing calculation
        oc1=yesTwonoZero(oc_1)
        oc2=yesTwonoZero(oc_2)
        oc3=yesTwonoZero(oc_3)
        oc_total=oc1+oc2+oc3

        sc_1 = request.POST['softskill_1']
        sc_2 = request.POST['softskill_2']
        sc_3 = request.POST['softskill_3']
        sc_4 = request.POST['softskill_4']
        sc_5 = request.POST['softskill_5']
        # Soft Skills calculation
        sc1=yesTwonoZero(sc_1)
        sc2=yesTwonoZero(sc_2)
        sc3=yesTwonoZero(sc_3)
        sc4=yesTwonoZero(sc_4)
        sc5=goodSix(sc_5)
        sc_total=sc1+sc2+sc3+sc4+sc5


        bc_1 = request.POST['business_1']
        bc_2 = request.POST['business_2']
        bc_3 = request.POST['business_3']
        bc_4 = request.POST['business_4']
        bc_5 = request.POST['business_5']
        bc_6 = request.POST['business_6']
        #Business Compliance calculation
        bc1=passFifteen(bc_1)
        bc2=passTen(bc_2)
        bc3=passFifteen(bc_3)
        bc4=passTen(bc_4)
        bc5=passFifteen(bc_5)
        bc6 = passFifteen(bc_6)
        bc_total=bc1+bc2+bc3+bc4+bc5+bc6

        total_score=oc_total+bc_total+sc_total

        areas_improvement=request.POST['areaimprovement']
        positives=request.POST['positives']
        comments=request.POST['comments']
        added_by=request.user.profile.emp_name

        leadsales=LeadSalesMonitoringForm(associate_name=associate_name,emp_id=emp_id,qa=qa,team_lead=team_lead,customer_name=customer_name,
                                  customer_contact=customer_contact,call_date=call_date,audit_date=audit_date,campaign=campaign,zone=zone,
                                  concept=concept,call_duration=call_duration,oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,
                                  sc_1=sc_1,sc_2=sc_2,sc_3=sc_3,sc_4=sc_4,sc_5=sc_5,bc_1=bc_1,bc_2=bc_2,bc_3=bc_3,bc_4=bc_4,bc_5=bc_5,
                                   bc_6=bc_6,areas_improvement=areas_improvement,positives=positives,comments=comments,
                                   added_by=added_by,oc_total=oc_total,bc_total=bc_total,sc_total=sc_total,total_score=total_score
                                   )
        leadsales.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data={'teams':teams,'users':users}
        return render(request, 'lead-sales-coaching-form.html',data)


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

        if audit_form=='chat':
            agent=Profile.objects.get(emp_name=agent)
            team=Team.objects.get(name=team)
            data = {'agent':agent,'team':team}
            return render(request, 'chat-coaching-form.html', data)

        elif audit_form=='outbound':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'outbound-coaching-form.html', data)
        elif audit_form=='leadsales':
            agent = Profile.objects.get(emp_name=agent)
            team = Team.objects.get(name=team)
            data = {'agent': agent, 'team': team}
            return render(request, 'lead-sales-coaching-form.html', data)
    else:
        pass

def coachingSummaryView(request):
    return render(request,'coaching-summary-view.html')

#calculation outbound

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

def categoryThree(val):
    if val=='yes':
        return 30
    elif val=='no':
        return 6
    else:
        return 18

def categoryFour(val):
    if val=='yes':
        return 40
    elif val=='no':
        return 8
    else:
        return 24
def categoryFive(val):

    if val=='good':
        return 20
    elif val=='average':
        return 12
    else:
        return 4
def categorySix(val):

    if val=='good':
        return 15
    elif val=='average':
        return 10
    else:
        return 3

def categoryTwoChat(val):

    if val=='yes':
        return 10
    elif val=='na':
        return 6
    else:
        return 2

def yesTwonoZero(val):
    if val=='yes':
        return 2
    elif val=='no':
        return 0

def goodSix(val):

    if val=='good':
        return 6
    elif val=='average':
        return 3
    else:
        return 0
def passTen(val):
    if val=='yes':
        return 10
    elif val=='no':
        return 0
def passFifteen(val):
    if val=='yes':
        return 15
    elif val=='no':
        return 0