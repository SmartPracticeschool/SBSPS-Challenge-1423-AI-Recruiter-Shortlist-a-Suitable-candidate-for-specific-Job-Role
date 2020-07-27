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
    # path('Dashboard',views.dashboard),
    url(r'(?P<Resume_ID>\d+)/$',views.dashboard,name ='Dashboard'),
    url(r'(?P<name>\D+)/$',views.sentinvite,name ='invitation')
]