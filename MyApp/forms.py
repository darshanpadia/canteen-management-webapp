from django import forms
from django.contrib.auth.models import User
from django.core import validators
from MyApp.models import UserProfileInfo

class FormNewUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = fields = ('username','email','password')

class FormUserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('somaiya_id','profile_pic')
    # def clean(self):
    #     super_cleaned = super().clean()
    #     pwd = super_cleaned.get("password")
    #     cpwd = super_cleaned.get("confirm_pass")
    #     if pwd != cpwd:
    #         raise forms.ValidationError("Passwords do not match!")
    #     else:
    #         user = User.objects.get_or_create(userid=super_cleaned.get('Somaiya_id'), password=pwd)


class FormLogin(forms.Form):
    Somaiya_id = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        super_cleaned = super().clean()
        id = super_cleaned.get("Somaiya_id")
        pwd = super_cleaned.get("password")
