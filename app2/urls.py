from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('clothes/',clothes,name='clothes'),
    path('shoes/',shoes,name='shoes'),
]