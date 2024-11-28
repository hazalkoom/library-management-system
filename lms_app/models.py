from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)

    
    
    def __str__(self):
        return self.name

class Book(models.Model):
    
    x = [
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True, blank=True)
    book_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    author_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    rental_per_day = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_rental = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default= True)
    status = models.CharField(max_length=30, choices=x, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    
    
    
    def __str__(self):
        return self.title