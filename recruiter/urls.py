from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup',views.SignUp), 
    path('insertrecord',views.companyinsert),
    path('signin',views.signin), 
    path('logout',views.logout),
    path('postjob',views.postjob),
    path('trydemo',views.demo),
    path('viewdone',views.candidate),
    path('categories',views.category),
    path('personality',views.personality),
    path('dashboard',views.dashboard),
    path('email',views.sentinvite)
   
    
    
]