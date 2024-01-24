import os
from django.shortcuts import render,redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf = Book.objects.all()
    return render(request, os.path.sep.join(['book','library.html']),{'shelf':shelf})
def upload(request):
    upload= BookCreate()
    if request.method == 'POST':
        upload= BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""something went wrong.Please reload the webpage by click <a href="{{url:'index'}}>reload</a>" """)
    else:
        return render(request, 'Book/upload_from.html',{'upload_form:',upload})   
    
    
def update_Book(request,Book_id):
    Book_id = int(Book_id)
    try:
        Book_shelf=Book.objects.get(id=Book_id)
    except Book.DoesNotExist:
        return redirect('index')
    Book_form = BookCreate(request.POST or None,instance=Book_shelf)
    if Book_form.is_valid():
        Book_form.save()
        return redirect('index')
    return redirect(request, 'Book/upload_form.html',{'upload_form':Book_form})
def delete_Book(request,Book_id):
    Book_id = int (Book_id)
    try:
        Book_shelf = Book.objects.get(id = Book_id)
    except Book.DoesNotExist:
        return redirect('index')
    Book_shelf.delete()
    return redirect('index')