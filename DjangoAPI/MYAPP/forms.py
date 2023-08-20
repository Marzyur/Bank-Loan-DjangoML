# import django
# from django.forms import ModelForm
from django import forms
from .models import Approval

class ApprovalForm(forms.ModelForm):
    class Meta:
        model=Approval
        fields='__all__'

