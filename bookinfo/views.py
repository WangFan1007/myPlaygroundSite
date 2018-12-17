from django.shortcuts import render,redirect,HttpResponse
from bookinfo import models

# Create your views here.

def book_list(request):
    books = models.Book.objects.all().order_by('id')
    return render(request, 'book_list.html', {'books':books})

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('publisher')
#        publisher = models.Publisher.objects.get(id=pub_id)
        book = models.Book.objects.create(name=book_name,publisher_id=pub_id)
        return redirect('/book_list')
    publishers = models.Publisher.objects.all().order_by('id')
    return render(request,'add_book.html',{'publishers':publishers})

def publisher_list(request):
    publishers = models.Publisher.objects.all().order_by('id')
    return render(request, 'publisher_list.html', {'publishers': publishers})

def del_publisher(request):
    del_id = request.GET.get('del_id')
    del_pub = models.Publisher.objects.get(id=del_id)
    del_pub.delete()
    return redirect('/publisher_list')

def add_publisher(request):

    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        models.Publisher.objects.create(name=name)
        return redirect('/publisher_list')
    return render(request, 'add_publisher.html')