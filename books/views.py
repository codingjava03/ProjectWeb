from django.shortcuts import render
from .models import Book

def all_books(request):
    books=Book.objects.all()
    return render(request,'all_books.html',{'books':books})
def available_books(request):
    books=Book.available_books.all()
    return render(request,'available_books.html',{'books':books})
