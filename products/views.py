from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render


# Create your views here.
from products.models import Product


def index(request):
    return HttpResponse("product index")

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product