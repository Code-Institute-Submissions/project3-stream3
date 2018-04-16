from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from reviews.forms import ReviewForm

def listcoffee(request):
    coffeeproducts = Product.objects.all()
    return render(request, "products/listcoffee.html", {'coffeeproducts': coffeeproducts})
    
def detailcoffee(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ReviewForm()
    return render(request, "products/detailcoffee.html", {'product': product, 'review_form': form})
