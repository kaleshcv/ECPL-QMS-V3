from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile,Team,OutboundMonitoringForm
from . import forms
from django.contrib.auth.models import User

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
            print('user desi is -------',user.profile.emp_desi)


            if user.profile.emp_desi=='Manager':


                return render(request, 'qa-home.html')

            if user.profile.emp_desi=='qa':
                return redirect('/employees/qahome')

            else:
                return redirect('/employees/agenthome')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/employees/index')


def agenthome(request):
    user = request.user.profile.emp_name
    team_name=request.user.profile.team
    print(team_name)
    coachings = OutboundMonitoringForm.objects.filter(associate_name=user)
    team=Team.objects.get(name=team_name)
    counts = OutboundMonitoringForm.objects.filter(associate_name=user).count()
    open_coachings = OutboundMonitoringForm.objects.filter(associate_name=user,status=False)
    data={'coachings':coachings,'team':team,'count':counts,'open_coachings':open_coachings}
    return render(request, 'agent-home.html',data)


def empCoachingView(request,pk):
    coaching=OutboundMonitoringForm.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'emp-coaching-view.html',data)

def signCoaching(request,pk):

    coaching=OutboundMonitoringForm.objects.get(id=pk)
    coaching.status=True
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

