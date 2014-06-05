from django.views.generic import ListView, DetailView


# Create your views here.
from products.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product