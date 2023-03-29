from django.shortcuts import render
from django.db.models import Q
from .models import Product

def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
