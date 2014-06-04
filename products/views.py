from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("product index")

class ProductListView(ListView):
    # model =
    context_object_name = "product_list"

    def get(self, request, *args, **kwargs):
        return HttpResponse("list")

class ProductDetailView(DetailView):
    # model =

    def get(self, request, *args, **kwargs):
        return HttpResponse(kwargs['product_id'])