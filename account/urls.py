from django.urls import path
from . import views

urlpatterns = [
    path('User_Signup',views.index),
    path('Insertrecord',views.Insertrecord)
]