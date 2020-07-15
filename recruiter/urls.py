from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.SignUp), 
    path('insertrecord',views.companyinsert),
    path('signin',views.signin), 
    path('logout',views.logout),
    path('postjob',views.postjob),
    path('trydemo',views.demo),
    path('viewdone',views.candidate),
    path('categories',views.category),
    path('dashboard',views.dashboard),
    path('Dashboard',views.email)
]