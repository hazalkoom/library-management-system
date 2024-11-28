from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('books', views.book, name= 'books'),
    path('update/<int:id>', views.update, name= 'update'),
    path('delete/<int:id>', views.delete, name= 'delete'),
]
