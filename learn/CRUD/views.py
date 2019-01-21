from django.shortcuts import render, redirect
from . models import BookList
# Create your views here.

def index(request):
    books = BookList.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'index.html', context)

def addBook(request):
    return render(request, 'add_book.html')

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')

def delete(request, id):
    delete_book = BookList.objects.get(pk=id)
    delete_book.delete()
    return redirect('/')

def edit(request, id):
    edit_books = BookList.objects.get(pk=id)
    context = {
        'edit_book' : edit_books
    }
    return render(request, 'edit.html', context)

def update(request, id):
    update_book = BookList.objects.get(pk=id)
    update_book.title = request.GET['title']
    update_book.price = request.GET['price']
    update_book.author = request.GET['author']

    update_book.save()
    return redirect('/')
