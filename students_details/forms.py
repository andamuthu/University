from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from students_details.models import *
from django.db import models

class SignupForm(forms.Form):
    user_name = forms.CharField(required=True, label='Enter Username')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput,label='Enter Password')
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Re-enter Password')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        return cleaned_data

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].strip()
        if len(user_name) < 3:
            raise forms.ValidationError("Enter more than 3 letters")

        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("You entered user is already exists")

        return user_name

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 5:
            raise forms.ValidationError("password is too short")
        return password


class LoginForm(forms.Form):
    user_name = forms.CharField(required=True, label='Enter Username')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput,label='Enter Password')

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        return cleaned_data


class DashboardForm(forms.Form):
    student_name = forms.CharField()
    Tamil = forms.IntegerField()
    English = forms.IntegerField()
    Maths = forms.IntegerField()
    Science = forms.IntegerField()
    Socialscience = forms.IntegerField()
    # Total_Marks = forms.IntegerField()

    def clean(self):
        cleaned_data = super(DashboardForm, self).clean()
        return cleaned_data

    if StudentsMarks.objects.filter(student_name=student_name).exists():
        raise forms.ValidationError("You entered student is already exists")


class EditForm(forms.ModelForm):
    class Meta:
        model = StudentsMarks
        exclude = ['student_name','total_marks','created_by']

    def clean(self):
        cleaned_data = super(EditForm, self).clean()
        return cleaned_data

