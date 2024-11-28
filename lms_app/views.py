from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *


# Create your views here.

# index page | homepage
def base(reqeust):
    if reqeust.method == 'POST':
        addbook = BookForm(reqeust.POST, reqeust.FILES)
        if addbook.is_valid():
            addbook.save()
        addcat = CategoryForm(reqeust.POST)
        if addcat.is_valid():
            addcat.save()
            
    context = {
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'form': BookForm(),
        'formcat':CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'soldbooks':Book.objects.filter(status='sold').count(),
        'rentedbooks':Book.objects.filter(status='rental').count(),
        'avibooks':Book.objects.filter(status='available').count(),
        
    }
    return render(reqeust, 'pages/index.html', context)
# books page
def book(reqeust):
    search = Book.objects.all()
    title = None
    if 'search_name' in reqeust.GET:
        title = reqeust.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    context = {
        'category':Category.objects.all(),
        'books':search,
        'formcat':CategoryForm(),
    }
    
    return render(reqeust, 'pages/books.html', context)

def update(reqeust, id):
    bookid = Book.objects.get(id=id)
    if reqeust.method == 'POST':
        booksave = BookForm(reqeust.POST, reqeust.FILES, instance=bookid)
        if booksave.is_valid:
            booksave.save()
            return redirect('/')
    else:
        booksave = BookForm(instance=bookid)        
    
    context = {
        'form':booksave
        
    }
    return render(reqeust, 'pages/update.html', context)

def delete(reqeust, id):
    del_book = get_object_or_404(Book, id=id)
    if reqeust.method == 'POST':
        del_book.delete()
        return redirect('/')
    
    context = {
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        
    }
    return render(reqeust, 'pages/delete.html', context)