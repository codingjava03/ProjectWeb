from django.urls import path
from .views import register,login_page,logout_view,home

urlpatterns=[
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login'),
    path('home/',home,name='home'),
    path('logout_view/',logout_view,name='logout')
]