from django.urls import path
from .views import all_books,available_books

urlpatterns = [
    path('',all_books,name='all_books'),
    path('all-books/',all_books,name='all_books'),
    path('available-books/',available_books,name='available-booka'),
]
