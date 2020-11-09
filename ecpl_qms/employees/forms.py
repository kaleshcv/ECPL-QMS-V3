from django import forms
from .models import Profile,Coaching
from django.contrib.auth.models import User


class ProfileCreation(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('email','emp_name','emp_id','emp_desi','team')

class AddCoaching(forms.ModelForm):
    class Meta:
        model=Coaching
        fields=('feedback','agent')

