from django.http.response import HttpResponse

def cart(request):
    return HttpResponse("cart")

def contact(request):
    return HttpResponse("contact")

def checkout(request):
    return HttpResponse("checkout")

def payment(request):
    return HttpResponse("payment")