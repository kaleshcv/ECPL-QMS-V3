from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileCreation(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('email','emp_name','emp_id','emp_desi','team')



