from django.contrib.auth import logout
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.views.generic import DetailView, UpdateView, View


class ProfileDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("profile view")

class ProfileUpdateView(UpdateView):
    def post(self, request, *args, **kwargs):
        return HttpResponse("updated")

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("register form")

    def post(self, request, *args, **kwargs):
        return HttpResponse("register posted")