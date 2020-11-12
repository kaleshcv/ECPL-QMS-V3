from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile,Coaching,Team
from . import forms
from .forms import AddCoaching
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
                form=AddCoaching()
                coaching = Coaching.objects.filter(agent=user)
                data = {'coaching': coaching,'form':form}
                return render(request, 'qa-home.html', data)

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
    coachings = Coaching.objects.filter(agent=user)
    team=Team.objects.get(name=team_name)
    counts = Coaching.objects.filter(agent=user).count()
    open_coachings = Coaching.objects.filter(agent=user,status=False)
    data={'coachings':coachings,'team':team,'count':counts,'open_coachings':open_coachings}
    return render(request, 'agent-home.html',data)


def editprofile(request):
    if request.method == 'POST':
        edit_form = forms.ProfileCreation(request.POST, request.FILES, instance=request.user.profile)
        if edit_form.is_valid():
            # saving
            instance = edit_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')
    else:

        edit_form = forms.ProfileCreation(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': edit_form})



def addcoaching(request):
    if request.method== 'POST':
        ticket_no = request.POST['ticket_no']
        agent = request.POST['agent']
        feedback = request.POST['feedback']
        qa = request.POST['qa']
        date=request.POST['date']
        coaching = Coaching(ticket_no=ticket_no,agent=agent,feedback=feedback,qa=qa,date=date)
        coaching.save()

        return redirect('/employees/qahome')

    else:
        users=User.objects.all()
        data={'users':users}
        return render(request, 'add-coaching.html',data)

def empCoachingView(request,pk):
    coaching=Coaching.objects.get(id=pk)
    data={'coaching':coaching}
    return render(request,'emp-coaching-view.html',data)

def signCoaching(request,pk):

    coaching=Coaching.objects.get(id=pk)
    coaching.status=True
    coaching.save()
    return redirect('/employees/agenthome')


def qahome(request):
    user=request.user.profile.emp_name
    coachings=Coaching.objects.filter(qa=user).order_by('id').reverse()[:10]

    counts=Coaching.objects.filter(qa=user).count()

    data={'coachings':coachings,'counts':counts}

    return render(request,'qa-home.html',data)

def outboundCoachingform(request):
    return render(request,'outbound-coaching-form.html')
