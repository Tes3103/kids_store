from django.shortcuts import render
from .models import product

# Create your views here.


def all_products(request):
    """ A view to show all products, inclusing sorting and search quieres """

    products = product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
