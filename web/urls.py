from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from books.views import *
urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',lambda request: redirect('login')),
    path('books/',include('books.urls'))
]
