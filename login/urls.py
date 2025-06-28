from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('login',views.login,name='login'),
    path('index',views.index,name='index'),
    path('sindex',views.sindex,name='sindex'),
    path('profile',views.profile,name='profile'),
    path('sprofile',views.sprofile,name='sprofile'),
    path('password',views.password,name='password'),
    path('verify',views.verify,name='verify'),
    path('logout',views.logout,name='logout'),
    path('slogout',views.slogout,name='slogout'),
    path('details',views.details,name='details'),
    path('marks',views.marks,name='marks'),
    path('submit',views.msubmit,name='msubmit'),
    path('grade',views.grade,name='grade'),
    path('sgrade',views.sgrade,name='sgrade'),
    path('slogin',views.slogin,name='slogin'),
    path('final',views.final,name='final'),
    path('<email>',views.verify,name='verify'),
    
    
]