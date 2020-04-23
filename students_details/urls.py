
from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf.urls import include,url
from django.conf.urls import *
from django.contrib.auth import views as auth_views,login


app_name = 'students_details'
urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('students_marks/', views.students_marks),
    path('students_list/', views.show_students_list),
    path('edit_marks/<int:pk>', views.edit_marks),
    path('delete_student/<int:pk>', views.delete_student),
]

