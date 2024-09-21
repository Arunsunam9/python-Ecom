

from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
    data = { 'title':"Daraz Ecom | Home page Dymanic title"}
    return render(request, 'home.html',data)


def about(request):
    data = { 'title':"Daraz Ecom | About page Dymanic title"}

    return render(request, 'about.html',data)


def contact(request):
    data = { 'title':"Daraz Ecom | Contact page Dymanic title"}

    return render(request, 'contact.html',data)


# def product(request):
#     data = { 'title':"Daraz Ecom | Product page Dymanic title"}

#     return render(request, 'product.html',data)


