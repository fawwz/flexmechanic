from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('signupopt', views.signupopt, name='signupopt'),
    path('customersignup', views.customerSignUp, name='customersignup'),
    path('mechanicsignup', views.mechanicSignUp, name='mechanicsignup'),
    path('signin', views.signin, name='signin'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('services', views.services, name='services'),
    path('contactus', views.contactus, name='contactus'),
    path('logout/', views.logout_view, name='logout'),
    path('indexcustomer', views.indexcustomer, name='indexcustomer'),
    path('indexmechanic', views.indexmechanic, name='indexmechanic'),
    path('mechanicprofile', views.mechanicprofile, name='mechanicprofile'),


    # path('signupopt/customer',views, name='customersignup'),
    # path('signupopt/mechanic',views , name='mechanicsignup')  
]
