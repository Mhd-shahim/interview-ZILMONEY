from django.shortcuts import render,HttpResponse
from .models import product

# Create your views here.

def product_details(request,pk):
    products = product.objects.get(pk=pk)
    return render(request, "product_details.html",{'prod' : products})

def all_products(request):
    products = product.objects.all()
    return render(request, "products.html", {'prod' : products})

def purchase(request,pk):
    products = product.objects.get(pk=pk)
    products.available_quantity = products.available_quantity-1
    products.save()
    return HttpResponse("Item Purchased")