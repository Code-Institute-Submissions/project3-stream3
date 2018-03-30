from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.

def listcoffee(request):
    coffeeproducts = Product.objects.all()
    return render(request, "products/listcoffee.html", {'coffeeproducts': coffeeproducts})
