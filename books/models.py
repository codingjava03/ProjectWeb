from django.db import models

class AvailableBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField()
    is_available = models.BooleanField(default=True)
    
    objects = models.Manager()  # Default manager
    available_books = AvailableBooksManager()  # Custom manager
    
    def __str__(self):
        return self.title
    

    

