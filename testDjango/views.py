from django.http.response import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView
from products.models import Product

class ContactTemplateView(TemplateView):
    template_name = ""

def cart(request):
    return HttpResponse("cart")

def contact(request):
    return HttpResponse("contact")

def checkout(request):
    return HttpResponse("checkout")

def payment(request):
    return HttpResponse("payment")

def search(request, keyword):
    result = Product.objects.filter(Q(product_name__contains=keyword) | Q(product_info__contains=keyword))
    print(result)
    return HttpResponse(keyword)