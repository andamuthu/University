from django.shortcuts import render
from django.db import IntegrityError
from students_details.forms import *
from students_details.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def students_list():
    return StudentsMarks.objects.filter(created_by=get_current_user())


@login_required(login_url='/students_details/login')
def show_students_list(request):
    return render(request, 'student_name_list.html', {'students_list': students_list()})


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'signup_form': SignupForm(), })

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name'].strip()
            password = form.cleaned_data['password'].strip()
            user = User.objects.create(username=user_name)
            user.set_password(password)
            user.save()
            message = 'User name " {} " is registred successfully'.format(user_name)
            form = SignupForm()
        else:
            message = 'Please correct below errors'
        return render(request, "signup.html",
                      {'message': message, 'signup_form': form})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_form': LoginForm(), })

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name'].strip()
            password = form.cleaned_data['password'].strip()
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'dashboard.html',
                              {'dashboard_form': DashboardForm()})
            else:
                message = 'Invalid username/password'
        else:
            message = 'Please correct below errors'
        return render(request, "login.html",
                      {'message': message, 'login_form': form})


def logout_view(request):
    user = request.user
    logout(request)
    return render(request, 'logout.html', {'user': user})


@login_required(login_url='/students_details/login')
def students_marks(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', {'dashboard_form': DashboardForm()})

    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name'].strip()
            tamil = form.cleaned_data['Tamil']
            english = form.cleaned_data['English']
            maths = form.cleaned_data['Maths']
            science = form.cleaned_data['Science']
            socialscience = form.cleaned_data['Socialscience']
            total_marks = tamil + english + maths + science + socialscience
            StudentsMarks.objects.create(student_name=student_name, tamil=tamil, english=english,
                                         maths=maths, science=science, socialscience=socialscience,
                                         total_marks=total_marks)
            message = ' " {} " marks are added successfully'.format(student_name)
            return render(request, 'student_name_list.html', {'message': message, 'students_list': students_list()})
        else:
            message = 'Please correct below errors'
            return render(request, 'dashboard.html', {'message': message, 'dashboard_form': DashboardForm()})


def edit_marks(request, pk):
    if request.method == 'GET':
        edit_student = StudentsMarks.objects.get(id=pk)
        form = EditForm(instance=edit_student)
        return render(request, 'edit_marks.html',
                      {'edit_student': edit_student, 'editform': form})

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            tamil = form.cleaned_data['tamil']
            english = form.cleaned_data['english']
            maths = form.cleaned_data['maths']
            science = form.cleaned_data['science']
            socialscience = form.cleaned_data['socialscience']
            mark_update = StudentsMarks.objects.get(id=pk)
            # update(tamil=tamil, english=english, science=science, socialscience=socialscience, )
            mark_update.tamil = tamil
            mark_update.english = english
            mark_update.maths = maths
            mark_update.science = science
            mark_update.socialscience = socialscience
            mark_update.save()
            message = ' " {} " marks are updated successfully'.format(mark_update.student_name)
            return render(request, 'student_name_list.html',
                          {'message': message, 'students_list': students_list(), })
        else:
            message = 'Form is not valid'
            edit_student = StudentsMarks.objects.get(id=pk)
            form = EditForm(instance=edit_student)
            # form = EditForm()
            return render(request, 'edit_marks.html',
                          {'message': message, 'edit_student': edit_student, 'editform': form})


def delete_student(request, pk):
    if request.method == 'GET':
        student = StudentsMarks.objects.get(id=pk)
        student.delete()
        message = ' "{}"  Student is deleted successfully'.format(student.student_name)
        return render(request, 'student_name_list.html',
                      {'message': message, 'students_list': students_list(), })
