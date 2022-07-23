from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CustomUser,BookDetails

# Register View
def register(request):
    if request.method=="POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = CustomUser(
                    email=email,
                    name=name, 
                    )
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/login')
    return render(request, 'testapp/register.html')

#Login View
def user_login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/show')
        else:
            return render(request, 'testapp/login.html', 
                {'message': 'Wrong Email or Password'}
            )
    return render(request, 'testapp/login.html')

#Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

#Book CRUD View
@login_required
def show_Book(request):
    if request.method=="POST":
        bookname = request.POST.get("bookname")
        authors = request.POST.get("authors")
        publisher = request.POST.get("publisher")
        book = BookDetails(bookname=bookname,
                        authors=authors,
                        publisher=publisher
                    )
        book.save()
    book=BookDetails.objects.all()
    return render(request, 'testapp/dashboard.html', {'books':book})

#Book update View
def update_book(request, id):
    if request.method=="POST":
        bookname = request.POST.get('bookname')
        authors = request.POST.get('authors')
        publisher = request.POST.get('publisher')
        book= BookDetails.objects.get(id=id)
        book.bookname=bookname
        book.authors=authors
        book.publisher=publisher
                    
        book.save()
        return HttpResponseRedirect("/show") 
    return render(request, "testapp/update_book.html")

# Delet Book View
def delete_book(request, id):
    if request.method=="POST":
        book=BookDetails.objects.get(id=id)
        book.delete()
    return HttpResponseRedirect('/show')

# Show Book Details View
def detail(request):
    if request.method=="GET":
        book=BookDetails.objects.all()
        return render(request, 'testapp/view.html', {'books':book})
    